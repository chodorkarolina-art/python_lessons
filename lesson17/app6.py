from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# lessona17_task8

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"<Product id={self.id}, name='{self.name}', price={self.price}>"

@app.route("/")
def home():
    return render_template("index.html")

# lessona17_task9
@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)