![Image](https://github.com/user-attachments/assets/90ac96b4-e4d9-44f6-af0a-e7d6c4f30ed5)
# Flask App CI/CD Pipeline Setup with Jenkins and AWS EC2

This guide describes the full setup process for deploying a Flask application using Jenkins on a development server, with deployment to an AWS EC2 instance running MySQL.

---

## Step 1: Install Required Tools on Development Server (Java, Jenkins)

1. **Login to Jenkins**

2. **Install SSH Plugin**  
   Navigate to:  
   `Manage Jenkins > Manage Plugins > Available Plugins`  
   Search for **SSH Plugin**, click **Install**, then **Restart Jenkins**.

3. **Add SSH Credentials**  
   Navigate to:  
   `Manage Jenkins > Credentials > System > Global Credentials`  
   Add new credential of type **SSH Username with Private Key** with your username and private key. Save.

4. **Add SSH Host**  
   Navigate to:  
   `Manage Jenkins > Configure System`  
   Under **SSH Servers**, add a new host with:  
   - **Hostname**: `<Live server IP>`  
   - **Port**: `22`  
   - **Username**: `<your-username>`  
   Save the configuration.

5. **Create Jenkins FreeStyle Projects**  
   Create the following projects:  
   - `Flask-Build`  
   - `Flask-Test`  
   - `Flask-Deploy`

---

## Step 2: Clone the Repository and Set Up GitHub

1. Create a repository on GitHub.

2. Set up a webhook on GitHub to notify Jenkins of code pushes.

3. In your local project directory, run:

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin <repository-url>
    git push origin master
    ```

---

## Step 3: Deployment Steps on AWS EC2

### 1. Install Required System Tools

Run the following commands on your EC2 instance to install Python and MySQL:

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


