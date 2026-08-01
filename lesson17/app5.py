from flask import Flask, render_template

app = Flask(__name__)

# lessona17_task7
gallery = [
    {
        "url": "https://images.pexels.com/photos/210205/pexels-photo-210205.jpeg",
        "caption": "Zachód słońca"
    },
    {
        "url": "https://images.unsplash.com/photo-1500375592092-40eb2168fd21?auto=format&fit=crop&w=800&q=60",
        "caption": "Wzburzona fala"
    }         
]

@app.route('/gallery')
def gallery_page():
    return render_template("gallery.html", images=gallery)

if __name__ == '__main__':
    app.run(debug=True)