# services/face_recognition.py
import face_recognition
import numpy as np
from models.user_model import obtener_usuarios

def codificar_rostro(frame):
    face_locations = face_recognition.face_locations(frame)
    if face_locations:
        return face_recognition.face_encodings(frame, face_locations)[0]
    else:
        print("No se detectó un rostro.")
        return None

def reconocer_rostro(face_encoding):
    usuarios = obtener_usuarios()
    for user in usuarios:
        nombre, encoding_binario = user
        stored_encoding = np.frombuffer(encoding_binario, dtype=np.float64)
        
        if face_recognition.compare_faces([stored_encoding], face_encoding, tolerance=0.6)[0]:
            return nombre
    return None
