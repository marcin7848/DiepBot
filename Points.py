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
    def get_screen():
        screen = PIL.ImageGrab.grab()
        width, height = screen.size
        screen = np.array(screen)
        return screen, width, height

    @staticmethod
    def remove_points():
        hwnd = win32gui.WindowFromPoint((0, 0))
        monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
        win32gui.RedrawWindow(hwnd, monitor, None, win32con.RDW_INVALIDATE)

    def detect_point_to_eat(self, screen, width, height):
        colors_boundaries_to_eat = [
            [255, 232, 105],  # yellow
            [252, 118, 119],  # red
            [118, 141, 252],  # blue
            [241, 119, 221]  # pink
        ]

        return self.__detect_closest_point(colors_boundaries_to_eat, screen, width, height)

    def detect_closest_enemy(self, screen, width, height):
        colors_boundaries_enemies = [
            [0, 178, 225],  # blue
            [0, 225, 110],  # green
            [191, 127, 245]  # purple
        ]
        return self.__detect_closest_point(colors_boundaries_enemies, screen, width, height)

    def detect_closest_friend(self, screen, width, height):
        colors_boundaries_friends = [
            [88, 88, 88]  # grey
        ]

        return self.__detect_closest_point(colors_boundaries_friends, screen, width, height)

    @staticmethod
    def __detect_closest_point(colors_boundaries, screen, width, height):
        center_of_screen_x = int(width / 2)
        center_of_screen_y = int(height / 2)
        y_points = []
        x_points = []

        for rgb in colors_boundaries:
            p_y, p_x = np.where(np.all(screen == rgb, axis=2))
            y_points.extend(p_y)
            x_points.extend(p_x)

        closest_point_idx = -1
        distance = 999999

        for idx in range(len(x_points)):
            dist = math.hypot(center_of_screen_x - x_points[idx], center_of_screen_y - y_points[idx])
            if distance > dist:
                distance = dist
                closest_point_idx = idx

        if closest_point_idx == -1:
            return -1, -1

        return x_points[closest_point_idx], y_points[closest_point_idx]