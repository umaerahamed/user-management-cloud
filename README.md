Yes. Since Jenkins and AWS deployment are now part of the project, I would replace the old README with this **complete updated version**.

You can copy-paste this directly into `README.md`.

````markdown
# Simple User Management Application

## 1. What the project does

This is a simple web application that allows users to:

- View all users
- Add a new user
- Delete an existing user

The application is built with Flask and MySQL and is containerized using Docker.

It is deployed on an AWS EC2 Ubuntu server using Docker Compose.

A Jenkins CI/CD pipeline is also configured to automate the deployment process.

---

## 2. Technologies used

- **Python**: Main programming language.
- **Flask**: Web framework used to build the application.
- **MySQL**: Database used to store user information.
- **HTML & CSS**: Used to create and style the web pages.
- **mysql-connector-python**: Connects the Flask application to MySQL.
- **python-dotenv**: Used for environment-based configuration.
- **Docker**: Containerizes the application.
- **Docker Compose**: Runs the Flask application and MySQL database together.
- **Git**: Version control.
- **GitHub**: Stores the project source code.
- **AWS EC2**: Cloud server used to deploy the application.
- **Ubuntu Linux**: Operating system running on the EC2 server.
- **Jenkins**: Used for CI/CD and automated deployment.
- **SSH**: Used by Jenkins to securely connect to the EC2 server.

---

## 3. Project architecture

The project follows this deployment flow:

```text
Developer
    |
    v
GitHub
    |
    v
Jenkins
    |
    | SSH
    v
AWS EC2
    |
    v
Docker Compose
    |
    +----------------------+
    |                      |
    v                      v
Flask Container       MySQL Container
    |                      |
    +----------+-----------+
               |
               v
          User Data
````

### How the deployment works

1. The project source code is stored in GitHub.
2. Jenkins connects to the AWS EC2 server using SSH.
3. Jenkins pulls the latest code from GitHub.
4. Jenkins builds the Docker image.
5. Docker Compose starts/recreates the application container.
6. The Flask application communicates with the MySQL container.
7. Users access the application through the EC2 public IP.

---

## 4. Application features

### View users

The home page displays all users stored in the MySQL database.

### Add user

A user can enter:

* Name
* Email

The information is stored in the MySQL database.

### Delete user

An existing user can be deleted from the database.

---

## 5. Project structure

```text
user-management/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── init_db.sql
├── .gitignore
├── .env
│
├── templates/
│   ├── index.html
│   └── add_user.html
│
└── static/
    └── style.css
```

### Important files

**app.py**

Contains the Flask application and routes.

**requirements.txt**

Contains the Python packages required by the application.

**Dockerfile**

Contains the instructions for building the Flask Docker image.

**docker-compose.yml**

Defines the Flask application and MySQL services.

**init_db.sql**

Creates the database and users table.

**.env**

Contains database configuration such as the MySQL password.

The `.env` file should not be committed to GitHub.

**.gitignore**

Prevents files such as `.env`, `venv`, and Python cache files from being committed.

---

# 6. MySQL database

The application uses a database named:

```text
user_management
```

The main table is:

```text
users
```

The table contains:

```text
id
name
email
```

The `id` is automatically generated using `AUTO_INCREMENT`.

---

# 7. Run the project locally without Docker

## Step 1 — Open the project folder

Open PowerShell or Command Prompt and go to the project folder:

```powershell
cd "D:\New folder (2)\cloud project\user-management"
```

---

## Step 2 — Create a Python virtual environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3 — Install requirements

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

---

## Step 4 — Configure the database

Create/update the `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_MYSQL_PASSWORD
DB_NAME=user_management
```

Make sure MySQL is running on your computer.

---

## Step 5 — Create the database

Run the SQL commands from `init_db.sql`.

```sql
CREATE DATABASE IF NOT EXISTS user_management;

