import math

import PIL.ImageGrab
import numpy as np
import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics
from threading import Thread


class Points:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def __draw_points(self):
        self.remove_points()
        dc = win32gui.GetDC(0)

        for point in self.points:
            color = win32api.RGB(point.color[0], point.color[1], point.color[2])
            for x in range(15):
                for y in range(15):
                    win32gui.SetPixel(dc, point.x + x, point.y+y, color)

    def draw_points(self):
        thread = Thread(target=self.__draw_points)
        thread.start()

    @staticmethod
    def remove_points():
        hwnd = win32gui.WindowFromPoint((0, 0))
        monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
        win32gui.RedrawWindow(hwnd, monitor, None, win32con.RDW_INVALIDATE)

    def detect_points_to_eat(self):
        screen = PIL.ImageGrab.grab()
        width, height = screen.size
        colors_boundaries_to_eat = [
            [255, 232, 105],  # yellow
            [252, 118, 119],  # red
            [118, 141, 252],  # blue
            [241, 119, 221]  # pink
        ]
        screen = np.array(screen)
        center_of_screen_x = int(width / 2)
        center_of_screen_y = int(height / 2)
        yPoints = []
        xPoints = []

        for rgb in colors_boundaries_to_eat:
            pY, pX = np.where(np.all(screen == rgb, axis=2))
            yPoints.extend(pY)
            xPoints.extend(pX)

        points_idx = []

        for idx in range(len(xPoints)):
            similar_point_idx = -1
            for ex_idx in range(len(points_idx)):
                dist = math.hypot(xPoints[idx] - xPoints[points_idx[ex_idx]],
                                  yPoints[idx] - yPoints[points_idx[ex_idx]])
                if dist <= 60:
                    similar_point_idx = ex_idx
                    break

            if similar_point_idx == -1:
                points_idx.append(idx)
            else:
                similar_point_dist = math.hypot(center_of_screen_x - xPoints[points_idx[similar_point_idx]],
                                                center_of_screen_y - yPoints[points_idx[similar_point_idx]])
                dist = math.hypot(center_of_screen_x - xPoints[idx], center_of_screen_y - yPoints[idx])
                if dist < similar_point_dist:
                    points_idx[similar_point_idx] = idx

        return xPoints, yPoints, points_idx


