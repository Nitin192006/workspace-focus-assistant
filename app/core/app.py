from core.config import APP_NAME
class WorkspaceFocusAssistant:

    def __init__(self):
        self.app_name = APP_NAME

    def run(self):
        print(f"{self.app_name} is starting...")