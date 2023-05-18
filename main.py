import datetime
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
# connection =
app.secret_key = 'manii'
UPLOAD_FOLDER = "static/upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def getconnection():
    return mysql.connector.connect(user="root", database="foods")

@app.route("/")
def adminheader():
    return render_template("adminheader.html")


@app.route("/food_details")
def food_details():
    connection = getconnection()
    cur = connection.cursor()
    cur.execute("select * from food_details")
    result = cur.fetchall()
    cur.close()
    return render_template("food_details.html", data=result)

@app.route("/food_detailsSave", methods =["POST","GET"])
def food_detailsSave():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        a = request.form["users_id"]
        b = request.form["food_id"]
        c = request.form["food_type1"]
        d = request.form["food_type2"]
        e = request.form["food_name"]
        f = request.form["food_date"]
        g = request.form["food_time"]
        h = request.form["food_location1"]
        i = request.form["food_location2"]
        j = request.form["food_phono"]
        k = file.filename
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("insert into food_details values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"','"+i+"','"+j+"','"+k+"')")
        connection.commit()
        return redirect(url_for("food_details"))

@app.route("/food_detailsupdate", methods = ["POST","GET"])
def food_detailsupdate():
    if request.method == "POST":
        a = request.form["users_id"]
        b = request.form["food_id"]
        c = request.form["food_type1"]
        d = request.form["food_type2"]
        e = request.form["food_name"]
        f = request.form["food_date"]
        g = request.form["food_time"]
        h = request.form["food_location1"]
        i = request.form["food_location2"]
        j = request.form["food_phono"]
        k = request.form["food_photo"]
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("update food_details set food_id='"+b+"',food_type1='"+c+"',food_type2='"+d+"',food_name='"+e+"',food_date='"+f+"',food_time='"+g+"',food_location1='"+h+"',food_location2='"+i+"',food_phono='"+j+"',food_photo='"+k+"' where users_id='"+a+"'")
        connection.commit()
        return redirect(url_for("food_details"))



@app.route("/food_detailsedit", methods=["POST", "GET"])
def food_detailsedit():
        id = request.args.get("RN")
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("select * from food_details where users_id = '"+id+"'")
        result = cur.fetchall()
        cur.close()
        return render_template("food_detailsedit.html", data =result)





@app.route("/food_detailsdelete", methods = ["POST", "GET"])
def food_detailsdelete():
        id = request.args.get("RN")
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("delete from  food_details where users_id='"+id+"'")
        connection.commit()
        cur.close()
        return redirect(url_for("food_details"))



@app.route("/orders")
def orders():
    connection = getconnection()
    cur = connection.cursor()
    cur.execute("select * from orders")
    result = cur.fetchall()
    cur.close()
    return render_template("orders.html", data=result)




@app.route("/ordersSave", methods =["POST","GET"])
def ordersSave():
    if request.method == "POST":
        a = request.form["order_userid"]
        b = request.form["order_foodid"]
        c = request.form["order_buyerid"]
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("insert into orders values('"+a+"','"+b+"','"+c+"','No',0)")
        connection.commit()
        return redirect(url_for("orders"))

@app.route("/ordersupdate", methods = ["POST","GET"])
def ordersupdate():
    if request.method == "POST":
        a = request.form["order_userid"]
        b = request.form["order_foodid"]
        c = request.form["order_buyerid"]
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("update orders set order_foodid='"+b+"',order_buyerid='"+c+"' where order_userid='"+a+"'")
        connection.commit()
        return redirect(url_for("orders"))



@app.route("/ordersedit", methods=["POST", "GET"])
def ordersedit():
        id = request.args.get("RN")
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("select * from orders where  order_userid='"+id+"'")
        result = cur.fetchall()
        cur.close()
        return render_template("ordersedit.html", data =result)


@app.route("/ordersdelete", methods=["POST", "GET"])
def ordersdelete():
        id = request.args.get("RN")
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("delete from  orders where order_userid='"+id+"'")
        connection.commit()
        cur.close()
        return redirect(url_for("orders"))


@app.route("/users")
def users():
    connection = getconnection()
    cur = connection.cursor()
    cur.execute("select * from users")
    result = cur.fetchall()
    cur.close()
    return render_template("users.html", data=result)


@app.route("/usersupdate", methods = ["POST","GET"])
def usersupdate():
    if request.method == "POST":
        a = request.form["users_photo"]
        b = request.form["users_id"]
        c = request.form["users_name"]
        d = request.form["users_address"]
        e = request.form["users_email"]
        f = request.form["users_password"]
        g = request.form["users_sex"]
        h = request.form["users_phno"]
        i = request.form["users_state"]
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("update users set users_id='"+b+"',users_name='"+c+"',users_address='"+d+"',users_email='"+e+"',users_password='"+f+"',users_sex='"+g+"',users_phno='"+h+"',users_state='"+i+"' where users_photo='"+a+"'")
        connection.commit()
        return redirect(url_for("users"))



@app.route("/usersedit", methods=["POST", "GET"])
def usersedit():
        id = request.args.get("RN")
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("select * from users where  users_photo='"+id+"'")
        result = cur.fetchall()
        cur.close()
        return render_template("usersedit.html", data =result)

@app.route("/usersSave", methods =["POST","GET"])
def usersSave():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        a = file.filename
        b = request.form["users_id"]
        c = request.form["users_name"]
        d = request.form["users_address"]
        e = request.form["users_email"]
        f = request.form["users_password"]
        g = request.form["users_sex"]
        h = request.form["users_phno"]
        i = request.form["users_state"]
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("insert into users values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"','"+i+"')")
        connection.commit()
        return redirect(url_for("users"))


@app.route("/usersdelete", methods =["POST", "GET"])
def usersdelete():
        id = request.args.get("RN")
        connection = getconnection()
        cur = connection.cursor()
        cur.execute("delete from  users where users_photo='"+id+"'")
        connection.commit()
        cur.close()
        return redirect(url_for("users"))


if __name__== "__main__":
    app.run(port=5000 ,debug=True)