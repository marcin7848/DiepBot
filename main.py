from Point import Point
from Points import Points

points = Points()
points.add_point(Point([0, 0, 250], 200, 200))
points.add_point(Point([250, 0, 0], 300, 300))

while True:
    points.draw_points()


