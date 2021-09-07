from controller.controllers import Controller
from event.events import EventManager
from model.models import Model
from view.views import View


def start():
    manager: EventManager = EventManager()
    model: Model = Model(manager=manager)
    controller: Controller = Controller(model=model, manager=manager)
    view: View = View(model=model, manager=manager)

    model.run()


if __name__ == "__main__":
    start()
