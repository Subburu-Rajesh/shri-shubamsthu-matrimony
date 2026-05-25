from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

# CREATE FLASK APP

app = Flask(__name__)

# =========================
# MYSQL CONFIGURATION
# =========================

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'

# ENTER YOUR MYSQL PASSWORD
app.config['MYSQL_PASSWORD'] = 'Rajesh@960'

app.config['MYSQL_DB'] = 'matrimony'

# MYSQL CONNECTION

mysql = MySQL(app)

# =========================
# HOME PAGE
# =========================
@app.route('/')
def home():
    return render_template('index.html')

# =========================
# REGISTER PAGE
# =========================

@app.route('/register')
def register():
    return render_template('register.html')

# =========================
# SAVE FORM DATA
# =========================

@app.route('/save', methods=['POST'])
def save():

    # GET FORM VALUES

    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    district = request.form['district']
    education = request.form['education']
    phone = request.form['phone']

    # INSERT INTO DATABASE

    cur = mysql.connection.cursor()

    cur.execute("""
        INSERT INTO profiles
        (name, age, gender, district, education, phone)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, age, gender, district, education, phone))

    mysql.connection.commit()

    cur.close()

    # REDIRECT TO PROFILES PAGE

    return redirect('/profiles')

# =========================
# DISPLAY PROFILES
# =========================

@app.route('/profiles')
def profiles():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM profiles")

    data = cur.fetchall()

    cur.close()

    return render_template('profiles.html', profiles=data)

# =========================
# RUN SERVER
# =========================

if __name__ == '__main__':
    app.run(debug=True)