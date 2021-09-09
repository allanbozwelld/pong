from pygame import QUIT, KEYDOWN, K_SPACE, K_ESCAPE
from pygame.event import get

from event.events import Quit, Tick, Input, State, EventManager
from model.models import Model, STATE_MENU, STATE_PLAY


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

                    if event.key == K_ESCAPE:
                        self.manager.post(State(state=None))
                    else:
                        state = self.model.state.peek()

                        if state == STATE_MENU:
                            self.keydown_menu(event)

                        if state == STATE_PLAY:
                            self.keydown_play(event)

    def keydown_menu(self, event):
        if event.key == K_ESCAPE:
            self.manager.post(State(None))

        if event.key == K_SPACE:
            self.manager.post(State(STATE_PLAY))

    def keydown_play(self, event):
        if event.key == K_ESCAPE:
            self.manager.post(State(None))
