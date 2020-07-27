import threading


class Event(threading.Event):
    """Factory class returns a thread event
    """

    def __init__(self):
        super(Event, self).__init__()


class Job(threading.Thread):
    def __init__(self, callback, event, interval):
        """Runs the callback functions after interval seconds

        Args:
            callback (function): [callback fucntion to invoke]
            event ([type]): [external event for controlling the update operation]
            interval (int): [time in seconds after which required to fire the callback]
        """

        self.callback = callback
        self.event = event
        self.interval = interval
        self.stopFlag = False
        super(Job, self).__init__()

    def run(self):
        while not self.event.wait(self.interval):
            if not self.stopFlag:
                self.callback()

    def stop(self):
        self.stopFlag = True
