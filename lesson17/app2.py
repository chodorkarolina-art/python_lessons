from flask import Flask

app = Flask(__name__)

# lesson17_task2
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"Wynik to : {num1 + num2}"

if __name__ == '__main__':
    app.run(debug=True)