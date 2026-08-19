# SmartVision camera test
import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera tidak dapat dibuka.")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        print("Gagal membaca camera.")
        break

    cv2.imshow("SmartVision - Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()