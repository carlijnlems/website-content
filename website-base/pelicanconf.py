#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = u'WebteamDIAG'
SITENAME = u'DIAG Base'
SITENAME_SHORT = 'DIAG'
SITE_REPO = 'website-base'
SITE_GROUP = 'base'

# Home page and social settings
SITELEAD = 'Some introduction text that is placed on the home page.'
SITE_PICTURE = 'images/social/missing_picture_social.png'
HOME_IMAGE = 'images/general/ApplicationsOfDeepLearning.png'
HOME_IMAGE_CAPTION = 'Automated tumor detection'
NUM_NEWS_HOME_PAGE = 4
TWITTER_URL = 'https://twitter.com/diagnijmegen?ref_src=twsrc%5Etfw'
FOOTER_TEXT = 'Some footer text'
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="http://www.radboudimaging.nl">Radboud Imaging</a>'
FOOTER_IMAGE = 'umc_logo.png'

# What sections to show in the nav bar
NAV_SECTIONS = [
    {"name": "News", "url": "news", "icon": "megaphone"},
    {"name": "Members", "url": "members", "icon": "users"},
    {"name": "Projects", "url": "projects", "icon": "folder"},
    {"name": "Vacancies", "url": "vacancies"},
    {"name": "Publications", "url": "publications", "icon": "file-text-o", "hidden": 85},
    {"name": "Presentations", "url": "presentations", "hidden": 95},
    {"name": "Thesis Gallery", "url": "thesis-gallery", "icon": "book", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon": "envelope-o", "hidden": 60},
]

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True

# What sections to show on homepage (current options that you customizable: {section_name: custom_name})
HOME_SECTIONS = {"News": 'News', "Vacancies": "Vacancies", "Projects": "Projects", "Members": 'Members'}

# URLs
SITEURL = ''
IMGURL = SITEURL
EDIT_CONTENT_URL = 'https://github.com/diagnijmegen/website-content/edit/master/{file_path}'

#
# Non-content variables
# In general these values do not have to be changed.
#
PATH = 'content'
RELATIVE_URLS = False

TIMEZONE = 'Europe/Amsterdam'
DEFAULT_LANG = 'EN'
ARTICLE_TRANSLATION_ID = None
PAGE_TRANSLATION_ID = None

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CURRENTYEAR = date.today().year
TODAY = date.today()
LINKS = ()
DEFAULT_PAGINATION = 10

# URL settings
BIBKEYS_SRC = 'content/dict_pubs.json'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'news/{slug}/'
ARTICLE_SAVE_AS = 'news/{slug}/index.html'
ARTICLE_TYPE = 'News'

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

SITEMAP_SAVE_AS = 'sitemap.xml'
INDEX_SAVE_AS = 'news/index.html'

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ['index', 'archives', 'sitemap']

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ["bibtex", "grouputil", "bibtex_loader", "edit_url", "hierarchy", "fileutil", "bootstrapify", "imgutil", "inline_extend", "content_aggregator"]
