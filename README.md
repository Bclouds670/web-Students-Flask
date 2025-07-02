![Image](https://github.com/user-attachments/assets/90ac96b4-e4d9-44f6-af0a-e7d6c4f30ed5)
# 🐍 Flask App CI/CD Pipeline with Jenkins & AWS EC2

## 📌 Project Overview

This project demonstrates how to implement a **CI/CD pipeline** to automate the build, test, and deployment of a **Flask web application**. The CI/CD process is managed using **Jenkins**, while the application is deployed to an **AWS EC2 instance** running **MySQL** as the backend database.

### 🔧 Key Features

- **Flask Web Application** with CRUD operations using MySQL
- **CI/CD Pipeline** using Jenkins
- **Automated Deployment** to AWS EC2 via SSH
- **MySQL Integration** for data storage

### 🛠️ Technologies Used

- Python 3 / Flask  
- MySQL Server  
- Jenkins (with SSH Plugin)  
- AWS EC2 (Ubuntu)  
- Git & GitHub  

---

## 🚀 Step 1: Jenkins Setup on Development Server

1. **Install Java & Jenkins**  
   Make sure Java is installed before setting up Jenkins.

2. **Install SSH Plugin in Jenkins**  
   Navigate to:  
   `Manage Jenkins > Manage Plugins > Available Plugins`  
   Search for **SSH Plugin**, install and restart Jenkins.

3. **Add SSH Credentials**  
   Navigate to:  
   `Manage Jenkins > Credentials > System > Global Credentials`  
   - Type: SSH Username with Private Key  
   - Username: your EC2 username  
   - Private Key: paste your private SSH key  

4. **Add SSH Host**  
   Navigate to:  
   `Manage Jenkins > Configure System > SSH Servers`  
   - Hostname: `<Your EC2 Public IP>`  
   - Port: `22`  
   - Username: your EC2 username  
   Save the configuration.

5. **Create Jenkins FreeStyle Projects**  
   - `Flask-Build`  
   - `Flask-Test`  
   - `Flask-Deploy`

---

## 🌐 Step 2: Clone the Repository & Setup GitHub

1. Create a repository on GitHub.

2. Set up a **webhook** in GitHub:  
   Navigate to your repo > Settings > Webhooks > Add webhook  
   - Payload URL: `http://<your-jenkins-ip>:8080/github-webhook/`  
   - Content type: `application/json`  
   - Trigger on: Just the push event

3. Push your project code to GitHub:

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/yourusername/your-repo.git
    git push -u origin master
    ```

---

## ☁️ Step 3: EC2 Instance & MySQL Configuration

### 1. Install Python and MySQL

SSH into your EC2 instance and run:

```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
sudo apt install mysql-server -y

Configure MySQL Database

Login to MySQL:
   mysql -u root -p
   
Create a database:
  CREATE DATABASE student_db;

Update the database credentials in app.py:
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'student_db'

python3 app.py


http://your-live-server-ip:5000


