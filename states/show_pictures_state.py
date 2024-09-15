from .base_state import State

class ShowPicturesState(State):
    def on_enter(self):
        self.context.display.show_picture_gallery()

    def handle_event(self, event):
        if event == 'select_picture':
            image = self.context.display.get_selected_image()
            self.context.display.show_image(image)
        elif event == 'back':
            from .menu_state import MenuState  # Import moved inside the method
            return MenuState(self.context)
        return self
