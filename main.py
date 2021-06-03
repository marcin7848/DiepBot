import tkinter, win32api, win32con, pywintypes
from Point import Point
import time
from Points import Points

points = Points()
points.add_point(Point('TestA', 'blue', '200', '200'))
points.add_point(Point('TestB', 'red', '300', '300'))

points.draw_letter()


time.sleep(2)
print('test')
#letter.remove_letter()
