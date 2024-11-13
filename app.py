# app.py
from services.camera_service import capturar_imagen
from services.face_recognition import codificar_rostro, reconocer_rostro
from models.user_model import registrar_usuario

def registrar_nuevo_usuario():
    nombre = input("Introduce tu nombre: ")
    frame = capturar_imagen()
    face_encoding = codificar_rostro(frame)
    if face_encoding is not None:
        registrar_usuario(nombre, face_encoding)

def iniciar_sesion():
    frame = capturar_imagen()
    face_encoding = codificar_rostro(frame)
    if face_encoding is not None:
        nombre = reconocer_rostro(face_encoding)
        if nombre:
            print(f"Bienvenido {nombre}!")
        else:
            print("Usuario no reconocido.")

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            registrar_nuevo_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
