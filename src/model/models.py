from event.events import Quit, Tick, State, EventManager, Initialization

STATE_MENU = 1
STATE_PLAY = 2


class Model(object):
    def __init__(self, manager: EventManager):
        self.state: StateModel = StateModel()
        self.running: bool = False
        self.manager: EventManager = manager

        manager.register(event=self)

    def run(self):
        self.state.push(STATE_MENU)
        self.running: bool = True
        self.manager.post(event=Initialization())

        while self.running:
            self.manager.post(event=Tick())

    def notify(self, event: object):
        if isinstance(event, Quit):
            self.running: bool = False

        if isinstance(event, State):
            if not event.state:
                if not self.state.pop():
                    self.manager.post(Quit())
            else:
                self.state.push(event.state)


class StateModel(object):
    def __init__(self):
        self.stack = []

    def push(self, state: object):
        self.stack.append(state)

        return state

    def pop(self):
        try:
            self.stack.pop()

            return len(self.stack) > 0
        except IndexError:
            return None

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None
