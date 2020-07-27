import psutil
from pync import Notifier
import threading
import os


class BatterySafe(object):
    MAX_CHARGE = 100
    MIN_CHARGE = 5

    def __init__(self, *args):
        super(BatterySafe, self).__init__(*args)
        self.updateBatteryState()
        print(self.plugged, self.percent)
        self.notify()

    def updateBatteryState(self):
        battery = psutil.sensors_battery()
        self.plugged = battery.power_plugged
        self.percent = str(battery.percent)

    def notify(self):

        if self.plugged and self.percent >= MAX_CHARGE:
            title = "💣 Unplug the charger now"
            subtext = "Your computer battery needs to discharge now to stay healthy."
        elif not self.plugged and self.percent <= MIN_CHARGE:
            title = "⚡️ Plug in the charger now"
            subtext = "Your computer battery needs to charge now to stay turned on."
        else:
            return

        description = "Your battery is at {batteryLevel}% {subtext}".format(
            batteryLevel=self.percent, subtext=subtext)
        Notifier.notify(description, title=title, group=os.getpid())


if __name__ == '__main__':
    BatterySafe()
