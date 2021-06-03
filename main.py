import math

from Point import Point
from Points import Points
import PIL.ImageGrab
import numpy as np

'''
points = Points()
points.add_point(Point([0, 0, 250], 200, 200))
points.add_point(Point([250, 0, 0], 300, 300))

while True:
    points.draw_points()
'''

screen = PIL.ImageGrab.grab()
width, height = screen.size
colors_boundaries = [
    [255, 232, 105],  # yellow
    [252, 118, 119],  # red
    [118, 141, 252]  # blue
]

screen = np.array(screen)
center_of_screen_y = int(width / 2)
center_of_screen_x = int(height / 2)
closest_point_idx = -1
distance = 999999
yPoints = []
xPoints = []

for rgb in colors_boundaries:
    pY, pX = np.where(np.all(screen == rgb, axis=2))
    yPoints.extend(pY)
    xPoints.extend(pX)

for idx in range(len(xPoints)):
    dist = math.hypot(center_of_screen_x - xPoints[idx], center_of_screen_y - yPoints[idx])
    if distance > dist:
        distance = dist
        closest_point_idx = idx

if closest_point_idx > -1:
    points = Points()
    points.add_point(Point([0, 0, 250], xPoints[closest_point_idx], yPoints[closest_point_idx]))

    while True:
        points.draw_points()
