from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__, static_url_path='/static', template_folder='templates')

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:king001@localhost:5433/flask'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Initialize Flask-Migrate AFTER creating the db object
migrate = Migrate(app, db)

from sqlalchemy.dialects.postgresql import JSON

class CheckoutData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    cart_data = db.Column(JSON)  # Use the appropriate data type for your database

# Ensuring database operations are within the application context
with app.app_context():
    # Create tables in the database
    db.create_all()

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        country = request.form['country']
        city = request.form['city']
        card_number = request.form['cardNumber']

        # Get cart data
        cart_data = request.form.getlist('listCart[]')

        # Save form data and serialized cart data to the database
        checkout_data = CheckoutData(
            name=name,
            phone=phone,
            address=address,
            country=country,
            city=city,
            card_number=card_number,
            cart_data=cart_data
        )

        db.session.add(checkout_data)
        db.session.commit()

        print(f"Received data: Name={name}, Phone={phone}, Address={address}, Country={country}, City={city}, Card Number={card_number}")
        print(f"Cart data: {cart_data}")

        return jsonify({'status': 'success', 'message': 'Order placed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
