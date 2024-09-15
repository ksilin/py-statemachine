from controllers.camera_controller import CameraController
from controllers.display_controller import DisplayController
from context import AppContext
from states.menu_state import MenuState
from state_machine import StateMachine
from utils.event_handler import get_next_event

def main():
    # Initialize controllers
    display_controller = DisplayController()
    camera_controller = CameraController()

    # Create context
    context = AppContext(display_controller, camera_controller)

    # Initialize state machine
    initial_state = MenuState(context)
    state_machine = StateMachine(initial_state)

    # Main event loop
    while True:
        event = get_next_event()
        state_machine.handle_event(event)

if __name__ == '__main__':
    main()
