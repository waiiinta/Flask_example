# need to Import Individualy
from flask import render_template, flash, redirect,request
from flask import session
from flaskext.mysql import MySQL
from flask_session import Session
from app import function
from app import app

mysql = MySQL()
mysql.init_app(app)

def sayagain(name):
	return 'hello hello %s' %name

def getcompany():
	app.config['MYSQL_DATABASE_DB'] = 'accrevocompany'
	conn = mysql.connect()
	cursor = conn.cursor()
	query = ('SELECT * FROM companys')
	cursor.execute(query)
	return cursor