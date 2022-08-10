from datetime import datetime
import pywhatkit

def my_time():
    current_time = datetime.now()
    time_hr = int(current_time.strftime("%H"))
    time_min = int(current_time.strftime("%M")) 
    
    pywhatkit.sendwhatmsg("+91 9879136395", "Your slot is booked!", time_hr, time_min, 20, True, 10)


my_time()