import mysql.conector

def conectar ():
    return mysql.conector.conect(
        host= "localhost",
        user="root",
        password="Welcome@ds",
        database="estoque"
    )
