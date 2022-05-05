from flask import Flask, render_template
from form import CommentForm

app = Flask(__name__)

@app.route("/")
def index():
    comment_form = CommentForm()
    title = 'Forms with Flask'
    return render_template('index.html', 
                           title=title,
                           form=comment_form)

if __name__ == "__main__":
    app.run(debug=True)