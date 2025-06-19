from flask import Flask, render_template
import pymysql.cursors

app = Flask(__name__)

# Connect to MySQL database
def get_db_connection():
    connection = pymysql.connect(
        host='127.0.0.1',    # e.g., 'localhost' or '127.0.0.1'
        user='root',    # your MySQL username
        password='root',  # your MySQL password
        database='portfolio',   # your database name
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Define the route for the homepage
@app.route('/')
def index():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM projects ORDER BY created_at DESC LIMIT 3')  # Fetch recent 3 projects
        projects = cursor.fetchall()
    connection.close()
    return render_template('index.html', projects=projects)

# Define the route for the projects page
@app.route('/projects')
def projects():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM projects ORDER BY created_at DESC')  # Fetch all projects ordered by creation date
        projects = cursor.fetchall()
    connection.close()
    return render_template('projects.html', projects=projects)

# Define the route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Define the route for the gallery page
@app.route('/gallery')
def gallery():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM gallery')
        gallery_images = cursor.fetchall()
    connection.close()
    return render_template('gallery.html', gallery_images=gallery_images)

# Define the route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
