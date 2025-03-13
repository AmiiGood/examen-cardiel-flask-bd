from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()


class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    nombre_cliente = db.Column(db.String(100))
    direccion_cliente = db.Column(db.String(100))
    telefono_cliente = db.Column(db.String(100))
    total_venta = db.Column(db.Float, default=0.0)
    detalles = db.relationship('DetallePizza', backref='venta')


class DetallePizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'))
    tamano = db.Column(db.String(20))
    cantidad = db.Column(db.Integer, default=1)
    subtotal = db.Column(db.Float)
    ingredientes = db.relationship(
        'IngredientePizza', backref='detalle_pizza')


class IngredientePizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detalle_pizza_id = db.Column(db.Integer, db.ForeignKey('detalle_pizza.id'))
    nombre_ingrediente = db.Column(db.String(50))
