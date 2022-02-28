from flask import Flask,render_template,request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("./order.html")

@app.route("/submit",methods=["POST"])
def aaa():
    a=request.form['name']
    b=request.form['item']
    d=request.form['nos']
    dt="db343434"

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SavvyCoderz",
    database='svc'
    )

    c = mydb.cursor()

    adding=("INSERT INTO svc.orders (Name, Item, Nos) VALUES (%s, %s, %s)")
    c.execute(adding,(a,b,d))
    mydb.commit()
    c.execute("SELECT Name, Item, Nos FROM svc.orders")

    res = c.fetchall()

    l=list(res)

    return str(l)

@app.route("/delete")
def dlt():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SavvyCoderz",
    database='svc'
    )

    c = mydb.cursor()

    c.execute("DELETE FROM orders WHERE Dltkey=%s",('*',))
    mydb.commit()
    
    return 'The table is cleared'

@app.route("/showorders")
def aa():
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SavvyCoderz",
    database='svc'
    )

    c = mydb.cursor()

    c.execute("SELECT Name, Item, Nos FROM svc.orders")

    res = c.fetchall()

    l=list(res)

    return str(l)

app.run(debug=True)