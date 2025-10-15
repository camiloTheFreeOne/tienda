import mysql.connector 
from mysql.connector   import Error

class conexionMysql:
    def __init__(self):
        try:
            self.mibasededatos = mysql.connector.connect(
                host= "localhost",
                port= "3306",
                user= "root",
                password= "",
                database= "ventas"
            )
            self.conexion = self.mibasededatos
            self.cursor = self.conexion.cursor()

            if self.mibasededatos.is_connected():
                db_info = self.mibasededatos.get_server_info()
                print (f"conected to my sql server, version: ,{db_info}")
        except Error as e:
            print(f"error al conectar conla base de tatos: {e}")
    
    def cerar_conexion(self):
        if self.mibasededatos.is_connected():
            self.cursor.close()
            self.conexion.close()
            print("coneccion cerrada correctamente")
if __name__== "_main_":
    conexion = conexionMysql()
    conexion.cerar_conexion()