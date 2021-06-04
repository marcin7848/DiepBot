from Point import Point
from Points import Points

while True:
    points = Points()
    (screen, width, height) = points.get_screen()
    (xPoints, yPoints, points_idx) = points.detect_points_to_eat(screen, width, height)

    for idx in points_idx:
        points.add_point(Point([0, 0, 250], xPoints[idx], yPoints[idx]))

    points.draw_points()

