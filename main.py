import time

from Point import Point
from Points import Points
import queue
from threading import Thread
import pyautogui
import random

queue_enemy = queue.Queue()
queue_point_to_eat = queue.Queue()


def find_enemy(screen, width, height):
    (enemy_x, enemy_y) = points.detect_closest_enemy(screen, width, height)
    queue_enemy.put((enemy_x, enemy_y))


def find_point_to_eat(screen, width, height):
    (point_x, point_y) = points.detect_point_to_eat(screen, width, height)
    queue_point_to_eat.put((point_x, point_y))


def shooting(screen, width, height):
    thread_enemy = Thread(target=find_enemy, args=(screen, width, height))
    thread_enemy.start()

    thread_points_to_eat = Thread(target=find_point_to_eat, args=(screen, width, height))
    thread_points_to_eat.start()

    thread_enemy.join()
    (enemy_x, enemy_y) = queue_enemy.get()
    if enemy_x != -1:
        points.add_point(Point([0, 0, 250], enemy_x, enemy_y))
        pyautogui.moveTo(enemy_x, enemy_y)
    else:
        thread_points_to_eat.join()
        (point_x, point_y) = queue_point_to_eat.get()
        if point_x != -1:
            points.add_point(Point([0, 0, 250], point_x, point_y))
            pyautogui.moveTo(point_x, point_y)


while True:
    points = Points()
    (screen, width, height) = points.get_screen()

    thread_shooting = Thread(target=shooting, args=(screen, width, height))
    thread_shooting.start()


    #(friend_x, friend_y) = points.detect_closest_friend(screen, width, height)

    #if friend_x != -1:
        #points.add_point(Point([0, 0, 250], friend_x, friend_y))

    points.draw_points()

