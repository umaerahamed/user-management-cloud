# Simple User Management Application

## 1. What the project does
This is a very simple web application that allows you to manage users. You can view a list of all users, add a new user, and delete existing users. It is explicitly designed to be beginner-friendly with no overly complex concepts.

## 2. Technologies used
- **Python**: The main programming language.
- **Flask**: A simple web framework for Python.
- **MySQL**: The database used to store user information.
- **HTML & CSS**: Used to structure and style the web pages.
- **mysql-connector-python**: A library to connect Python to MySQL.
- **python-dotenv**: A library to load configuration from a `.env` file.

## 3. How to create the MySQL database and table
1. Open your MySQL client (like MySQL Workbench, phpMyAdmin, or command line).
2. Run the SQL commands found in the `init_db.sql` file in this project:

```sql
CREATE DATABASE user_management;
USE user_management;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```

## 4. How to create the Python virtual environment
Open your terminal (or command prompt) and run:
```bash
# On Windows
python -m venv venv

# On Mac/Linux
python3 -m venv venv
```

Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

## 5. How to install requirements
With your virtual environment activated, install the required packages by running:
```bash
pip install -r requirements.txt
```

## 6. How to configure the .env file
1. You will see a file named `.env` in the project folder.
2. Open it and update `DB_PASSWORD` with your actual MySQL password.
3. If your MySQL server is not running on `localhost` or uses a different user than `root`, update those as well.

## 7. How to run the Flask application
In your terminal, with the virtual environment activated, run:
```bash
python app.py
```

## 8. The URL to open in the browser
Once the application is running, open your web browser and go to:
http://127.0.0.1:5000/
