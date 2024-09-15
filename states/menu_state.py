from .base_state import State
from .make_pictures_state import MakePicturesState
from .show_pictures_state import ShowPicturesState

class MenuState(State):
    def on_enter(self):
        self.context.display.show_menu_options(['Make Pictures', 'Show Pictures'])

    def handle_event(self, event):
        if event == 'select_option':
            selected_option = self.context.display.get_selected_option()
            if selected_option == 'Make Pictures':
                return MakePicturesState(self.context)
            elif selected_option == 'Show Pictures':
                return ShowPicturesState(self.context)
        return self
