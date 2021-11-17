from tkinter import *
import time
import playsound

root = Tk()
root.title("Clock")
root.geometry("400x400")
root.resizable(0,0)  #to prevent resizing
root.config(bg ='blanched almond')

Label(root, text = 'Clock Timer',  bg="cyan", font="Aesthetic 19", relief=SUNKEN).pack()

Label(root, font ='arial 15 bold', text = 'Current Time :', bg = 'papaya whip').place(x = 40 ,y = 70)
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(x = 190 , y = 70)
clock()

second = StringVar()
screen_sec = Entry(root, textvar = second, width = 2, font = "lucida 12 bold").place(x=250, y=155)
second.set('00')
# screen_sec.pack(pady = 9, padx = 10)

minute = StringVar()
screen_min = Entry(root, textvar = minute, width = 2, font = "lucida 12 bold").place(x=225, y=155)
minute.set('00')
# screen_min.pack(pady = 9, padx = 10)

hour = StringVar()
screen_hour = Entry(root, textvar = hour, width = 2, font = "lucida 12 bold").place(x=200, y=155)
hour.set('00')
# screen_hour.pack(pady = 9, padx = 10)

def CountDown():
    time = int (hour.get()) * 3600 + int (minute.get()) * 60 + int (second.get())
    while time > -1:
        minute_countdown = time // 60
        second_countdown = time % 60
        hour_countdown = 0

        if minute_countdown > 60:
            hour_countdown = minute_countdown // 60
            minute_countdown = minute_countdown % 60

        second.set(second_countdown)
        minute.set(minute_countdown)
        hour.set(hour_countdown)

        root.update()
        # time.sleep(1)

        if(time == 0):
            playsound('Dusk Till Dawn(Mr-Jatt1.com)')
            second.set('00')
            minute.set('00')
            hour.set('00')
        time = time-1

Label(root, font ='arial 15 bold', text = 'Set time:',   bg ='papaya whip').place(x = 40 ,y = 150)
Button(root, text='START', bd ='5', command = CountDown, bg = 'antique white', font = 'arial 10 bold').place(x=150, y=210)
root.mainloop()