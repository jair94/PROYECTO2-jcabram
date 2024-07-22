from flask import Flask, render_template
from flask_restful import Api
from models.heladeria import Heladeria
from models.producto import Producto
from models.ingredientes import Ingredientes
from models.tipo_ingrediente import TipoIngrediente
from db import db
from controllers.ingredientes_controllers import IngredienteController
from controllers.producto_controllers import ProductoController
from controllers.heladeria_controllers import HeladeriaController
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}/{os.getenv("SCHEMA_DB")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

api.add_resource(HeladeriaController, '/heladeria', '/heladeria/<int:id>')
api.add_resource(ProductoController, '/producto', '/producto/<int:id>')
api.add_resource(IngredienteController, '/ingrediente', '/ingrediente/<int:id>')

@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('heladeria.html', productos=productos)

@app.route('/menu')
def menu():
    productos = Producto.query.all()
    return render_template('menu.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
