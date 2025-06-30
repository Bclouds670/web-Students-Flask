from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'raj',
    'password': 'Pass@123',
    'database': 'studentsdb'
}

# Home page: Registration form
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        address = request.form['address']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO students (name, email, phone, course, address) VALUES (%s, %s, %s, %s, %s)',
            (name, email, phone, course, address)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return 'Student Registered Successfully!'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
