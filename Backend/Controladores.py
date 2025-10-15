from ModeloUsuario import modelUsuarios
from ModeloProducto import modelProductos
from flask_login import LoginManager
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

CORS(app)

usuarios = modelUsuarios()
productos = modelProductos()

@app.route('/login', methods = ['POST'])
def loginUsuario():
    data = request.get_json()
    email = data.get('email')
    password = data.get('clave')
    resultado = usuarios.verificar_usuario(email, password)
    return jsonify({"mensaje": resultado })

# rutas usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios.obtener_usuarios())

@app.route('/usuario/<int:id>', methods=['GET'])
def listar_usuario(id):
    return jsonify(usuarios.obtener_usuario(id))

@app.route('/nuevo_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    clave = data.get('clave')
    usuarios.insertar_usuario(nombre, email, clave)
    return jsonify({"mensaje:": "usuario reguistrado con exito"})

@app.route('/actualizar_usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    clave = data.get('clave')
    if nombre is None and email is None and clave is None:
        return jsonify({"error": "campos imcompletos para actualizacion"}), 400
    
    usuario_existente = usuarios.obtener_usuario(id)

    if usuario_existente:
        usuarios.actualizar_usuario(id, nombre, email, clave)
        return jsonify({"mensaje": "usuario actualizado con exito"})
    else:
        return jsonify({"mansaje": "el usuario no existe"}), 400

@app.route('/eliminar_usuario/<int:id>', methods= ['DELETE'])
def elimarUsurio(id):
    if usuarios.obtener_usuario(id):
        usuarios.eliminar_usuarios(id)
        return jsonify({"mensaje": "usuario elminado con exito"})
    else:
        return jsonify({"mensaje": "este usuario no existe"}), 400
    
# rutas produstos
@app.route('/productos', methods=['GET'])
def listar_productos():
    return jsonify(productos.obtener_productos())

@app.route('/producto/<int:id>', methods=['GET'])
def listar_producto(id):
    return jsonify(productos.obtener_producto(id))

@app.route('/nuevo_producto', methods=['POST'])
def nuevo_producto():
    data = request.get_json()
    nombre_producto = data.get('nombre_producto')
    precio = data.get('precio')
    productos.insertar_producto(nombre_producto, precio)
    return jsonify({"mensaje": "producto creado con exito"})

@app.route('/actualizar_producto/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.get_json()
    nombre_producto = data.get('nombre_producto')
    precio = data.get('precio')
    if nombre_producto is None and precio is None:
        return jsonify({"error": "campos imcompletos para actualizacion"}), 400
   
    producto_existente= productos.obtener_producto(id)
    if producto_existente:
        productos.actualizar_prodructo(id, nombre_producto, precio)
        return jsonify({"mensaje": "producto actualizado con exito"})
    else:
        return jsonify({"mensaje": "este producto no existe"}), 404

@app.route('/eliminar_producto/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
     if productos.obtener_producto(id):
        productos.eliminar_producto(id)
        return jsonify({"mensaje": "prouducto elminado con exito"})
     else:
         return jsonify({"mensaje": "producto no existe"}), 404
    
if __name__== '_main_':
    app.run(debug=True)