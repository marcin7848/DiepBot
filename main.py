from Point import Point
from Points import Points

while True:
    points = Points()
    (xPoints, yPoints, points_idx) = points.detect_points_to_eat()

    for idx in points_idx:
        points.add_point(Point([0, 0, 250], xPoints[idx], yPoints[idx]))

    points.draw_points()

