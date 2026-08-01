# lesson17_task10
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# konfiguracja bazy danych
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lesson17_app7.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# model Registration
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
# utworzenie bazy
with app.app_context():
    db.create_all()
    
@app.route("/")
def home():
    return redirect(url_for("register"))

@app.route("/register", methods=["GET", "POST"])
def register():
    
    if request.method == "POST":
        
        name = request.form["name"]
        email = request.form["email"]
        
        registration = Registration(
            name=name,
            email=email
        )
        
        db.session.add(registration)
        db.session.commit()
        
        return redirect(url_for("thank_you"))
    
    return render_template("register.html")

@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)