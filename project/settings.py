# Django settings for ischool_user_manager project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('iSchool Zambia', 'support@ischool.zm')
)

MANAGERS = ADMINS

import os

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(os.path.dirname(__file__), 'default.db'),
		'HOST': '',
		'USER': '',
		'PASSWORD': '',
		'PORT': '',
	},
	'other': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(os.path.dirname(__file__), 'other.db'),
		'HOST': '',
		'USER': '',
		'PASSWORD': '',
		'PORT': '',
	},
}

class SchoolDatabaseRouter(object):
    """A router which directs database queries to either the
    license or the school database, depending on the model (table)."""

    def db_for_read(self, model, **hints):
    	# print "read database for %s is %s" % (model, model._meta.db_tablespace)
    	from django.contrib.auth.models import Permission
    	# if model == Permission:
    	#	import pdb; pdb.set_trace()
    	return model._meta.db_tablespace or 'default'

    def db_for_write(self, model, **hints):
    	# print "write database for %s is %s" % (model, model._meta.db_tablespace)
    	return model._meta.db_tablespace or 'default'

    def allow_relation(self, obj1, obj2, **hints):
    	# return (obj1._meta.db_tablespace == obj2._meta.db_tablespace)
    	return True

    def allow_syncdb(self, db, model):
    	# We must allow MigrationHistory to sync in all databases:
    	# https://groups.google.com/forum/?fromgroups=#!topic/south-users/Sre6bO9aJzo
    	from south.models import MigrationHistory
    	if False and model == MigrationHistory:
    		allowed = True
    	else:
			if model._meta.db_tablespace:
				tablespace = model._meta.db_tablespace
			else:
				tablespace = 'default'

			allowed = (db == tablespace)
		
    	# print "allow syncdb for %s in %s: %s" % (model, db, allowed)
    	return allowed

DATABASE_ROUTERS = [SchoolDatabaseRouter()]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Lusaka'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-scouse'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
import os
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = "hello"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'demo',
]

# AUTH_USER_MODEL = 'users.IschoolUser'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# The name of the class to use to run the test suite
# TEST_RUNNER = 'intranet_binder.testing.SmartTestSuiteRunner'

# MONKEY_PATCHES = ['intranet_binder.monkeypatches']

# Store passwords in SHA1 so that we can share them with PHP,
# which doesn't support PBKDF2 yet (or not in the version we have
# available on the server, anyway).
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# AUTHENTICATION_BACKENDS = ('users.auth.IschoolUserBackend',)

# tasks.py expects to find local_settings.py so the database stuff is there
# from local_settings import *

if False and DEBUG:
	MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
	INTERNAL_IPS = ('127.0.0.1',)
	INSTALLED_APPS += ('debug_toolbar',)

