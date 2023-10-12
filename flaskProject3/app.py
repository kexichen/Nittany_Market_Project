from _mysql_connector import MySQL
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '336336xx'
app.config['MYSQL_DB'] = 'kexi'

mysql = MySQL(app)


# http://127.0.0.1:5000/login/

@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users_data WHERE email = %s AND password = %s', (email, password,))
        # Fetch one record and return result
        users_data = cursor.fetchone()

        # If account exists in accounts table in out database
        # if users_data:
        #
        #     # Create session data, we can access this data in other routes
        #     session['email'] = users_data['email']
        #     cursor.execute('SELECT * FROM buyers_data WHERE email = %s ', (email,))
        #     buyer_info = cursor.fetchone()
        #     print(buyer_info['home_address_id'])
        #     cursor.execute('SELECT * FROM address_data WHERE address_id = %s ', (buyer_info['home_address_id'],))
        #     home_address = cursor.fetchone()
        #     cursor.execute('SELECT * FROM zipcode_info_data WHERE zipcode = %s',(home_address['zipcode'],))
        #     home_address_more_info = cursor.fetchone()
        #
        #     print(home_address_more_info)
        #     cursor.execute('SELECT * FROM address_data WHERE address_id = %s ', (buyer_info['billing_address_id'],))
        #     billing_address = cursor.fetchone()
        #
        #     cursor.execute('SELECT * FROM zipcode_info_data WHERE zipcode = %s',(billing_address['zipcode'],))
        #     billing_address_more_info = cursor.fetchone()
        #
        #     cursor.execute('SELECT * FROM credit_cards_data WHERE Owner_email = %s ', (buyer_info['email'],))
        #     credit_cards = cursor.fetchone()

        return render_template('home.html')
            # return render_template('userinfo.html', email=users_data['email'], first_name=buyer_info['first_name'],last_name=buyer_info['last_name'],gender=buyer_info['gender'], age=buyer_info['age'], home_address=home_address,home_address_more_info = home_address_more_info, billing_address=billing_address,billing_address_more_info = billing_address_more_info,credit_cards = credit_cards)
            # return 'Logged in successfully!'
    else:
            # Account does not exist or username/password incorrect
            msg = 'Incorrect username/password!'
            render_template('index.html', msg=msg)
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)

