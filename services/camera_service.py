# services/camera_service.py
import cv2

def capturar_imagen():
    video_capture = cv2.VideoCapture(0)
    print("Presiona 's' para capturar tu imagen")
    frame = None

    while True:
        ret, frame = video_capture.read()
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return frame
