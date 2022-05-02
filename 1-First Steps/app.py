# Import Flask
from flask import Flask, render_template

# Flask need to know if it's been executed
# from a principal file or if it's imported.
app = Flask(__name__)

# Route example -> www.google.com/search
# www.google.com -> Domain
# search -> Route

# http://127.0.0.1:5000/
@app.route("/")
# http://127.0.0.1:5000/home
@app.route("/home")
def index():
    #return "Hola, mundo!"
    #return render_template("index.html")
    name = "Hernan"
    return render_template('index.html', name=name)

@app.route("/iterate")
def iterate():
    a = [1, 2, 3]
    return render_template('iterate.html', param=a)

# http://127.0.0.1:5000/contacto
@app.route("/contact")
def contact():
    #return "<h1>Contact</h1>"
    return render_template("contact.html")

# http://127.0.0.1:5000/hello/<name>
@app.route("/hello/<string:name>")
def hello(name):
    return f"<h1>Hi {name}</h1>"

if __name__ == "__main__":
    # It enables to run the app.py file in the terminal
    # without need to run the Flask server first.
    # Any saved changes will be shown.
    app.run(debug=True)