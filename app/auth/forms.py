from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Me manter conectado(a)')
    submit = SubmitField('Entrar')


class RegistrationForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Nome de Usuário', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9._ ]*$', 0,
               'Os nomes de usuário devem conter apenas letras, números, pontos ou sublinhados')])
    password = PasswordField('Senha', validators=[
        DataRequired(), EqualTo('password2', message='As senhas devem corresponder.')])
    password2 = PasswordField('Confirme sua senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('E-mail já cadastrado.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Nome de usuário já em uso.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Senha Antiga', validators=[DataRequired()])
    password = PasswordField('Nova Senha', validators=[
        DataRequired(), EqualTo('password2', message='As senhas devem corresponder.')])
    password2 = PasswordField('Confirmar nova senha',
                              validators=[DataRequired()])
    submit = SubmitField('Atualizar Senha')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Redefinir Senha')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Nova Senha', validators=[
        DataRequired(), EqualTo('password2', message='As senhas devem corresponder.')])
    password2 = PasswordField('Confirmar Senha', validators=[DataRequired()])
    submit = SubmitField('Redefinir Senha')


class ChangeEmailForm(FlaskForm):
    email = StringField('Novo E-mail', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Atualizar endereço de e-mail')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('E-mail já cadastrado.')
