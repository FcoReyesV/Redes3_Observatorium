import pymysql.cursors


class Conexion:

    def conectar(self):
        con = pymysql.connect(host='localhost', user="root", password="b4l3fir3", db="observatoriumPantitlan")
        return con

    def cerrar(self, conexion):
        conexion.close()