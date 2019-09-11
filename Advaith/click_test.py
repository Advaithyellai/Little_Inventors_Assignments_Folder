import tkinter as tk
import time
def openup(event):
    root = tk.Tk()
    a = 0
    def enterpress():
        global a
        a+=1
        tex.set(a)
        def buttonpress():
            global a
            print("clicks in a second(clicks/second) = {}".format(a/b.get()))
            root.destroy()
        root.after(int(b.get())*1000, buttonpress)
        return
    tex = tk.IntVar()
    tk.Label(root, textvariable = tex).grid()
    tk.Button(root, text = "Click Me!!!", height = 10, width = 20,command = enterpress).grid()
root_2 = tk.Tk()
tk.Label(root_2, text = "No. of seconds = ").grid(row = 0, column = 0)
b = tk.Entry(root_2)
b.grid(row = 0, column = 1)
b.bind('<Return>', openup)
root_2.mainloop()