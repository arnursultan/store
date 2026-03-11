from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'key'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.shop',
    'apps.cart',
    'apps.orders',
    'apps.reviews',
    'apps.favorites',
    'apps.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'store.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'store',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

JAZZMIN_SETTINGS = {
    "site_title": "Administration panel",
    "site_header": "Library",
    "site_brand": "StoreServer",
    "welcome_sign": "Welcome to the Store Server admin panel",
    "copyright": "Store Server",
    "search_model": ["auth.User", "auth.Group"],
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://t.me/ar_nursultan", "new_window": True},
        {"model": "auth.User"},
    ],
    "show_sidebar": True,
    "changeform_format": "horizontal_tabs",
}

JAZZMIN_UI_TWEAKS = {
    #  Light themes
    # "theme" : "flatly",
    # "theme" : "simplex",
    # "theme" : "cerulean",
    # "theme" : "cosmo",
    # "theme" : "journal",
    # "theme" : "litera",
    # "theme" : "lumen",
    # "theme" : "lux",
    # "theme" : "materia",
    # "theme" : "minty",
    # "theme" : "pulse",
    # "theme" : "sandstone",
    # "theme" : "simplex",
    # "theme" : "sketchy",
    # "theme" : "spacelab",
    # "theme" : "united",
    # "theme" : "yeti",
    #  Dark themes
    # "theme": "darkly",
    # "theme" : "slate",
    # "theme" : "cyborg",
    "theme" : "solar",
    # "theme" : "superhero",
}
