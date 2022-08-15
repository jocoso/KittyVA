import pyautogui
import random
import tkinter as tk
import os

x = 30
cycle = 0
check = 0
idle_num =[1,2,3,4,5]
event_number = 0
impath = os.path.realpath("../resources") + "\\"

def event(cycle,check,event_number,x):
    if event_number in idle_num:
        check = 0
        window.after( 400, update, cycle, check, event_number, x ) #no. 1,2,3 = idle

def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) -1:
        cycle += 1
    else:
        cycle = 0

    event_number = 1
    return cycle, event_number

def update(cycle,check,event_number,x):
    #idle
    if check == 0:
        frame = idle[cycle]
        cycle ,event_number = gif_work(cycle,idle,event_number,1,5)
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)

def start_move(event):
    window.x = event.x
    window.y = event.y

def stop_move(event):
    window.x = None
    window.y = None

def do_move(event):
    delta_x = event.x - window.x
    delta_y = event.y - window.y
    move_x = window.winfo_x() + delta_x
    move_y = window.winfo_y() + delta_y
    window.geometry(f"+{move_x}+{move_y}")

window = tk.Tk()

idle = [tk.PhotoImage(file=impath+'cat_idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle gif

move_x = 0
move_y = 0


#window configuration
window.geometry('300x300+'+str(x)+'+30')
window.config(highlightbackground='black')
label = tk.Label(window,bd=0,bg='black')
window.overrideredirect(True)
label.pack(side="right", fill="both", expand=True)
label.bind("<ButtonPress-1>", start_move)
label.bind("<ButtonRelease-1>", stop_move)
label.bind("<B1-Motion>", do_move)
window.wm_attributes('-transparentcolor','black')
label.pack()

#loop the program
window.after(1,update,cycle,check,event_number,x)
window.mainloop()
