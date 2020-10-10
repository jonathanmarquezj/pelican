#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'jonathan'
SITENAME = 'hola mundo 2'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "theme/attila"
#HEADER_COVER = 'static/home.png'
HEADER_COVER = 'https://blog.static.minfive.com/other/banner-bg.jpg'
HEADER_COLOR = 'black'

#COLOR_SCHEME_CSS = 'monokai.css'
#CSS_OVERRIDE = ['css/myblog.css']
JS_OVERRIDE = ['']


# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
