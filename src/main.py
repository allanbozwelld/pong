from controller.controllers import Controller
from event.events import EventManager
from model.models import Model
from view.views import View


def start():
    event_manager = EventManager()
    model = Model(event_manager=event_manager)
    controller = Controller(model=model, event_manager=event_manager)
    view = View(model=model, event_manager=event_manager)

    model.run()


if __name__ == "__main__":
    start()
