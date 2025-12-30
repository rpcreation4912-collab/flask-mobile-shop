from database import init_db

init_db()
from flask import Flask, render_template, request, redirect
from database import get_db, create_table
import os

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
create_table()

@app.route("/")
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mobiles")
    mobiles = cursor.fetchall()
    conn.close()
    return render_template("index.html", mobiles=mobiles)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        brand = request.form["brand"]
        model = request.form["model"]
        price = request.form["price"]
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mobiles (brand, model, price) VALUES (?, ?, ?)",
            (brand, model, price)
        )
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()
    cursor = conn.cursor()
    if request.method == "POST":
        brand = request.form["brand"]
        model = request.form["model"]
        price = request.form["price"]
        cursor.execute(
            "UPDATE mobiles SET brand=?, model=?, price=? WHERE id=?",
            (brand, model, price, id)
        )
        conn.commit()
        conn.close()
        return redirect("/")
    cursor.execute("SELECT * FROM mobiles WHERE id=?", (id,))
    mobile = cursor.fetchone()
    conn.close()
    return render_template("edit.html", mobile=mobile)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mobiles WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
