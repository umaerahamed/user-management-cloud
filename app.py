from flask import Flask, render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Function to get a connection to the database
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection

# Route: View all users (Home Page)
@app.route('/')
def index():
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get all users from the database
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    
    # Close the database connection
    cursor.close()
    conn.close()
    
    # Show the HTML page with the users data
    return render_template('index.html', users=users)

# Route: Add a new user
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    # If the user submits the form
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Insert the new user into the database
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(sql, values)
        
        # Save the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()
        
        # Go back to the home page
        return redirect('/')
    
    # If the user just visits the page, show the form
    return render_template('add_user.html')

# Route: Delete a user
@app.route('/delete/<int:id>')
def delete_user(id):
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Delete the user with the given id
    sql = "DELETE FROM users WHERE id = %s"
    values = (id,)
    cursor.execute(sql, values)
    
    # Save the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    
    # Go back to the home page
    return redirect('/')

# Start the application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
