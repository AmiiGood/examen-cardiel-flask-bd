from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SelectMultipleField, widgets
from wtforms import validators


class ClienteForm(FlaskForm):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(
            min=4, max=25, message='El nombre debe tener entre 4 y 25 caracteres')
    ])
    direccion = StringField('Dirección', [
        validators.DataRequired(message='La dirección es requerida'),
        validators.length(
            min=4, max=100, message='La dirección debe tener entre 4 y 100 caracteres')
    ])
    telefono = StringField('Teléfono', [
        validators.DataRequired(message='El teléfono es requerido'),
        validators.length(
            min=7, max=12, message='El teléfono debe tener entre 7 y 12 caracteres')
    ])


class PizzaForm(FlaskForm):
    tamano = RadioField(
        'Tamaño',
        choices=[('pequena', 'Pequeña ($40)'),
                 ('mediana', 'Mediana ($80)'),
                 ('grande', 'Grande ($120)')],
        default='mediana',
        validators=[validators.DataRequired(message='El tamaño es requerido')])

    ingredientes = SelectMultipleField(
        'Ingredientes ($10 cada uno)',
        choices=[
            ('jamon', 'Jamón'),
            ('pina', 'Piña'),
            ('champinones', 'Champiñones')
        ],
        default=['jamon'],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
    )

    numPizzas = IntegerField('Número de pizzas', [
        validators.DataRequired(message='El número de pizzas es requerido'),
        validators.NumberRange(
            min=1, max=100, message='El número de pizzas debe ser entre 1 y 100')
    ], default=1)
