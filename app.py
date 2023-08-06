from flask import Flask, render_template, jsonify
from flaskext.mysql import MySQL
from decimal import Decimal

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'userpass'
app.config['MYSQL_DATABASE_DB'] = 'app_db'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/products')
def get_products():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT id, name, type, price, stock_quantity FROM deli_products')
    products = cursor.fetchall()

    # Fetch column names from cursor.description
    column_names = [desc[0] for desc in cursor.description]

    # Create a list of dictionaries with column names and row data
    products_with_columns = []
    for row in products:
        product_dict = dict(zip(column_names, row))

        # Convert Decimal objects to strings
        for key, value in product_dict.items():
            if isinstance(value, Decimal):
                product_dict[key] = str(value)

        products_with_columns.append(product_dict)

    # Return JSON data with column names
    return jsonify(products_with_columns)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cursor = mysql.get_db().cursor()

    # Check if the product exists
    cursor.execute('SELECT * FROM deli_products WHERE id = %s', (product_id,))
    product = cursor.fetchone()

    if product and product[4] > 0:  # Check if the product exists and is in stock
        cursor.execute('INSERT INTO cart (product_id, quantity) VALUES (%s, 1) ON DUPLICATE KEY UPDATE quantity = quantity + 1', (product_id,))
        cursor.execute('UPDATE deli_products SET stock_quantity = stock_quantity - 1 WHERE id = %s', (product_id,))
        mysql.get_db().commit()
        return jsonify({'message': 'Product added to cart.'})
    elif product and product[4] <= 0:
        return jsonify({'message': 'Product out of stock.'}), 400
    else:
        return jsonify({'message': 'Product not found.'}), 404

@app.route('/cart')
def get_cart():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT deli_products.name, cart.quantity FROM deli_products INNER JOIN cart ON deli_products.id = cart.product_id')
    cart_items = cursor.fetchall()
    # Fetch column names from cursor.description
    column_names = [desc[0] for desc in cursor.description]
    # Create a list of dictionaries with column names and row data
    cart_with_columns = []
    for row in cart_items:
        cart_dict = dict(zip(column_names, row))

        # Convert Decimal objects to strings
        for key, value in cart_dict.items():
            if isinstance(value, Decimal):
                cart_dict[key] = str(value)

        cart_with_columns.append(cart_dict)

    # Return JSON data with column names
    return jsonify(cart_with_columns)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