@app.route("/home", methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route("/user", methods=["GET"])
def user():
    msg = 'will display user info!'
    # Create session data, we can access this data in other routes
    email = session['email']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM buyers_data WHERE email = %s ', (email,))
    buyer_info = cursor.fetchone()
    print(buyer_info['home_address_id'])
    cursor.execute('SELECT * FROM address_data WHERE address_id = %s ', (buyer_info['home_address_id'],))
    home_address = cursor.fetchone()
    cursor.execute('SELECT * FROM zipcode_info_data WHERE zipcode = %s', (home_address['zipcode'],))
    home_address_more_info = cursor.fetchone()

    print(home_address_more_info)
    cursor.execute('SELECT * FROM address_data WHERE address_id = %s ', (buyer_info['billing_address_id'],))
    billing_address = cursor.fetchone()

    cursor.execute('SELECT * FROM zipcode_info_data WHERE zipcode = %s', (billing_address['zipcode'],))
    billing_address_more_info = cursor.fetchone()

    cursor.execute('SELECT * FROM credit_cards_data WHERE Owner_email = %s ', (buyer_info['email'],))
    credit_cards = cursor.fetchone()
    return render_template('userinfo.html', email=email, first_name=buyer_info['first_name'],
                           last_name=buyer_info['last_name'], gender=buyer_info['gender'], age=buyer_info['age'],
                           home_address=home_address, home_address_more_info=home_address_more_info,
                           billing_address=billing_address, billing_address_more_info=billing_address_more_info,
                           credit_cards=credit_cards)
    # return 'Logged in successfully!'
    # return render_template('userinfo.html', email=msg)

# Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users_data WHERE email = %s AND password = %s', (email, password,))
        # Fetch one record and return result
        users_data = cursor.fetchone()
        # If account exists in accounts table in out database
        if users_data:

            # Create session data, we can access this data in other routes
            session['email'] = users_data['email']
            cursor.execute('SELECT * FROM buyers_data WHERE email = %s ', (email,))
            buyer_info = cursor.fetchone()
            print(buyer_info['home_address_id'])
            cursor.execute('SELECT * FROM address_data WHERE address_id = %s ', (buyer_info['home_address_id'],))
            home_address = cursor.fetchone()
            cursor.execute('SELECT * FROM zipcode_info_data WHERE zipcode = %s',(home_address['zipcode'],))
            home_address_more_info = cursor.fetchone()

            print(home_address_more_info)
            cursor.execute('SELECT * FROM address_data WHERE address_id = %s ', (buyer_info['billing_address_id'],))
            billing_address = cursor.fetchone()

            cursor.execute('SELECT * FROM zipcode_info_data WHERE zipcode = %s',(billing_address['zipcode'],))
            billing_address_more_info = cursor.fetchone()

            cursor.execute('SELECT * FROM credit_cards_data WHERE Owner_email = %s ', (buyer_info['email'],))
            credit_cards = cursor.fetchone()
            return render_template('userinfo.html', email=users_data['email'], first_name=buyer_info['first_name'],last_name=buyer_info['last_name'],gender=buyer_info['gender'], age=buyer_info['age'], home_address=home_address,home_address_more_info = home_address_more_info, billing_address=billing_address,billing_address_more_info = billing_address_more_info,credit_cards = credit_cards)
            # return 'Logged in successfully!'


@app.route("/password", methods=['GET', 'POST'])
def password():
    msg = 'will display user info!'
    if request.method == 'POST' and 'password' in request.form and 'email' in session:
        newpassword = request.form['password']
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # Check if account exists using MySQL
        cursor.execute('UPDATE users_data SET password = %s WHERE email = %s', (newpassword, email,))
        mysql.connection.commit()
        msg = 'password has been changed successfully!'
        return render_template('home.html', msg=msg)
    return render_template('changepassword.html', msg=msg)

@app.route("/categories", methods=['GET', 'POST'])
def categories():
    msg = 'will display user info!'
    connection = cursor = mysql.connection
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    root = {}
    parents = ['Root']
    while True:
        all_children = []
        for parent in parents:
            print(parent)
            cursor.execute('SELECT * FROM categories_data WHERE parent_category = %s ', (parent,))
            child_categores = cursor.fetchall()
            children = []
            for child in child_categores:
                print("--", child['category_name'])
                children.append(child['category_name'])
            root[parent] = children
            # print(parent, root[parent])
            all_children += children
        parents = all_children
        if len(parents) == 0:
            break
    print("finished")
    # print(root)
    return render_template('categories.html', categories=root)

@app.route("/product",methods=['GET', 'POST'])
def product():
    # fname = request.form.get("firstname")
    # lname = request.form.get("lastname")

    category_name = request.args.get('category')
    # print(category_name)
    connection = cursor = mysql.connection
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM product_listing_data WHERE Category = %s', (category_name,))
    products = cursor.fetchall()
    print(products)
    return render_template('product.html', products=products)


@app.route("/publish", methods=['GET', 'POST'])
def publish():

    if request.method == 'POST' and 'title' in request.form :# and 'product_description' in request.form:
        # Create variables for easy access
        title = request.form['title']
        print(title)
        product_name = request.form['product_name']
        print(product_name)

        quantity = request.form['quantity']
        print(quantity)
        product_description = request.form['product_description']
        print(product_description)
        category = request.form['category']
        print(category)
        price = request.form['product-price']
        print(price)
        email = session['email']


        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT MAX(Listing_ID) FROM product_listing_data')
        max_now = cursor.fetchone()
        print(max_now['MAX(Listing_ID)'])
        Listing_ID = int(max_now['MAX(Listing_ID)']) + 1
        cursor.execute('INSERT INTO product_listing_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (email, str(Listing_ID), category, title, product_name, product_description,'$'+str(price),str(quantity)))
        mysql.connection.commit()
        # users_data = cursor.fetchone()
        msg = 'publish new product info success!'
        return render_template('publish.html', email=msg)
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # Check if account exists using MySQL
        # cursor.execute('SELECT * FROM users_data WHERE email = %s AND password = %s', (email, password,))
    else:
        msg = 'publish new product info!'
        return render_template('publish.html',email=msg)
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('INSERT * INTO product_listing_data WHERE email = %s AND password = %s', (email, password,))
    # # Fetch one record and return result
    # users_data = cursor.fetchone()

