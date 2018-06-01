from directory_cms_client import constants as cms_constants
from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, User as ZendeskUser

from django.conf import settings
from django.urls import reverse
from django.utils import translation
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView

from api_client import api_client
from core.helpers import cms_client, handle_cms_response
from core import forms, helpers, mixins

from directory_cms_client.constants import (
    EXPORT_READINESS_TERMS_AND_CONDITIONS_SLUG,
    EXPORT_READINESS_PRIVACY_AND_COOKIES_SLUG,
)

ZENPY_CREDENTIALS = {
    'email': settings.ZENDESK_EMAIL,
    'token': settings.ZENDESK_TOKEN,
    'subdomain': settings.ZENDESK_SUBDOMAIN
}
# Zenpy will let the connection timeout after 5s and will retry 3 times
zenpy_client = Zenpy(timeout=5, **ZENPY_CREDENTIALS)


class CMSFeatureFlagMixin:
    def dispatch(self, *args, **kwargs):
        translation.activate(self.request.LANGUAGE_CODE)
        return super().dispatch(*args, **kwargs)


class LandingPageCMSView(
    mixins.CMSLanguageSwitcherMixin, mixins.ActiveViewNameMixin,
    CMSFeatureFlagMixin, TemplateView
):
    active_view_name = 'index'
    template_name = 'core/landing_page.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(
            page=self.get_cms_page(),
            search_form=forms.SearchForm(),
            *args,
            **kwargs
        )

    def get_cms_page(self):
        response = helpers.cms_client.lookup_by_slug(
            slug=cms_constants.FIND_A_SUPPLIER_LANDING_SLUG,
            language_code=translation.get_language(),
            draft_token=self.request.GET.get('draft_token'),
        )
        return helpers.handle_cms_response(response)


class IndustriesLandingPageCMSView(
    mixins.CMSLanguageSwitcherMixin, mixins.ActiveViewNameMixin,
    CMSFeatureFlagMixin, TemplateView
):
    active_view_name = 'index'
    template_name = 'core/industries_landing_page.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(
            page=self.get_cms_page(),
            search_form=forms.SearchForm(),
            *args,
            **kwargs
        )

    def get_cms_page(self):
        response = helpers.cms_client.lookup_by_slug(
            slug=cms_constants.FIND_A_SUPPLIER_LANDING_SLUG,
            language_code=translation.get_language(),
            draft_token=self.request.GET.get('draft_token'),
        )
        return helpers.handle_cms_response(response)


class IndustryPageCMSView(
    mixins.CMSLanguageSwitcherMixin, mixins.ActiveViewNameMixin,
    CMSFeatureFlagMixin, TemplateView
):
    active_view_name = 'index'
    template_name = 'core/industry_page.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(
            page=self.get_cms_page(),
            search_form=forms.SearchForm(),
            *args,
            **kwargs
        )

    def get_cms_page(self):
        response = helpers.cms_client.lookup_by_slug(
            slug=cms_constants.FIND_A_SUPPLIER_LANDING_SLUG,
            language_code=translation.get_language(),
            draft_token=self.request.GET.get('draft_token'),
        )
        return helpers.handle_cms_response(response)


class SetupGuideLandingPageCMSView(
    mixins.CMSLanguageSwitcherMixin, mixins.ActiveViewNameMixin,
    CMSFeatureFlagMixin, TemplateView
):
    active_view_name = 'index'
    template_name = 'core/setup_guide_landing_page.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(
            page=self.get_cms_page(),
            search_form=forms.SearchForm(),
            *args,
            **kwargs
        )

    def get_cms_page(self):
        response = helpers.cms_client.lookup_by_slug(
            slug=cms_constants.FIND_A_SUPPLIER_LANDING_SLUG,
            language_code=translation.get_language(),
            draft_token=self.request.GET.get('draft_token'),
        )
        return helpers.handle_cms_response(response)


class SetupGuidePageCMSView(
    mixins.CMSLanguageSwitcherMixin, mixins.ActiveViewNameMixin,
    CMSFeatureFlagMixin, TemplateView
):
    active_view_name = 'index'
    template_name = 'core/setup_guide_page.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(
            page=self.get_cms_page(),
            search_form=forms.SearchForm(),
            *args,
            **kwargs
        )

    def get_cms_page(self):
        response = helpers.cms_client.lookup_by_slug(
            slug=cms_constants.FIND_A_SUPPLIER_LANDING_SLUG,
            language_code=translation.get_language(),
            draft_token=self.request.GET.get('draft_token'),
        )
        return helpers.handle_cms_response(response)


class ContactFormView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(
            contact_form=forms.ContactForm(),
            *args, **kwargs
        )


class TermsAndConditionsView(TemplateView):
    template_name = 'core/plain_cms_page.html'

    def get_context_data(self, *args, **kwargs):
        response = cms_client.lookup_by_slug(
            slug=EXPORT_READINESS_TERMS_AND_CONDITIONS_SLUG,
            language_code=translation.get_language(),
            draft_token=self.request.GET.get('draft_token'),
        )
        return super().get_context_data(
            page=handle_cms_response(response),
            *args, **kwargs
        )


class PrivacyAndCookiesView(TemplateView):
    template_name = 'core/plain_cms_page.html'

    def get_context_data(self, *args, **kwargs):
        response = cms_client.lookup_by_slug(
            slug=EXPORT_READINESS_PRIVACY_AND_COOKIES_SLUG,
            language_code=translation.get_language(),
            draft_token=self.request.GET.get('draft_token'),
        )
        return super().get_context_data(
            page=handle_cms_response(response),
            *args, **kwargs
        )
