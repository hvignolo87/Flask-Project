from wtforms import Form, StringField, TextAreaField, \
                    EmailField

from wtforms.validators import Length, DataRequired, Email

# Define this class to create the form with Flask
class CommentForm(Form):
    # Equals <input type="text">
    username = StringField('username', 
                            [DataRequired(message='Username is required'),
                             Length(min=4, max=25,
                                    message='Enter a valid username')
                            ])
    email = EmailField('email', 
                        [DataRequired(message='Username is required'),
                         Email(message='Enter a valid email')
                        ])
    comment = TextAreaField('comment')