# Techlanders_ecom
e-commerce  website using python(flask framework),css,html,javascript

Flask:

This is a simple Flask application that provides a basic checkout system. Users can visit the checkout page, submit their personal information, and the data will be stored in a PostgreSQL database.

## Features

- **Checkout Form:** Users can fill out a form with their name, phone number, address, country, city, and card number.
- **Database Storage:** Form data is stored in a PostgreSQL database using SQLAlchemy.
- **Static Files:** The application uses static files for CSS, JavaScript, and images.
- **CORS:** Cross-Origin Resource Sharing is enabled to handle requests from different origins.

## Setup

1. **Database Configuration:**
    - Make sure you have PostgreSQL installed.
    - Update the `SQLALCHEMY_DATABASE_URI` in `app.config` to point to your PostgreSQL instance.

2. **Environment Setup:**
    - It's recommended to set up a virtual environment.
    - Install the required packages using `pip install -r requirements.txt`.

3. **Run the Application:**
    - Execute `python app.py` to run the Flask application.
    - Access the application at `http://localhost:5000`.

## Usage

1. Visit the homepage (`/`) to see the index page.
2. Navigate to `/checkout` to access the checkout page.
3. Fill out the checkout form with the required information.
4. Submit the form to store the data in the database.
5. A success page (`/success`) will be displayed upon successful submission.

## Folder Structure

- **templates:** Contains HTML templates for rendering pages.
- **static:** Includes static files such as CSS, JavaScript, and images.
- **app.py:** The main Flask application file.

## Additional Notes

- This is a basic example, and additional features can be added for a more comprehensive checkout system.

Feel free to enhance and customize this application according to your requirements.

required modules:

Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-CORS==4.0.0
psycopg2-binary==2.9.39
