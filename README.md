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

2. Setup a webhook on GitHub to notify Jenkins of code pushes.

3. In your local project directory, run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <repository-url>
   git push origin master
