from event.events import Quit
from event.events import Tick
from event.events import Initialization


class Model(object):
    def __init__(self, event_manager):
        self.running = False
        self.event_manager = event_manager

        event_manager.register(event=self)

    def run(self):
        self.running = True
        self.event_manager.post(event=Initialization())

        while self.running:
            tick = Tick()

            self.event_manager.post(event=tick)

    def notify(self, event):
        if isinstance(event, Quit):
            self.running = False
