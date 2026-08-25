import cv2
import os

save_folder = "dataset_raw"
os.makedirs(save_folder, exist_ok=True)

camera = cv2.VideoCapture(0)

count = len([f for f in os.listdir(save_folder) if f.endswith(".jpg")])

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera tak dapat baca.")
        break

    cv2.imshow("Capture Dataset - tekan S untuk simpan, Q untuk keluar", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        filename = os.path.join(save_folder, f"botol_{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Disimpan: {filename}")
        count += 1

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()