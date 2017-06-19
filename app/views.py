from flask import render_template, flash, redirect,request
from flask import session
from flaskext.mysql import MySQL
from flask_session import Session
from app import function
from app import app

# setup MySQL variable
mysql = MySQL()
mysql.init_app(app)


# Homepage and Python example_______________________
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

# GET and POST examples_____________________________
@app.route('/tuna',methods=['GET','POST'])
def mama():
	if request.method == 'POST':
		if 'username' in request.form:
			data = request.form['username']
			return 'this is your user name ' + data
		else:
			return 'this does not have user name'
	else: return 'may be get'

@app.route('/salmon/<name>')
def salmon(name):
	data = request.args.get('data')
	if data is not None:
		return render_template('salmon.html',title='Welcome to salmon',name=name+data)
	else:
		return render_template('salmon.html',title='No get Data',name=name)


# session example __________________________
@app.route('/set',methods=["GET"])
def form():
	session['username'] = 'hello'
	return 'now set'

@app.route('/session')
def set_session():
	username = session['username']
	return username
# ___________________________________________


# passing args with URL which is not GET___________
@app.route('/profile/<username>')
def profile(username):
	return "Hey there %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "<h2>Post ID is %s<h2>" % post_id

# MySQL examples________________________________
@app.route('/select1')
def select1():
	app.config['MYSQL_DATABASE_DB'] = 'accrevocompany'
	conn = mysql.connect()
	cursor = conn.cursor()
	query = ('SELECT * FROM companys')
	cursor.execute(query)

	for row in cursor:
		return str(row[0])
	# return render_template('select1.html',title='select from db')

@app.route('/select2')
def select2():
	app.config['MYSQL_DATABASE_DB'] = 'accrevocompany'
	conn = mysql.connect()
	cursor = conn.cursor()
	query = ('SELECT * FROM companys')
	cursor.execute(query)

	return render_template('select1.html',title='select from db',table=cursor)

# user Function from other file to manage database
@app.route('/select3')
def select3():
	cursor = function.getcompany()

	return render_template('select1.html',title='select from db',table=cursor)
#__________________________________________________

# use Fuction from other file______________________
@app.route('/shout/<name>')
def shout(name):
	return say(name) + function.sayagain(name)

def say(name):
	return "hi %s" %name
#__________________________________________________


if __name__ == '__main__':
	# Secret key for Sessions
	app.secret_key = 'ADFWEF'
	app.run()