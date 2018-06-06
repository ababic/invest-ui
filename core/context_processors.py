from django.conf import settings
from core.helpers import get_language_from_prefix


def feature_flags(request):
    return {
        'features': {
        }
    }


def analytics(request):
    return {
        'analytics': {
            'GOOGLE_TAG_MANAGER_ID': settings.GOOGLE_TAG_MANAGER_ID,
            'GOOGLE_TAG_MANAGER_ENV': settings.GOOGLE_TAG_MANAGER_ENV,
            'UTM_COOKIE_DOMAIN': settings.UTM_COOKIE_DOMAIN,
        }
    }


def untranslated_url(request):
    current_language = get_language_from_prefix(request)
    if current_language == 'en-gb':
        untranslated_url = request.path
    else:
        untranslated_url = request.path.replace('/' + current_language, '')
    return {
        'untranslated_url': untranslated_url
    }
