from db import db
from models.producto import Producto
from models.ingredientes import Ingredientes

class Heladeria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    productos = db.relationship('Producto', backref='heladeria', lazy=True)

    def __init__(self):
        self.productos = Producto.query.all()

    def get_productos(self):
        return self.productos

    def vender(self, nombre_producto):
        producto = Producto.query.filter_by(nombre=nombre_producto).first()
        if not producto:
            return "Producto no encontrado"

        try:
            for ingrediente in producto.ingredientes:
                if ingrediente.inventario < 0.2:
                    raise ValueError(f"Nos hemos quedado sin {ingrediente.nombre}")

            for ingrediente in producto.ingredientes:
                ingrediente.inventario -= 0.2

            db.session.commit()
            return "¡Vendido!"

        except ValueError as e:
            return str(e)