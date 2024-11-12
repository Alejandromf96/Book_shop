from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from flask_wtf.file import FileAllowed
from models import User


class RegistrationForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=2, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is alredy taken. Please try another one.')


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class SearchForm(FlaskForm):
    search = StringField('Buscar libros', validators=[DataRequired()])
    submit = SubmitField('Buscar')

# Formulario para añadir un nuevo libro, accesible solo para administradores
class BookForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    price = FloatField('Precio', validators=[DataRequired()])
    image = FileField('Imagen del Libro', validators=[FileAllowed(['jpeg', 'png'])])
    submit = SubmitField('Añadir Libro')