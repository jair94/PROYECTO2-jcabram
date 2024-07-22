from flask_restful import Resource
from flask import request, jsonify
from models.ingredientes import Ingredientes
from db import db

class IngredienteController(Resource):
    
    def get(self, id=None):
        if id:
            ingrediente = Ingredientes.query.get_or_404(id)
            return jsonify({
                'id': ingrediente.id,
                'nombre': ingrediente.nombre,
                'precio': ingrediente.precio,
                'calorias': ingrediente.calorias,
                'inventario': ingrediente.inventario,
                'es_vegetariano': ingrediente.es_vegetariano,
                'tipo_id': ingrediente.tipo_id,
                'sabor': ingrediente.sabor
            })
        else:
            ingredientes = Ingredientes.query.all()
            result = []
            for ingrediente in ingredientes:
                result.append({
                    'id': ingrediente.id,
                    'nombre': ingrediente.nombre,
                    'precio': ingrediente.precio,
                    'calorias': ingrediente.calorias,
                    'inventario': ingrediente.inventario,
                    'es_vegetariano': ingrediente.es_vegetariano,
                    'tipo_id': ingrediente.tipo_id,
                    'sabor': ingrediente.sabor
                })
            return jsonify(result)

    def post(self):
        data = request.json
        nuevo_ingrediente = Ingredientes(
            nombre=data['nombre'],
            precio=data['precio'],
            calorias=data['calorias'],
            inventario=data['inventario'],
            es_vegetariano=data['es_vegetariano'],
            tipo_id=data['tipo_id'],
            sabor=data.get('sabor')
        )
        db.session.add(nuevo_ingrediente)
        db.session.commit()
        return jsonify({'message': 'Ingrediente creado con éxito'}), 201

    def put(self, id):
        data = request.json
        ingrediente = Ingredientes.query.get_or_404(id)
        ingrediente.nombre = data['nombre']
        ingrediente.precio = data['precio']
        ingrediente.calorias = data['calorias']
        ingrediente.inventario = data['inventario']
        ingrediente.es_vegetariano = data['es_vegetariano']
        ingrediente.tipo_id = data['tipo_id']
        ingrediente.sabor = data.get('sabor')
        db.session.commit()
        return jsonify({'message': 'Ingrediente actualizado con éxito'})

    def delete(self, id):
        ingrediente = Ingredientes.query.get_or_404(id)
        db.session.delete(ingrediente)
        db.session.commit()
        return jsonify({'message': 'Ingrediente eliminado con éxito'})
