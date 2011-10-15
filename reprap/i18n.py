from translationstring import TranslationStringFactory
from pyramid.i18n import get_localizer
from pyramid.threadlocal import get_current_request

def translator(term, domain='deform'):
    """hooks into pyramid's translation infrastructure to translate `term`"""
    if not hasattr(term, 'interpolate'): # not a translation string
        term = TranslationStringFactory(domain)(term)
    return get_localizer(get_current_request()).translate(term)