from weakref import WeakKeyDictionary


class Event(object):
    def __init__(self, event: object):
        self.event: object = event

    def __repr__(self):
        return "%s" % self.event


class State(object):
    def __init__(self, state: object):
        self.name: str = "State"
        self.state: object = state

    def __repr__(self):
        if self.state:
            return "%s pushed %s" % (self.name, self.state)
        else:
            return "%s popped" % self.name


class Quit(Event):
    def __init__(self):
        super(Quit, self).__init__(event="Quit")


class Tick(Event):
    def __init__(self):
        super(Tick, self).__init__(event="Tick")


class Input(Event):
    def __init__(self, unicode: str):
        self.unicode: str = unicode

        super(Input, self).__init__(event="Input")

    def __repr__(self):
        return "%s (unicode=%s)" % (self.event, self.unicode)


class Initialization(Event):
    def __init__(self):
        super(Initialization, self).__init__(event="Initialization")


class EventManager(object):
    def __init__(self):
        self.debug: bool = True
        self.listeners: WeakKeyDictionary = WeakKeyDictionary()

    def post(self, event: object):
        if not isinstance(event, Tick) and self.debug:
            print(repr(event))

        for listener in self.listeners.keys():
            listener.notify(event)

    def register(self, event: object):
        self.listeners[event]: int = 1

    def unregister(self, event: object):
        if event in self.listeners.keys():
            del self.listeners[event]
