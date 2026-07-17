import cv2
from core.config import APP_NAME
from vision.camera import CameraManager

class WorkspaceFocusAssistant:

    def __init__(self):
        self.app_name = APP_NAME
        self.camera = CameraManager()

    def run(self):

        print(f"{self.app_name} is starting...")
        self.camera.start()
        while True:

            frame = self.camera.read_frame()

            if frame is None:
                break

            cv2.imshow(self.app_name, frame)
            key = cv2.waitKey(1)

            if key == ord("q"):
                break

        self.camera.stop()