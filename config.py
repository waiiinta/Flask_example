CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# path to DB file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# folder store Migrate-data file
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# MySQL config
MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = ''
# MYSQL_DATABASE_DB = 'accrevocompany'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
