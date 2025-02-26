import cv2
import numpy as np


hsv_min = np.array([255, 255, 255])
hsv_max = np.array([0, 0, 0])

def get_hsv_value(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_value = hsv_frame[y, x]
        print(f"HS: {hsv_value}")
        global hsv_min, hsv_max
        hsv_min = np.minimum(hsv_min, hsv_value)
        hsv_max = np.maximum(hsv_max, hsv_value)


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("Frame", frame)
    cv2.setMouseCallback("Frame", get_hsv_value)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print(f"HSV min: {hsv_min}")
print(f"HSV max: {hsv_max}")
cap.release()
cv2.destroyAllWindows()
