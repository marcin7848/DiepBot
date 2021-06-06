import math
import os
import sys
import time

from Point import Point
from Points import Points
import queue
from threading import Thread
import pyautogui
import keyboard

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
    (enemy_pos_x, enemy_pos_y) = queue_enemy.get()
    if enemy_pos_x != -1:
        #points.add_point(Point([0, 0, 250], enemy_x, enemy_y))
        pyautogui.moveTo(enemy_pos_x, enemy_pos_y)
    else:
        thread_points_to_eat.join()
        (point_eat_x, point_eat_y) = queue_point_to_eat.get()
        if point_eat_x != -1:
            #points.add_point(Point([0, 0, 250], point_x, point_y))
            pyautogui.moveTo(point_eat_x, point_eat_y)


def key_press(key, press_down):
    if press_down:
        pyautogui.keyDown(key)
    else:
        pyautogui.keyUp(key)


def move_right_left(points):
    (screen, width, height) = Points.get_screen()
    (friend_x, friend_y) = points.detect_closest_friend(screen, width, height)
    center_of_screen_x = int(width / 2)
    center_of_screen_y = int(height / 2)

    if friend_x != -1:
        dist = math.hypot(center_of_screen_x - friend_x, center_of_screen_y - friend_y)
        if dist > 100:
            if center_of_screen_x < friend_x:
                key_press('right', True)
                while center_of_screen_x < friend_x:
                    (screen, width, height) = Points.get_screen()
                    center_of_screen_x = int(width / 2)
                    (friend_x, friend_y) = points.detect_closest_friend(screen, width, height)
                key_press('right', False)
            else:
                key_press('left', True)
                while center_of_screen_x > friend_x:
                    (screen, width, height) = Points.get_screen()
                    center_of_screen_x = int(width / 2)
                    (friend_x, friend_y) = points.detect_closest_friend(screen, width, height)
                key_press('left', False)

        time.sleep(0.1)
        move_right_left(points)


def moving(points):
    (screen, width, height) = Points.get_screen()
    (friend_x, friend_y) = points.detect_closest_friend(screen, width, height)

    if friend_x != -1:
        center_of_screen_x = int(width / 2)
        center_of_screen_y = int(height / 2)
        dist = math.hypot(center_of_screen_x - friend_x, center_of_screen_y - friend_y)
        if dist > 100:
            if center_of_screen_x < friend_x:
                key_press('right', True)
            else:
                key_press('right', False)
            if center_of_screen_x > friend_x:
                key_press('left', True)
            else:
                key_press('left', False)
            if center_of_screen_y < friend_y:
                key_press('down', True)
            else:
                key_press('down', False)
            if center_of_screen_y > friend_y:
                key_press('up', True)
            else:
                key_press('up', False)
        else:
            key_press('left', False)
            key_press('right', False)
            key_press('up', False)
            key_press('down', False)

        time.sleep(0.1)
        moving(points)
        #points.add_point(Point([0, 0, 250], friend_x, friend_y))


def upgrade_tank():
    for i in range(10):
        pyautogui.press('6')
    for i in range(10):
        pyautogui.press('7')
    for i in range(10):
        pyautogui.press('4')
    for i in range(10):
        pyautogui.press('5')
    for i in range(10):
        pyautogui.press('2')

    time.sleep(5)
    upgrade_tank()


def break_loop(break_list):
    keyboard.wait("p")
    break_list.append(True)
    print('P')



thread_upgrade = Thread(target=upgrade_tank)
thread_upgrade.start()

break_list = []
thread_break_loop = Thread(target=break_loop, args=(break_list,))
thread_break_loop.start()

points = Points()
thread_moving = Thread(target=move_right_left, args=(points,))
thread_moving.start()


#while not break_list:
    #time.sleep(0.1)
    #points = Points()
    #(screenx, widthx, heightx) = Points.get_screen()



    #thread_shooting = Thread(target=shooting, args=(screenx, widthx, heightx))
    #thread_shooting.start()



    # points.draw_points()


