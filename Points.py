import tkinter
from tkinter import *
from threading import Thread

import pywintypes
import win32api
import win32con


class Points:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def __draw_letter(self):
        root = Tk()
        root.geometry('1920x1080')
        for point in self.points:
            label = tkinter.Label(root, text=point.letter, font=('Times New Roman', '40'), fg=point.color, bg='black')
            label.master.overrideredirect(True)
            #label.master.geometry(f"+{point.y}")
            label.master.lift()
            label.master.wm_attributes("-topmost", True)
            label.master.wm_attributes("-disabled", True)
            label.master.wm_attributes("-transparentcolor", "black")
            label.place(x=point.x, y=point.y)

            hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
            exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
            win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
            label.pack()

        root.mainloop()

    def draw_letter(self):
        thread = Thread(target=self.__draw_letter)
        thread.start()

    #def remove_letter(self):
        #self.thread.