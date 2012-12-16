# Django settings for doommaster project.
import django.conf.global_settings as DEFAULT_SETTINGS
from os import path
here = lambda *x: path.join(path.abspath(path.dirname(__file__)), *x)

PROJECT_DIR = here()
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Venelin Stoykov', 'vkstoykov@gmail.com'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Sofia'
DATETIME_FORMAT = "j F Y, H:i"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'bg'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
STATIC_ROOT = here('static/')
MEDIA_ROOT = here('media/')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


STATICFILES_DIRS = (
    here('pages/static/'),
)


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qi!k%l+n@hs8l8%)t@j2bl6_jj_x2q-g^em=i!6m17(7x1^$9r'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    here('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)


MIDDLEWARE_CLASSES = (
    'middleware.SQLPrintingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    'django.contrib.webdesign',

    'django_extensions',
    'south',
    'tinymce',

    'pages',
    'links',
    'blog',
    'gallery',
    'disqus',
)

INTERNAL_IPS = ('127.0.0.1',)


try:
    from settings_local import *
except ImportError:
    import sys
    sys.exit("\033[1;31mCan not import settings_local\033[0m")


TINYMCE_DEFAULT_CONFIG = {
    'plugins': "autolink,lists,style,table,save,emotions,iespell,inlinepopups,preview,media,searchreplace,contextmenu,paste,directionality,fullscreen,noneditable,xhtmlxtras",

    'theme': "advanced",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,

    'theme_advanced_buttons1': "save,newdocument,|,fullscreen,code,|,search,replace,|,styleselect,formatselect,fontselect,fontsizeselect,|,removeformat,cleanup,help,|,undo,redo,preview",
    'theme_advanced_buttons2': "cut,copy,paste,pastetext,pasteword,|,bold,italic,underline,strikethrough,|,sub,sup,|,justifyleft,justifycenter,justifyright,justifyfull,|,bullist,numlist,|,outdent,indent,blockquote,link,unlink,anchor,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,charmap,emotions,iespell,media,image,|,cite,abbr,acronym,attribs,|,styleprops",
    'theme_advanced_buttons4': "",

    #'content_css': "%scss/style.css" % STATIC_URL,
    'preformatted': True,

}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = True

try:
    import uwsgi
    import uwsgi_admin
except ImportError:
    pass
else:
    INSTALLED_APPS += ('uwsgi_admin',)
