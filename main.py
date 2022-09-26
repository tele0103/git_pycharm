from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>Hello world!</h1>"


@app.route('/kontakt/<name>')
def contact(name):
    return "<h2>Ich bin ein Kontaktfomular für " + name + "</h2>"


app.run(debug=True, port=9999)
