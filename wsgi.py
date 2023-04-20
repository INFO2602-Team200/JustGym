import click, pytest, sys
from flask import Flask, render_template
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app,login_manager
from App.controllers import ( create_user, get_all_users_json, get_all_users,add_exercise, add_workout)
from datetime import date

import json

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)
login_manager.init_app(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass',"bob@mail.com",date(1990, 5, 12), 170, 110 ,"Male")
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("email", default="rob@mail.com")
@click.argument("dateOfBirth", default= date(1990, 5, 12))
@click.argument("height", default=160)
@click.argument("weight", default=120)
@click.argument("sex", default="Male")
@click.argument("data", default=None)
@click.argument("preferences", default=None)

def create_user_command(username, password,email,dateOfBirth,height,weight,sex):
    create_user(username, password, email,dateOfBirth,height,weight,sex)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/categories', methods=['GET'])
def categories():
    return render_template('categories_page.html')


@app.route('/settings', methods=['GET'])
def settings():
    return render_template('settings.html')

@app.route('/logout', methods=['GET'])
def logout():
    return render_template('settings.html')


@app.route('/test', methods = ['GET'])
def test():
    file = open('App/exercises.json')
    data = json.load(file)

    for i in data:
        print(i)
        print('NO')

    return render_template('test_home.html', data = data)


@app.route('/test1', methods = ['GET'])
def test1():
    file = open('App/exercises.json')
    data = json.load(file)


    return render_template('test_exercises.html', data = data)
    
