import socket
import cv2
from custom_socket import CustomSocket

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

host = socket.gethostname()
port = 10011
c = CustomSocket(host, port)
c.clientConnect()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't read frame.")
        continue

    # print("Send")
    msg = c.req(frame)
    print(msg)

    # Show client frame
    cv2.imshow("client_cam", frame)
    if cv2.waitKey(1) == ord("q"):
        cap.release()

cv2.destroyAllWindows()
