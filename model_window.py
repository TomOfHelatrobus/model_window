from tkinter import *

def front_window(self):
    if self != "none": self.destroy()
    F = Frame(root)
    F.pack(fill=BOTH, side=LEFT)
    buttons = Canvas(F)  # button bar
    buttons.pack(fill=BOTH, side=BOTTOM)
# link up the canvas and scrollbar
    S = Scrollbar(F)
    C = Canvas(F, width=1600)
    S.pack(side=RIGHT, fill=BOTH)
    C.pack(side=LEFT, fill=BOTH)
    S.configure(command=C.yview, orient="vertical")
    C.configure(yscrollcommand=S.set)
    if sys.platform == "win32":
        C.bind_all('<MouseWheel>', lambda event: C.yview_scroll(int(-1 * (event.delta / 120)), "units"))
    elif sys.platform == "linux":
        C.bind_all('<Button-4>', lambda event: C.yview('scroll',-1,'units'))
        C.bind_all('<Button-5>', lambda event: C.yview('scroll',1,'units'))
# create the frame inside the canvas
    FF = Frame(C)
    C.create_window((0, 0), window=FF, anchor=NW)
    return F,S,C,FF,buttons

def rear_window(wd):
    root.update()
    wd[2].config(scrollregion=wd[2].bbox("all"))
    mainloop()

def first_window(self):
    root.title("#1")
    wd = front_window(self)  # get window objects 0=F,1=S,2=C,3=FF,4=buttons
    Label(wd[3],text="hello there from the first window").pack()
    Button(wd[4], text="second window", width=20, anchor="w", command=lambda: second_window(wd[0])).pack(side=LEFT)
    Button(wd[4], text="Quit", width=20, anchor="w", command=lambda: root.destroy()).pack(side=LEFT)
    rear_window(wd)

def second_window(self):
    root.title("#2")
    wd = front_window(self)  # get window objects 0=F,1=S,2=C,3=FF,4=buttons
    Label(wd[3],text="hello there from the second window").pack()
    Button(wd[4], text="first window", width=20, anchor="w", command=lambda: first_window(wd[0])).pack(side=LEFT)
    Button(wd[4], text="Quit", width=20, anchor="w", command=lambda: root.destroy()).pack(side=LEFT)
    rear_window(wd)

if __name__ == "__main__":
    position_x = 100
    position_y = 50
    size_x = 625
    size_y = 600
    root = Tk()
    root.geometry("%dx%d+%d+%d" % (size_x,size_y,position_x,position_y))
    first_window("none")