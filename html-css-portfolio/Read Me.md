# Portfolio Website (Flask + MySQL)

This is a personal portfolio website built with Flask and MySQL. It features project listings, a gallery, and contact/about pages.

## Features

- Responsive design with custom CSS
- Projects and gallery images stored in a MySQL database
- Dynamic pages rendered with Jinja2 templates

## Requirements

- Python 3.x
- MySQL Server

## Python Packages

Install the required packages using pip:

```sh
pip install flask pymysql
```

## Database Setup

1. Start your MySQL server.
2. Run the SQL script to create the database and tables, and insert sample data:

   ```sh
   mysql -u root -p < queries_to_setup_db.sql
   ```

   (Enter your MySQL password when prompted.)

## Running the App

1. Set the `FLASK_APP` environment variable (optional for Flask 2.x):

   ```sh
   export FLASK_APP=app.py
   ```

2. Start the Flask development server:

   ```sh
   python app.py
   ```

3. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

- `app.py` — Main Flask application
- `queries_to_setup_db.sql` — SQL script to set up the database
- `static/` — CSS and images
- `templates/` — HTML templates

## Notes

- Update the MySQL credentials in [`app.py`](app.py) if needed.
- For additional sample data, you can use [`insert_data.py`](insert_data.py).