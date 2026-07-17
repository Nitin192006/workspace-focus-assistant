import cv2


class CameraManager:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.capture = None

    def start(self):
        self.capture = cv2.VideoCapture(self.camera_index)

        if not self.capture.isOpened():
            raise RuntimeError("Unable to access webcam.")

    def read_frame(self):
        success, frame = self.capture.read()

        if not success:
            return None

        return frame

    def stop(self):
        if self.capture is not None:
            self.capture.release()

        cv2.destroyAllWindows()