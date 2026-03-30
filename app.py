from flask import Flask, render_template, request, redirect
import mysql.connector

# testing my branch copy
app = Flask(__name__)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="Swati",
    password="*******",
    database="edutech"
)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s AND role=%s",
        (username, password, role)
    )

    result = cursor.fetchone()

    if result:
        # Redirect based on role
        if role == "faculty":
            return redirect('/faculty')
        elif role == "student":
            return redirect('/student')
        elif role == "Other":
            return redirect('/Other')
    else:
        return "Invalid Credentials ❌"
    
# Different pages
@app.route('/faculty')
def faculty():
    return render_template('demo.html')

@app.route('/student')
def student():
    return render_template('studentpage.html')

@app.route('/Other')
def other():
    return render_template('demo.html')

app.run(debug=True)
