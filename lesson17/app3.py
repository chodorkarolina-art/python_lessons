from flask import Flask, render_template

app = Flask(__name__)

movies = ["Władca pierścieni", "Gwiezdne wojny", "Never let me go"]

# lessona17_task3
@app.route('/movies')
def movies_page():
    return render_template("movies.html", movies=movies)
    
# lessona17_task4
@app.route('/movies2')
def movies_page_v2():
    return render_template(
        "movies_v2.html", 
        movies=movies,
        page_title="Moje ulubione filmy"
        )

if __name__ == '__main__':
    app.run(debug=True)
    
    