class AppContext:
    def __init__(self, display_controller, camera_controller):
        self.display = display_controller
        self.camera = camera_controller
        # Add other shared resources if needed
