from flask import Flask, render_template, request
from form import CommentForm

app = Flask(__name__)

# Enable post method
@app.route("/", methods=['GET', 'POST'])
def index():
    # Define the form instance
    comment_form = CommentForm(request.form)
    # If the form is sent, print 
    # the data in the console
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print('An error has ocurred')

    # Page title
    title = 'Forms with Flask'
    return render_template('index.html', 
                           title=title,
                           form=comment_form)

if __name__ == "__main__":
    app.run(debug=True)