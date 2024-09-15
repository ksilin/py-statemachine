class StateMachine:
    def __init__(self, initial_state):
        self.state = initial_state
        self.state.on_enter()

    def handle_event(self, event):
        next_state = self.state.handle_event(event)
        if next_state != self.state:
            self.state.on_exit()
            self.state = next_state
            self.state.on_enter()
