from pygame import init, quit
from pygame.display import flip, set_caption, set_mode
from pygame.time import Clock

from event.events import Quit, Tick, Initialization


class View(object):
    def __init__(self, model, event_manager):
        self.model = model
        self.event_manager = event_manager

        self.clock = None
        self.screen = None
        self.initialized = False

        event_manager.register(event=self)

    def notify(self, event):
        if isinstance(event, Initialization):
            self.initialization()
        elif isinstance(event, Quit):
            self.initialized = False

            quit()
        elif isinstance(event, Tick):
            self.render()

            self.clock.tick(30)

    def render(self):
        if not self.initialized:
            return

        self.screen.fill((0, 0, 0))

        flip()

    def initialization(self):
        init()
        set_caption("Pong!")

        self.clock = Clock()
        self.screen = set_mode(size=(800, 600))
        self.initialized = True
