from Conexionbd import conexionMysql

class modelUsuarios:
    def __init__(self):
        self.mibasededatos = conexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor
    
    def obtener_conexion(self):
        return self.mibasededatos
    
    def obtener_usuario(self, id):
        self.cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def obtener_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()
    
    def insertar_usuario(self, nombre, email, clave):
        val = (nombre, email, clave)
        sql = "INSERT INTO usuarios (nombre, email, clave) VALUES(%s, %s, %s)"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def actualizar_usuario(self, id, nombre, email, clave):
            val= (nombre, email, clave, id)
            sql= "UPDATE usuarios SET nombre= %s, email= %s, clave= %s WHERE id= %s"
            self.cursor.execute(sql, val)
            self.conexion.commit()

    def eliminar_usuarios(self, id):
            val = (id,)
            sql = "DELETE FROM usuarios WHERE id = %s"
            self.cursor.execute(sql, val)
            self.conexion.commit()

    def cerar_conexion(self):
         self.cursor.close()
         self.conexion.close()


    def verificar_usuario(self, email, password):
         val = (email, password)
         sql = "SELECT email, clave FROM usuarios WHERE email = %s AND clave = %s"
         self.cursor.execute(sql, val)
         user =  self.cursor.fetchone()
         if  user:
              return "index"
         else:
              return "contraseña incorrecta" 

