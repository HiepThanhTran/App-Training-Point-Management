"""
Django settings for core project.

Generated by "django-admin startproject" using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

import cloudinary
import pymysql
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(".env.development.local")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app", ".now.sh"]

INTERNAL_IPS = ["127.0.0.1"]

# Application definition

INSTALLED_APPS = [
	# Default
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"django.contrib.postgres",
	# Library & Framework
	"rest_framework",
	"oauth2_provider",
	"corsheaders",
	"drf_yasg",
	"debug_toolbar",
	"django_ckeditor_5",
	# Third-party
	"activities.apps.ActivitiesConfig",
	"interacts.apps.InteractsConfig",
	"schools.apps.SchoolsConfig",
	"users.apps.UsersConfig",
	"commands.apps.CommandsConfig",
]

MIDDLEWARE = [
	"corsheaders.middleware.CorsMiddleware",
	"debug_toolbar.middleware.DebugToolbarMiddleware",
	"django.middleware.security.SecurityMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		"DIRS": ["templates"],
		"APP_DIRS": True,
		"OPTIONS": {
			"context_processors": [
				"django.template.context_processors.debug",
				"django.template.context_processors.request",
				"django.contrib.auth.context_processors.auth",
				"django.contrib.messages.context_processors.messages",
			],
		},
	},
]

WSGI_APPLICATION = "core.wsgi.application"

pymysql.install_as_MySQLdb()

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": os.getenv("POSTGRES_DATABASE"),
		"USER": os.getenv("POSTGRES_USER"),
		"PASSWORD": os.getenv("POSTGRES_PASSWORD"),
		"HOST": os.getenv("POSTGRES_HOST"),
	},
	# "default": {
	# 	"ENGINE": "django.db.backends.mysql",
	# 	"NAME": "training_point_db",
	# 	"USER": "root",
	# 	"PASSWORD": "29012003",
	# 	"HOST": "localhost",
	# },
	# "default": {
	#     "ENGINE": "django.db.backends.sqlite3",
	#     "NAME": BASE_DIR / "db.sqlite3",
	# },
}

AUTH_USER_MODEL = "users.Account"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
	},
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Ho_Chi_Minh"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
	"DEFAULT_AUTHENTICATION_CLASSES": (
		"rest_framework.authentication.SessionAuthentication",
		"oauth2_provider.contrib.rest_framework.OAuth2Authentication",
	),
	"DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

OAUTH2_PROVIDER = {"OAUTH2_BACKEND_CLASS": "oauth2_provider.oauth2_backends.JSONOAuthLibCore"}

# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:5000"
# ]

SWAGGER_SETTINGS = {
	"TAGS_SORTER": "alpha",
	"OPERATIONS_SORTER": "method",
	"DEFAULT_MODEL_RENDERING": "example",
	"DISPLAY_OPERATION_ID": False,
	"VALIDATOR_URL": None,
	"DEFAULT_FIELD_INSPECTORS": [
		"drf_yasg.inspectors.CamelCaseJSONFilter",
		"drf_yasg.inspectors.InlineSerializerInspector",
		"drf_yasg.inspectors.RelatedFieldInspector",
		"drf_yasg.inspectors.ChoiceFieldInspector",
		"drf_yasg.inspectors.FileFieldInspector",
		"drf_yasg.inspectors.DictFieldInspector",
		"drf_yasg.inspectors.SimpleFieldInspector",
		"drf_yasg.inspectors.StringDefaultFieldInspector",
	],
}

DEBUG_TOOLBAR_CONFIG = {
	"UPDATE_ON_FETCH": True,
	"SHOW_COLLAPSED": True,
}

cloudinary.config(
	cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
	api_key=os.getenv("CLOUDINARY_API_KEY"),
	api_secret=os.getenv("CLOUDINARY_API_SECRET"),
	# api_proxy = "http://proxy.server:3128/",
)

customColorPalette = [
	{"color": "hsl(4, 90%, 58%)", "label": "Red"},
	{"color": "hsl(340, 82%, 52%)", "label": "Pink"},
	{"color": "hsl(291, 64%, 42%)", "label": "Purple"},
	{"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
	{"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
	{"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]

# CKEDITOR_5_CUSTOM_CSS = "path_to.css"  # optional
# CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage"  # optional
CKEDITOR_5_CONFIGS = {
	"default": {
		"toolbar": ["heading", "|", "bold", "italic", "link", "bulletedList", "numberedList", "blockQuote", "imageUpload"],
	},
	"extends": {
		"blockToolbar": ["paragraph", "heading1", "heading2", "heading3", "|", "bulletedList", "numberedList", "|", "blockQuote"],
		"toolbar": [
			"heading", "|", "outdent", "indent", "|",
			"bold", "italic", "link", "underline", "strikethrough", "code", "subscript", "superscript", "highlight", "|",
			"codeBlock", "sourceEditing", "insertImage", "bulletedList", "numberedList", "todoList", "|",
			"blockQuote", "imageUpload", "|",
			"fontSize", "fontFamily", "fontColor", "fontBackgroundColor", "mediaEmbed", "removeFormat", "insertTable",
		],
		"image": {
			"toolbar": ["imageTextAlternative", "|", "imageStyle:alignLeft", "imageStyle:alignRight", "imageStyle:alignCenter", "imageStyle:side", "|"],
			"styles": ["full", "side", "alignLeft", "alignRight", "alignCenter"],
		},
		"table": {
			"contentToolbar": ["tableColumn", "tableRow", "mergeTableCells", "tableProperties", "tableCellProperties"],
			"tableProperties": {
				"borderColors": customColorPalette,
				"backgroundColors": customColorPalette,
			},
			"tableCellProperties": {
				"borderColors": customColorPalette,
				"backgroundColors": customColorPalette,
			},
		},
		"heading": {
			"options": [
				{
					"model": "paragraph",
					"title": "Paragraph",
					"class": "ck-heading_paragraph",
				},
				{
					"model": "heading1",
					"view": "h1",
					"title": "Heading 1",
					"class": "ck-heading_heading1",
				},
				{
					"model": "heading2",
					"view": "h2",
					"title": "Heading 2",
					"class": "ck-heading_heading2",
				},
				{
					"model": "heading3",
					"view": "h3",
					"title": "Heading 3",
					"class": "ck-heading_heading3",
				},
			]
		},
	},
	"list": {
		"properties": {
			"styles": "true",
			"startIndex": "true",
			"reversed": "true",
		}
	},
}
