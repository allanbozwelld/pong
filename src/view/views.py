from pygame import init, quit
from pygame.display import flip, set_caption, set_mode
from pygame.time import Clock

from event.events import Quit, Tick, EventManager, Initialization
from model.models import Model, STATE_MENU, STATE_PLAY


class View(object):
    def __init__(self, model: Model, manager: EventManager):
        self.model: Model = model
        self.manager: EventManager = manager

        self.clock: None = None
        self.screen: None = None
        self.initialized: bool = False

        manager.register(event=self)

    def notify(self, event: object):
        if isinstance(event, Initialization):
            self.initialization()
        elif isinstance(event, Quit):
            self.initialized: bool = False

            quit()
        elif isinstance(event, Tick):
            if not self.initialized:
                return

            state = self.model.state.peek()

            if state == STATE_MENU:
                self.render_menu()

            if state == STATE_PLAY:
                self.render_play()

            self.clock.tick(30)

    def render_menu(self):
        self.screen.fill((0, 0, 0))

        flip()

    def render_play(self):
        self.screen.fill((0, 0, 0))

        flip()

    def initialization(self):
        init()
        set_caption("Pong!")

        self.clock: Clock = Clock()
        self.screen: set_mode = set_mode(size=(800, 600))
        self.initialized: bool = True
