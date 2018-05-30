from django.conf import settings
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.views.static import serve

import core.views
import conf.sitemaps

sitemaps = {
    'static': conf.sitemaps.StaticViewSitemap,
    'industries': conf.sitemaps.SectorLandingPageSitemap,
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
    url(
        r"^$",
        core.views.LandingPageCMSView.as_view(),
        name="index"
    ),
    url(
        r'^subscribe/$',
        core.views.AnonymousSubscribeFormView.as_view(),
        name='subscribe'
    ),
    url(
        r'^feedback/$',
        core.views.LeadGenerationFormView.as_view(),
        name='lead-generation'
    ),
]


if settings.THUMBNAIL_STORAGE_CLASS_NAME == 'local-storage':
    urlpatterns += [
        url(
            r'^media/(?P<path>.*)$',
            serve,
            {'document_root': settings.MEDIA_ROOT}
        ),
    ]