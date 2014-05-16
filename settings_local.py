# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.
import os

DEBUG = False

## webserver host and port
# HOST = '0.0.0.0'
# PORT = 5000

SECRET = os.environ.get('SECRET', 'foobar')
SECRET_KEY = os.environ.get('SECRET_KEY', 'my-session-secret')

SQLALCHEMY_DATABASE_URI = 'postgresql://pybossa:tester@localhost/pybossa'
# Heroku
env_database_url = os.environ.get('DATABASE_URL')
if env_database_url:
    SQLALCHEMY_DATABASE_URI = env_database_url.replace('postgres://',
                                                       'postgresql://')
ITSDANGEROUSKEY = os.environ.get('ITSDANGEROUSKEY', 'its-dangerous-key')

## project configuration
BRAND = 'CulturePlex Bossa'
TITLE = 'CulturePlex\'s crowd-sourcing platform'
LOGO = 'default_logo.png'
COPYRIGHT = 'CulturePlex Lab.'
DESCRIPTION = ''
TERMSOFUSE = 'http://okfn.org/terms-of-use/'
DATAUSE = 'http://opendatacommons.org/licenses/by/'
CONTACT_EMAIL = 'admin@cultureplex.ca'
CONTACT_TWITTER = 'cultureplex'

## Default number of apps per page
## APPS_PER_PAGE = 20

## External Auth providers
# TWITTER_CONSUMER_KEY=''
# TWITTER_CONSUMER_SECRET=''
# FACEBOOK_APP_ID=''
# FACEBOOK_APP_SECRET=''
# GOOGLE_CLIENT_ID=''
# GOOGLE_CLIENT_SECRET=''
if ('TWITTER_CONSUMER_KEY' in os.environ
        and 'TWITTER_CONSUMER_SECRET' in os.environ):
    TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
    TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
if ('FACEBOOK_APP_ID' in os.environ
        and 'FACEBOOK_APP_SECRET' in os.environ):
    FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
    FACEBOOK_APP_SECRET = os.environ.get('FACEBOOK_APP_SECRET')
if ('GOOGLE_CLIENT_ID' in os.environ
        and 'GOOGLE_CLIENT_SECRET' in os.environ):
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

## Supported Languages

LOCALES = ['en', 'es', 'fr']

## list of administrator emails to which error emails get sent
# ADMINS = ['me@sysadmin.org']

## CKAN URL for API calls
#CKAN_NAME = "Demo CKAN server"
#CKAN_URL = "http://demo.ckan.org"


## logging config
# Sentry configuration
# SENTRY_DSN=''
## set path to enable
# LOG_FILE = '/path/to/log/file'
## Optional log level
# import logging
# LOG_LEVEL = logging.DEBUG

## Mail setup
MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME', None)
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', None)
MAIL_PORT = os.environ.get('MAIL_PORT', 25)
MAIL_FAIL_SILENTLY = False
MAIL_DEFAULT_SENDER = 'PyBossa Support <info@pybossa.com>'

## Announcement messages
## Use any combination of the next type of messages: root, user, and app owners
## ANNOUNCEMENT = {
##     'admin': 'Root Message',
##     'user': 'User Message',
##     'owner': 'Owner Message',
## }

## Enforce Privacy Mode, by default is disabled
## This config variable will disable all related user pages except for admins
## Stats, top users, leaderboard, etc
ENFORCE_PRIVACY = True


## Cache setup. By default it is enabled
## Redis Sentinel
# List of Sentinel servers (IP, port)
REDIS_CACHE_ENABLED = False
REDIS_SENTINEL = [('localhost', 26379)]
# Heroku
env_sentinel = os.environ.get('REDISCLOUD_URL')
if env_sentinel:
    REDIS_SENTINEL = [env_sentinel.split("://")[1].rsplit(":", 1)]
REDIS_MASTER = 'mymaster'
REDIS_KEYPREFIX = 'pybossa_cache'

## Allowed upload extensions
ALLOWED_EXTENSIONS = ['js', 'css', 'png', 'jpg', 'jpeg', 'gif']

## If you want to use the local uploader configure which folder
UPLOAD_METHOD = 'local'
UPLOAD_FOLDER = 'uploads'

## If you want to use Rackspace for uploads, configure it here
# RACKSPACE_USERNAME = 'username'
# RACKSPACE_API_KEY = 'apikey'
# RACKSPACE_REGION = 'ORD'

## Default number of users shown in the leaderboard
# LEADERBOARD = 20