USE user_management;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```

---

## Step 6 — Start Flask

Run:

```bash
python app.py
```

The application will start on port:

```text
5000
```

---

## Step 7 — Open the local application

Open:

```text
http://localhost:5000
```

or:

```text
http://127.0.0.1:5000
```

### Important

`localhost` and `127.0.0.1` refer to the computer where the application is currently running.

They are for **local development only**.

---

# 8. Run the project using Docker Compose

Docker Compose allows the Flask application and MySQL database to run together as separate containers.

## Step 1 — Open the project folder

```powershell
cd "D:\New folder (2)\cloud project\user-management"
```

---

## Step 2 — Start the containers

```powershell
docker compose up -d
```

---

## Step 3 — Check the containers

```powershell
docker compose ps
```

You should see both services running:

```text
user-management-app
user-management-db
```

---

## Step 4 — Open the application

```text
http://localhost:5000
```

---

## Stop the application

```bash
docker compose down
```

---

# 9. AWS EC2 deployment

The application is deployed on an AWS EC2 Ubuntu server.

The EC2 server runs:

* Ubuntu Linux
* Docker
* Docker Compose
* Flask container
* MySQL container

---

## EC2 application URL

The current deployed application can be accessed at:

```text
http://16.171.200.199:5000
```

> Note: The EC2 public IP can change if the instance is stopped and started unless an Elastic IP is used. If the IP changes, replace it with the new EC2 public IP.

---

# 10. Manual deployment on EC2

Connect to the EC2 server using SSH:

```bash
ssh -i "user-management-serv.pem" ubuntu@16.171.200.199
```

Go to the project:

```bash
cd ~/user-management-cloud
```

Pull the latest code:

```bash
git pull origin main
```

Build and start the application:

```bash
docker compose up -d --build
```

Check the containers:

```bash
docker compose ps
```

---

# 11. Jenkins CI/CD

Jenkins is used to automate the deployment process.

Jenkins is running on the Windows development machine.

The application itself runs on AWS EC2.

Jenkins connects to EC2 using SSH.

### CI/CD flow

```text
GitHub
   |
   v
Jenkins
   |
   | SSH
   v
AWS EC2
   |
   v
git pull
   |
   v
docker compose up -d --build
   |
   v
Flask + MySQL
```

---

## What Jenkins does

When the Jenkins pipeline is executed:

### 1. Connects to EC2

Jenkins uses an SSH private key to connect to the Ubuntu EC2 server.

### 2. Pulls the latest code

```bash
git pull origin main
```

### 3. Builds the Docker image

```bash
docker compose up -d --build
```

### 4. Starts the containers

Docker Compose starts:

```text
Flask container
MySQL container
```

### 5. Verifies the deployment

Jenkins runs:

```bash
docker compose ps
```

to check that the containers are running.

---

# 12. Jenkins pipeline

The current Jenkins pipeline performs the following:

```text
Deploy to EC2
        |
        v
SSH into EC2
        |
        v
git pull origin main
        |
        v
docker compose up -d --build
        |
        v
docker compose ps
        |
        v
Deployment successful
```

---

# 13. AWS Security Group

The EC2 Security Group controls network access to the server.

The project uses:

| Port | Purpose                             |
| ---- | ----------------------------------- |
| 22   | SSH                                 |
| 5000 | Flask application                   |
| 3306 | MySQL internal Docker communication |

Port `3306` is not publicly exposed.

The Flask container communicates with MySQL through the Docker Compose network.

---

# 14. Docker Compose networking

The Flask application connects to MySQL using:

```text
DB_HOST=db
```

`db` is the name of the MySQL service in `docker-compose.yml`.

Docker Compose creates a network where services can communicate using their service names.

Therefore:

```text
Flask container
      |
      | DB_HOST=db
      v
