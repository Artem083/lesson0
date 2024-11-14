from tkinter import *
import time


def tick():
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    clock.config(text=time2)
    # calls itself every 200 milliseconds to update the time
    # display as needed could use >200 ms
    clock.after(200, tick)


def tick1():
    #  get the current local ti[me from the PC
    time2 = time.strftime('%H:%M:%S')
    #  if time string has changed, update it
    clock1.config(text=time2)
    # calls itself every 200 milliseconds to update the time
    # display as needed could use >200 ms
    clock1.after(200, tick1)


root = Tk()
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)
tick()
clock1 = Label(root, font=('times', 20, 'bold'), bg='yellow')
clock1.pack(fill=BOTH, expand=1)
tick1()
root.mainloop()