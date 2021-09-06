from pygame import QUIT, KEYDOWN
from pygame.event import get

from event.events import Quit, Tick, Input


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
                elif event.type == KEYDOWN:
                    self.event_manager.post(event=Input(unicode=event.unicode))
