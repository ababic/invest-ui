from directory_cms_client.constants import (
    EXPORT_READINESS_HIGH_POTENTIAL_OPPORTUNITY_FORM_SLUG,
    EXPORT_READINESS_HIGH_POTENTIAL_OPPORTUNITY_FORM_SUCCESS_SLUG
)
from directory_cms_client.client import cms_api_client

from django.conf import settings
from django.http import Http404
from django.template.response import TemplateResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.functional import cached_property

from core.helpers import handle_cms_response
from opportunities import forms


class FeatureFlagMixin:
    def dispatch(self, *args, **kwargs):
        if not settings.FEATURE_FLAGS['HIGH_POTENTIAL_OPPORTUNITIES_ON']:
            raise Http404()
        return super().dispatch(*args, **kwargs)


class HighPotentialOpportunityDetailView(FeatureFlagMixin, TemplateView):
    template_name = 'opportunities/high-potential-opportunity-detail.html'

    def get_context_data(self, **kwargs):
        response = cms_api_client.lookup_by_slug(
            slug=self.kwargs.get('slug'),
            language_code=settings.LANGUAGE_CODE,
            draft_token=self.request.GET.get('draft_token'),
        )

        if response.status_code == 404:
            raise Http404()
        page = handle_cms_response(response)
        return super().get_context_data(page=page, **kwargs)


class HighPotentialOpportunityFormView(FeatureFlagMixin, FormView):
    template_name = 'opportunities/high-potential-opportunities-form.html'
    success_template_name = (
        'opportunities/high-potential-opportunities-success.html'
    )
    form_class = forms.HighPotentialOpportunityForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['field_attributes'] = self.page
        kwargs['opportunity_choices'] = [
            (opportunity['pdf_document'], opportunity['heading'])
            for opportunity in self.page['opportunity_list']
        ]
        initial_opportunities_value = [
            item['pdf_document']
            for item in self.page['opportunity_list']
            if item['meta']['slug'] == self.kwargs['slug']
        ]
        kwargs['initial']['opportunities'] = initial_opportunities_value
        return kwargs

    def get_context_data(self, **kwargs):
        return super().get_context_data(page=self.page, **kwargs)

    def form_valid(self, form):
        form.save()
        opportunities = [
            item for item in self.success_page['opportunity_list']
            if item['pdf_document'] in form.cleaned_data['opportunities']
        ]
        return TemplateResponse(
            self.request,
            self.success_template_name,
            {
                'page': self.success_page,
                'view': self,
                'opportunities': opportunities
            }
        )

    @cached_property
    def page(self):
        response = cms_api_client.lookup_by_slug(
            slug=EXPORT_READINESS_HIGH_POTENTIAL_OPPORTUNITY_FORM_SLUG,
            language_code=settings.LANGUAGE_CODE,
            draft_token=self.request.GET.get('draft_token'),
        )
        if response.status_code == 404:
            raise Http404()
        return handle_cms_response(response)

    @cached_property
    def success_page(self):
        response = cms_api_client.lookup_by_slug(
            slug=EXPORT_READINESS_HIGH_POTENTIAL_OPPORTUNITY_FORM_SUCCESS_SLUG,
            language_code=settings.LANGUAGE_CODE,
            draft_token=self.request.GET.get('draft_token'),
        )
        return handle_cms_response(response)
