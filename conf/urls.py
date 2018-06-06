from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.views.static import serve

import core.views
import conf.sitemaps

sitemaps = {
    'static': conf.sitemaps.StaticViewSitemap,
}

urlpatterns = [
    url(
        r"^sitemap\.xml$", sitemap, {'sitemaps': sitemaps},
        name='sitemap'
    ),
    url(
        r"^robots\.txt$",
        TemplateView.as_view(
            template_name='robots.txt', content_type='text/plain'
        ),
        name='robots'
    ),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(
        r"^$",
        core.views.LandingPageCMSView.as_view(),
        name="index"
    ),
    url(
        r"^industries/$",
        core.views.IndustriesLandingPageCMSView.as_view(),
        name="industries"
    ),
    url(
        r"^industries/(?P<slug>.+)/$",
        core.views.IndustryPageCMSView.as_view(),
        name="industry"
    ),
    url(
        r"^uk-setup-guide/$",
        core.views.SetupGuideLandingPageCMSView.as_view(),
        name="setup-guide"
    ),
    url(
        r"^guide-page/$",
        core.views.SetupGuidePageCMSView.as_view(),
        name="guide-page"
    ),
    url(
        r"^contact/$",
        core.views.ContactFormView.as_view(),
        name="contact"
    ),
    url(
        r"^terms-and-conditions/$",
        core.views.TermsAndConditionsView.as_view(),
        name="terms-and-conditions"
    ),
    url(
        r"^privacy-and-cookies/$",
        core.views.PrivacyAndCookiesView.as_view(),
        name="privacy-and-cookies"
    ),
    prefix_default_language=False,
)


if settings.THUMBNAIL_STORAGE_CLASS_NAME == 'local-storage':
    urlpatterns += [
        url(
            r'^media/(?P<path>.*)$',
            serve,
            {'document_root': settings.MEDIA_ROOT}
        ),
    ]
