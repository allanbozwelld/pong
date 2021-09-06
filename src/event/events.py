from weakref import WeakKeyDictionary


class Event(object):
    def __init__(self, event):
        self.event = event

    def __repr__(self):
        return "%s" % self.event


class Quit(Event):
    def __init__(self):
        super(Quit, self).__init__(event="Quit")


class Tick(Event):
    def __init__(self):
        super(Tick, self).__init__(event="Tick")


class Input(Event):
    def __init__(self, unicode):
        self.unicode = unicode
        super(Input, self).__init__(event="Input")

    def __repr__(self):
        return "%s (unicode=%s)" % (self.event, self.unicode)


class Initialization(Event):
    def __init__(self):
        super(Initialization, self).__init__(event="Initialization")


class EventManager(object):
    def __init__(self):
        self.listeners = WeakKeyDictionary()

    def post(self, event):
        if not isinstance(event, Tick):
            print(repr(event))

        for listener in self.listeners.keys():
            listener.notify(event)

    def register(self, event):
        self.listeners[event] = 1

    def unregister(self, event):
        if event in self.listeners.keys():
            del self.listeners[event]
