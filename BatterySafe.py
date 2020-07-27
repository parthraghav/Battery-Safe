import psutil
import pync
import os

# import win32api
# win32api.MessageBox(0, percent+'% | '+plugged, 'Battery Info')

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
if plugged == False:
    plugged = "Not Plugged In"
else:
    plugged = "Plugged In"
# print(percent+'% | '+plugged)
pync.notify(percent+'% | '+plugged, title="🔋Battery Safe",
            group=os.getpid(), execute='say "OMG"')
