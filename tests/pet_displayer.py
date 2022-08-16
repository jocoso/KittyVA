import pyautogui
import random
import tkinter as tk
import os

class Pet(tk.Tk):
    def __init__(self, imagepath, frame_num):
        tk.Tk.__init__(self)

        self.cycle = 0
        self.check = 0
        self.idle_num =[i + 1 for i in range(frame_num)] # self.idle_num = [1, 2, 3, ...]
        self.event_number = 0
        self.frame = None
        self.idle = [tk.PhotoImage(file=imagepath, format = 'gif -index %i' %(i)) for i in range(frame_num)]#idle gif
       
        self.set_window_config()
        self.set_labels()

    # ====== Initialization ======
        

    def set_labels(self):
        # Floating Window
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


impath = os.path.realpath("../resources") + "\\"
imagepath = impath + 'cat_idle.gif'

pet = Pet(imagepath, 4)
pet.run()