MySQL container
```

The application does not need to connect to MySQL using the EC2 public IP.

---

# 15. Useful Docker commands

Check running containers:

```bash
docker ps
```

Check all containers:

```bash
docker ps -a
```

Check Compose services:

```bash
docker compose ps
```

Start the application:

```bash
docker compose up -d
```

Start and rebuild:

```bash
docker compose up -d --build
```

Stop the application:

```bash
docker compose down
```

View application logs:

```bash
docker compose logs web
```

View MySQL logs:

```bash
docker compose logs db
```

View all logs:

```bash
docker compose logs
```

---

# 16. Troubleshooting

## Problem 1 — MySQL was killed because of memory pressure

The EC2 instance had approximately 1 GB of RAM.

While running Flask and MySQL, the MySQL process was terminated.

I checked memory using:

```bash
free -h
```

Then checked the kernel logs:

```bash
sudo dmesg | tail -30
```

The logs showed an OOM kill of `mysqld`.

The issue was caused by limited memory on the EC2 instance.

I restarted the Docker Compose services and evaluated the instance sizing rather than adding more workloads to the same small instance.

---

## Problem 2 — MySQL table did not exist

The Flask application initially returned:

```text
Table 'user_management.users' doesn't exist
```

The MySQL container itself was running, but the required `users` table had not been initialized.

I checked the application logs:

```bash
docker compose logs web
```

The solution was to mount `init_db.sql` into the MySQL initialization directory and recreate the Docker Compose volumes so that MySQL could initialize the database table.

---

## Problem 3 — Jenkins could not connect to EC2

Jenkins initially received an SSH connection timeout.

I tested connectivity from Windows using:

```powershell
Test-NetConnection 16.171.200.199 -Port 22
```

The EC2 Security Group had an SSH rule that did not match my current public IP.

I updated the Security Group SSH rule and tested the connection again.

After that:

```text
TcpTestSucceeded : True
```

Jenkins was able to connect.

---

## Problem 4 — Jenkins rejected the SSH private key

Jenkins initially showed:

```text
UNPROTECTED PRIVATE KEY FILE
```

Windows OpenSSH was rejecting the temporary private key because its permissions were too broad.

Jenkins was running as the Windows `LocalSystem` account.

I fixed the permissions using:

```powershell
icacls "%SSH_KEY%" /inheritance:r
icacls "%SSH_KEY%" /grant:r "SYSTEM:R"
```

After that, Jenkins successfully connected to EC2.

---

# 17. Important project commands

### Local

```bash
python app.py
```

### Docker

```bash
docker compose up -d
docker compose ps
docker compose down
```

### Deployment

```bash
git pull origin main
docker compose up -d --build
```

### Troubleshooting

```bash
docker compose logs
free -h
sudo dmesg | tail -30
```

---

# 18. Project outcome

The application was successfully:

* Developed using Flask and MySQL
* Containerized using Docker
* Configured using Docker Compose
* Stored in GitHub
* Deployed on AWS EC2
* Connected to MySQL through Docker networking
* Automated using Jenkins
* Deployed through an SSH-based CI/CD pipeline
* Tested and successfully accessed through the EC2 public IP

---

# 19. Application URLs

### Local development

```text
http://localhost:5000
```

### AWS EC2 deployment

```text
http://16.171.200.199:5000
```

---

# 20. Simple project explanation

This project is a simple Flask and MySQL user management application.

I containerized the Flask application and MySQL database using Docker and Docker Compose. I stored the source code in GitHub and deployed the application on an Ubuntu AWS EC2 instance.

For CI/CD, I configured Jenkins on Windows. Jenkins connects to EC2 using SSH, pulls the latest code from GitHub, rebuilds the Docker image, starts the Docker Compose services, and verifies that the containers are running.

During the project, I also handled real deployment issues such as a MySQL OOM kill caused by limited EC2 memory, a missing MySQL table, an EC2 Security Group SSH problem, and Windows SSH private-key permission issues.

````

### One correction I strongly recommend

In your GitHub README, **don't put your actual `.env` password** anywhere. Your `.gitignore` already excludes `.env`, which is good.

Also, your current EC2 URL:

```text
http://16.171.200.199:5000
````

is the correct deployed URL **right now**. If the EC2 public IP changes later, update that line.
