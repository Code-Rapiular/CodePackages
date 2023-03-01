from tkinter import *
from time import *

def update():
    time_String = str(strftime("%I:%M:%S %p"))
    time_label.config(text=time_String)

    day_String = str(strftime("%A"))
    day_label.config(text=day_String)

    date_String = str(strftime("%d ,%B , %Y")) #DD/MM/YY
    date_label.config(text=date_String)

    window.after(1000,update) #Update self 

window = Tk() #Initialise Window

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black") #Style CSS
time_label.pack() 

day_label = Label(window,font=("Ink Free",25)) #Style CSS
day_label.pack()

date_label = Label(window,font=("Ink Free",25)) #Style CSS
date_label.pack()

update()

window.mainloop() #Call Window