from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange


# Форма для инициализации приключения
class InitGameWorldForm(FlaskForm):
    width = IntegerField('Введите ширину', name="Ширина", validators=[NumberRange(min=2, max=15), DataRequired()])
    height = IntegerField('Введите высоту', name="Высота", validators=[NumberRange(min=2, max=15), DataRequired()])
    submit_init = SubmitField('Начать приключение!')


# Форма "шага"
class MoveForm(FlaskForm):
    way = SelectField('Выберите сторону света, в которую желаете отправиться',
                      validators=[NumberRange(min=1), DataRequired()], coerce=int,
                      choices=[(1, "Север"), (2, "Восток"), (3, "Юг"), (4, "Запад")])
    number_steps = IntegerField("Как далеко планируете продвинуться?", validators=[NumberRange(min=1), DataRequired()],
                                default=1, render_kw={"class": "form-control"})
    submit_move = SubmitField("В путь!")
