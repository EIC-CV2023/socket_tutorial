import cv2
from custom_socket import CustomSocket
import socket
import json
import numpy as np
import traceback


def main():
    HOST = socket.gethostname()
    PORT = 10011

    server = CustomSocket(HOST, PORT)
    server.startServer()

    while True:
        # Wait for connection from client
        conn, addr = server.sock.accept()
        print("Client connected from", addr)

        # Process frame received from client
        while True:
            res = dict()
            try:
                # Frame shape must be the same with client
                data = server.recvMsg(conn)
                img = np.frombuffer(data, dtype=np.uint8).reshape(720, 1280, 3)

                # Example: result = RGB of center pixel
                # res must be in dict not list
                cen_b, cen_g, cen_r = img[720 // 2, 1280 // 2]
                res = {"R": int(cen_r), "G": int(cen_g), "B": int(cen_b)}

                # Send back result
                print(res)
                server.sendMsg(conn, json.dumps(res))

                # Show server frame
                # cv2.imshow("server_cam", img)
                # if cv2.waitKey(1) == ord("q"):
                #     break

            except Exception as e:
                traceback.print_exc()
                print(e)
                print("Connection Closed")
                del res
                break

        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
