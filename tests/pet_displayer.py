import random
import threading
import tkinter as tk
import pyttsx3
# from PIL import Image, ImageTk
import os

class Pet(tk.Tk):
    def __init__(self, catimagepath, frame_num):
        tk.Tk.__init__(self)

        #initializing variables
        self.engine = pyttsx3.init()
        self.cycle = 0
        self.check = 0
        self.idle_num =[i + 1 for i in range(frame_num)] # self.idle_num = [1, 2, 3, ...]
        self.event_number = 0
        self.frame = None
        self.talking = False

        # Images
        self.idle = [tk.PhotoImage(file=catimagepath, format = 'gif -index %i' %(i)) for i in range(frame_num)]#idle gif

        # Prepping
        self.set_window_config()
        self.set_menu()
        self.set_labels()
        self.set_inputs()

    # ====== Initialization ======
    def set_labels(self):
        # Floating Window
        self.label = tk.Label(self,bd=0,bg='black')
        self.label.pack(side="left", fill="both", expand=True)
        
        self.label.pack()

    def say_hello(self):
        self.engine.say('Hola')
        self.engine.runAndWait()

    def set_inputs(self):
        self.bind("<Button-3>", self.open_action_menu)
        self.label.bind("<ButtonPress-1>", self.start_move)
        self.label.bind("<ButtonRelease-1>", self.stop_move)
        self.label.bind("<B1-Motion>", self.do_move)

    def set_menu(self):
        self.rclickmenu = tk.Menu(self, tearoff=0)
        self.rclickmenu.add_command(label='Hello', command=self.say_hello)
        self.rclickmenu.add_command(label='Log Off', command=self.exit_program)

    def exit_program(self):
        self.engine.say('Adios')
        self.engine.runAndWait()
        self.destroy()
        exit()
    
    def open_action_menu(self, event):
        try:
            self.rclickmenu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.rclickmenu.grab_release()

    # Configures window specifications
    def set_window_config(self):
        self.config(highlightbackground='black')
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
            
        self.geometry('320x300+'+str(self.winfo_x())+'+'+str(self.winfo_y()))
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

    # ====== Public Functions ======
    def add_action(self, name, action):
        self.rclickmenu.add_command(label=name, command=action)
        
    def run(self):
        #loop the program
        self.after(1,self.update)
        self.mainloop()



impath = os.path.realpath("../resources") + '\\'
catimagepath = impath + 'cat_idle_cropped.gif'

pet = Pet(catimagepath, 5)
pet.run()



