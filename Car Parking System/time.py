from datetime import datetime

import pywhatkit

def my_time():
    Current = datetime.now()
    time_h = int(Current.strftime("%H"))
    time_m = int(Current.strftime("%M")) + 1

    pywhatkit.sendwhatmsg("+91 98791 36395", "Hello", time_h, time_m, 20, True, 10)


my_time()