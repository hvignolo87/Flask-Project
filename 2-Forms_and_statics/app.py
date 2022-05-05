from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contact", methods=["POST"])
def contact():
    form_name = request.form.get("input_name")
    return render_template("contact.html", name=form_name)

if __name__ == "__main__":
    app.run(debug=True)