import psutil
from pync import Notifier
import threading
import os

import BatterySafe.ThreadManager as ThreadManager


class BatteryManager(object):
    MAX_CHARGE = 100            # Percentage
    MIN_CHARGE = 5             # Percentage
    NOTIFICATION_INTERVAL = 2   # Seconds

    def __init__(self, *args):
        """Constructor
        """
        super(BatteryManager, self).__init__(*args)
        # print(self.plugged, self.percent)
        # self.percent = 100
        # self.plugged = True
        self.notifierEvent = ThreadManager.Event()
        self.notifierThread = ThreadManager.Job(self._doNotify, self.notifierEvent,
                                                self.NOTIFICATION_INTERVAL)
        self.notifierThread.run()

    def _doNotify(self):
        """Called every [NOTIFICATION_INTERVAL] seconds to perform a battery checkup
        """
        self._updateBatteryState()
        self._notify()

    def _updateBatteryState(self):
        """Updates the battery state
        """
        battery = psutil.sensors_battery()
        self.plugged = battery.power_plugged
        self.percent = battery.percent

    def _notify(self):
        """Generates a notification and invokes the notifier
        """
        if self.plugged and self.percent >= self.MAX_CHARGE:
            title = "💣 Unplug the charger now"
            subtext = "Your computer battery needs to discharge now to stay healthy."
        elif not self.plugged and self.percent <= self.MIN_CHARGE:
            title = "⚡️ Plug in the charger now"
            subtext = "Your computer battery needs to charge now to stay turned on."
        else:
            return
        description = "Your battery is at {batteryLevel}%. {subtext}".format(
            batteryLevel=self.percent, subtext=subtext)
        Notifier.notify(description, title=title, group=os.getpid())

    def __del__(self):
        """Destructor
        """
        self.notifierThread.stop()
