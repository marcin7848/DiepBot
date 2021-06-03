import time

import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics
from threading import Thread


class Points:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def __draw_points(self):
        #self.remove_points()
        dc = win32gui.GetDC(0)

        for point in self.points:
            color = win32api.RGB(point.color[0], point.color[1], point.color[2])
            for x in range(10):
                for y in range(10):
                    win32gui.SetPixel(dc, point.x + x, point.y+y, color)


    def draw_points(self):
        thread = Thread(target=self.__draw_points)
        thread.start()

    @staticmethod
    def remove_points():
        hwnd = win32gui.WindowFromPoint((0, 0))
        monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
        win32gui.RedrawWindow(hwnd, monitor, None, win32con.RDW_INVALIDATE)

