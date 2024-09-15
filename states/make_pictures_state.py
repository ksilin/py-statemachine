from .base_state import State

class MakePicturesState(State):
    def on_enter(self):
        self.context.display.show_camera_view()

    def handle_event(self, event):
        if event == 'capture':
            image = self.context.camera.capture_image()
            self.context.display.show_image(image)
        elif event == 'back':
            from .menu_state import MenuState  # Import moved inside the method
            return MenuState(self.context)
        return self
