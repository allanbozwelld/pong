from pygame import QUIT, KEYDOWN
from pygame.event import get

from event.events import Quit, Tick, Input, EventManager
from model.models import Model


class Controller(object):
    def __init__(self, model: Model, manager: EventManager):
        self.model: Model = model
        self.manager: EventManager = manager

        manager.register(event=self)

    def notify(self, event: object):
        if isinstance(event, Tick):
            for event in get():
                if event.type == QUIT:
                    self.manager.post(event=Quit())
                elif event.type == KEYDOWN:
                    self.manager.post(event=Input(unicode=event.unicode))
