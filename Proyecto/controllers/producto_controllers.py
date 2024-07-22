from flask_restful import Resource
from flask import request, jsonify
from models.producto import Producto
from db import db

class ProductoController(Resource):

    def get(self, id=None):
        if id:
            producto = Producto.query.get_or_404(id)
            return jsonify({
                'id': producto.id,
                'nombre': producto.nombre,
                'precio_publico': producto.precio_publico,
                'tipo_vaso': producto.tipo_vaso,
                'volumen': producto.volumen,
                'heladeria_id': producto.heladeria_id,
                'tipo_producto': producto.tipo_producto
            })
        else:
            productos = Producto.query.all()
            result = []
            for producto in productos:
                result.append({
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio_publico': producto.precio_publico,
                    'tipo_vaso': producto.tipo_vaso,
                    'volumen': producto.volumen,
                    'heladeria_id': producto.heladeria_id,
                    'tipo_producto': producto.tipo_producto
                })
            return jsonify(result)

    def post(self):
        data = request.json
        nuevo_producto = Producto(
            nombre=data['nombre'],
            precio_publico=data['precio_publico'],
            tipo_vaso=data.get('tipo_vaso'),
            volumen=data.get('volumen'),
            heladeria_id=data['heladeria_id'],
            tipo_producto=data['tipo_producto']
        )
        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({'message': 'Producto creado con éxito'}), 201

    def put(self, id):
        data = request.json
        producto = Producto.query.get_or_404(id)
        producto.nombre = data['nombre']
        producto.precio_publico = data['precio_publico']
        producto.tipo_vaso = data.get('tipo_vaso')
        producto.volumen = data.get('volumen')
        producto.heladeria_id = data['heladeria_id']
        producto.tipo_producto = data['tipo_producto']
        db.session.commit()
        return jsonify({'message': 'Producto actualizado con éxito'})

    def delete(self, id):
        producto = Producto.query.get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return jsonify({'message': 'Producto eliminado con éxito'})
