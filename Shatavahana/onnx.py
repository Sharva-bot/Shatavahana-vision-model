import cv2
from ultralytics import YOLO

# Use best.onnx for NO LAG, best.pt will lag
# If you only have best.pt, use it but set imgsz=320
model = YOLO('best.onnx') # or 'best.pt' if onnx not downloaded
# model = YOLO('best.pt')

cap = cv2.VideoCapture(0) # 0 = webcam, remove CAP_DSHOW

# For speed
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # track = 10x better than model(frame), keeps ID
    results = model.track(frame, imgsz=320, conf=0.5, verbose=False)
    annotated_frame = results[0].plot()

    cv2.imshow("Indigenous Body Tracker - Q to quit", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()