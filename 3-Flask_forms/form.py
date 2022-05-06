from wtforms import Form, StringField, TextAreaField, \
                    EmailField, HiddenField

from wtforms.validators import Length, DataRequired, \
                               Email, ValidationError


# Define a custom validation
def length_honeypot(form, field):
    if len(field.data) > 0:
        raise ValidationError('This field must be empty')
    return None

# Define this class to create the form with Flask
class CommentForm(Form):
    # Equals <input type="text">
    username = StringField('username', 
                            # Data validation
                            [DataRequired(message='Username is required'),
                             Length(min=4, max=25,
                                    message='Enter a valid username')
                            ])
    
    email = EmailField('email', 
                        # Data validation
                        [DataRequired(message='Username is required'),
                         Email(message='Enter a valid email')
                        ])
    
    comment = TextAreaField('comment')

    # Hidden field with custom validation function
    honeypot = HiddenField('', [length_honeypot])