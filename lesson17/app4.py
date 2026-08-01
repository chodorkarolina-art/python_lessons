from flask import Flask, render_template

app = Flask(__name__)

# lessona17_task6
book = {
    'title': 'Hobbit', 
    'author': 'J.R.R. Tolkien', 
    'year': 1937
}

@app.route('/book')
def book_page():
    return render_template("book.html", book=book)

if __name__ == '__main__':
    app.run(debug=True)
    
    
