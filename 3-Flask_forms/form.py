from wtforms import Form, StringField, TextAreaField, EmailField

class CommentForm(Form):
    username = StringField('username')
    email = EmailField('email')
    comment = TextAreaField('comment')