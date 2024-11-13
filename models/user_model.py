# models/user_model.py
from database.connection import get_connection

def registrar_usuario(name, face_encoding):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, face_encoding) VALUES (%s, %s)", 
                   (name, face_encoding.tobytes()))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"{name} registrado exitosamente.")

def obtener_usuarios():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name, face_encoding FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users
