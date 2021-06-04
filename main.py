import time

from Point import Point
from Points import Points
import queue
from threading import Thread
import pyautogui
import random

queue_enemy = queue.Queue()
queue_points_to_eat = queue.Queue()


def find_enemy(screen, width, height):
    (enemy_x, enemy_y) = points.detect_closest_enemy(screen, width, height)
    queue_enemy.put((enemy_x, enemy_y))


def find_points_to_eat(screen, width, height):
    (xPoints, yPoints, points_idx) = points.detect_points_to_eat(screen, width, height)
    queue_points_to_eat.put((xPoints, yPoints, points_idx))


while True:
    points = Points()
    (screen, width, height) = points.get_screen()

    thread_enemy = Thread(target=find_enemy, args=(screen, width, height))
    thread_enemy.start()

    thread_points_to_eat = Thread(target=find_points_to_eat, args=(screen, width, height))
    thread_points_to_eat.start()

    thread_enemy.join()
    (enemy_x, enemy_y) = queue_enemy.get()
    if enemy_x != -1:
        points.add_point(Point([0, 0, 250], enemy_x, enemy_y))
        #pyautogui.moveTo(enemy_x, enemy_y)
    else:
        thread_points_to_eat.join()
        (xPoints, yPoints, points_idx) = queue_points_to_eat.get()
        for idx in points_idx:
            points.add_point(Point([0, 0, 250], xPoints[idx], yPoints[idx]))

        if len(points_idx) > 0:
            index = random.choice(points_idx)
            #pyautogui.moveTo(xPoints[index], yPoints[index])




    #(friend_x, friend_y) = points.detect_closest_friend(screen, width, height)

    #if friend_x != -1:
        #points.add_point(Point([0, 0, 250], friend_x, friend_y))

    points.draw_points()

