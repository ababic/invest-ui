from urllib.parse import urlparse

from django.utils.cache import set_response_etag
from django.utils import translation
from django.utils.functional import cached_property

from directory_cms_client.client import cms_api_client
from directory_constants.constants import cms
from directory_cms_client.helpers import handle_cms_response_allow_404

from core.helpers import get_untranslated_url


class LocalisedURLsMixin:
    @property
    def localised_urls(self):
        localised = []
        requested_language = translation.get_language()
        url_parts = urlparse(self.request.build_absolute_uri())
        base_url = f'{url_parts.scheme}://{url_parts.netloc}/'

        for code, language in self.available_languages:
            if code == requested_language:
                continue
            else:
                if code == 'en-gb':
                    localised_page = base_url + get_untranslated_url(
                        self.request.path)[1:]
                else:
                    localised_page = base_url + code + get_untranslated_url(
                        self.request.path)
                localised.append([localised_page, code])

        return localised

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(
            localised_urls=self.localised_urls,
            *args, **kwargs)


class SetEtagMixin:
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.method == 'GET':
            response.add_post_render_callback(set_response_etag)
        return response


class GetSlugFromKwargsMixin:
    @property
    def slug(self):
        return self.kwargs.get('slug')


class GetCMSComponentMixin:
    @cached_property
    def cms_component(self):
        response = cms_api_client.lookup_by_slug(
            slug=self.component_slug,
            language_code=translation.get_language(),
            draft_token=self.request.GET.get('draft_token'),
            service_name=cms.COMPONENTS,
        )
        return handle_cms_response_allow_404(response)

    def get_context_data(self, *args, **kwargs):

        activated_language = translation.get_language()
        activated_language_is_bidi = translation.get_language_info(
            activated_language)['bidi']

        cms_component = None
        component_is_bidi = activated_language_is_bidi

        if self.cms_component:
            cms_component = self.cms_component
            component_supports_activated_language = activated_language in \
                dict(self.cms_component['meta']['languages'])
            component_is_bidi = activated_language_is_bidi and \
                component_supports_activated_language

        return super().get_context_data(
            component_is_bidi=component_is_bidi,
            cms_component=cms_component,
            *args, **kwargs)
