from pygame import QUIT
from pygame.event import get

from event.events import Quit
from event.events import Tick
from event.events import Input


class Controller(object):
    def __init__(self, model, event_manager):
        self.model = model
        self.event_manager = event_manager

        event_manager.register(event=self)

    def notify(self, event):
        if isinstance(event, Tick):
            for event in get():
                if event.type == QUIT:
                    self.event_manager.post(event=Quit())
                else:
                    self.event_manager.post(event=Input(unicode=event.unicode))
