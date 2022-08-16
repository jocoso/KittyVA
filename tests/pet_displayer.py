import pyautogui
import random
import tkinter as tk
import os

class Pet(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
       
        self.init_variables()
        self.set_window_config()
        self.set_labels()

    # ====== Initialization ======

    # Initialize variables
    def init_variables(self):
        self.x = 30
        self.curx = 30
        self.cycle = 0
        self.check = 0
        self.idle_num =[1,2,3,4]
        self.event_number = 0
        self.frame = None
        self.impath = os.path.realpath("../resources") + "\\"
        self.idle = [tk.PhotoImage(file=self.impath+'cat_idle.gif',format = 'gif -index %i' %(i)) for i in range(4)]#idle gif

    def set_labels(self):
        self.label.pack(side="right", fill="both", expand=True)
        self.label.bind("<ButtonPress-1>", self.start_move)
        self.label.bind("<ButtonRelease-1>", self.stop_move)
        self.label.bind("<B1-Motion>", self.do_move)
        
        self.label.pack()

    # Configures window specifications
    def set_window_config(self):
        self.config(highlightbackground='black')
        self.label = tk.Label(self,bd=0,bg='black')
        self.overrideredirect(True)
        self.wm_attributes('-transparentcolor','black')

    # ====== Window Display ======

    def event(self):        
        self.check = 0
        self.after( 200, self.update ) #no. 1,2,3 = idle

    def gif_work(self):
        if self.cycle < len(self.idle) -1:
            self.cycle += 1
        else:
            self.cycle = 0
        self.event_number = random.randrange(1, 5 + 1,1)

    def update(self):
        #idle
        if self.check == 0:
            self.frame = self.idle[self.cycle]
            self.gif_work()
            
        self.geometry('300x300+'+str(self.winfo_x())+'+'+str(self.winfo_y()))
        self.label.configure(image=self.frame)
        self.after(1, self.event)

    # ====== Movement =======

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        move_x = self.winfo_x() + deltax
        move_y = self.winfo_y() + deltay
        self.geometry(f"+{move_x}+{move_y}")

    # ====== Public Function ======

    def run(self):
        #loop the program
        self.after(1,self.update)
        self.mainloop()


pet = Pet()
pet.run()



