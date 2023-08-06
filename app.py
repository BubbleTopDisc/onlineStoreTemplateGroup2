#!/usr/bin/env python3

from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request
from core.session import Sessions

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
db = Database('database/store_records.db')
products = db.get_full_inventory()
sessions = Sessions()
sessions.add_new_session(username, db)


@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    return render_template('index.html', username=username, products=products, sessions=sessions)


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')


@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    try:
        username = request.form['username']
        password = request.form['password']
        if login_pipeline(username, password):
            sessions.add_new_session(username, db)
            return render_template('home.html', products=products, sessions=sessions)
        else:
            print(f"Incorrect username ({username}) or password ({password}).")
            return render_template('index.html')
    except Exception as e:
        print(f"An error occurred: {e}")
    # Jacob Blanton - This handles an exception in the code



@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')


@app.route('/Desktops')
def desktops_page():
    """
    Renders the desktops page when the user is at the `/Desktops` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('desktops.html')


@app.route('/Monitors')
def monitorss_page():
    """
    Renders the monitors page when the user is at the `/Monitors` endpoint.

    args:
        - None

    returns:
        - None
    """
    try:
        return render_template('monitors.html')
    except Exception as e:
        print(f"An error occurred: {e}")
        # Jacob Blanton - Handles an exception here aswell


@app.route('/Laptops')
def laptops_page():
    """
    Renders the desktops page when the user is at the `/Laptops` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('laptops.html')


@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/store_records.db: adds a new user to the database
    """
    try:
        username = request.form['username']
        password = request.form['password']
        if not password:
            raise ValueError('Password is missing')
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        salt, key = hash_password(password)
        update_passwords(username, key, salt)
        db.insert_user(username, key, email, first_name, last_name)
        return render_template('index.html')
    except Exception as e:
        print(e)
        #Daniel Blanton - this test makes sure no incorrect values are entered as well as making sure password is not null


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    order = {}
    user_session = sessions.get_session(username)
    # for item in products:
    #     print(f"item ID: {item['id']}")
    #     if request.form[str(item['id'])] > '0':
    #         count = request.form[str(item['id'])]
    #         order[item['item_name']] = count
    #         user_session.add_new_item(
    #             item['id'], item['item_name'], item['price'], count)
    try:
        order_type = request.form('order_type')
        if order_type == 'desktop':
            if request.form.get('graphics'):
                order['graphics'] = int(request.form['graphics'])
            if request.form.get('cpu'):
                order['cpu'] = int(request.form['cpu'])
            if request.form.get('ram'):
                order['ram'] = int(request.form['ram'])
        elif order_type == 'laptop':
            if request.form.get('graphics'):
                order['graphics'] = int(request.form['graphics'])
            if request.form.get('cpu'):
                order['cpu'] = int(request.form['cpu'])
            if request.form.get('ram'):
                order['ram'] = int(request.form['ram'])
        elif order_type == 'monitor':
            if request.form.get('small'):
                order['small'] = int(request.form['small'])
            if request.form.get('medium'):
                order['medium'] = int(request.form['medium'])
            if request.form.get('large'):
                order['large'] = int(request.form['large'])
    except Exception as e:
        print(e)
        # Daniel Blanton - try and catch tests for incorrect inputs 

    return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost)


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
