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
center_of_screen_x = int(width / 2)
center_of_screen_y = int(height / 2)
yPoints = []
xPoints = []

for rgb in colors_boundaries:
    pY, pX = np.where(np.all(screen == rgb, axis=2))
    yPoints.extend(pY)
    xPoints.extend(pX)

points_idx = []

for idx in range(len(xPoints)):
    similar_point_idx = -1
    for ex_idx in range(len(points_idx)):
        dist = math.hypot(xPoints[idx] - xPoints[points_idx[ex_idx]], yPoints[idx] - yPoints[points_idx[ex_idx]])
        if dist <= 60:
            similar_point_idx = ex_idx
            break

    if similar_point_idx == -1:
        points_idx.append(idx)
    else:
        similar_point_dist = math.hypot(center_of_screen_x - xPoints[points_idx[similar_point_idx]], center_of_screen_y - yPoints[points_idx[similar_point_idx]])
        dist = math.hypot(center_of_screen_x - xPoints[idx], center_of_screen_y - yPoints[idx])
        if dist < similar_point_dist:
            points_idx[similar_point_idx] = idx


points = Points()
for idx in points_idx:
    points.add_point(Point([0, 0, 250], xPoints[idx], yPoints[idx]))

while True:
    points.draw_points()

