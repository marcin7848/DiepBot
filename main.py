from Point import Point
from Points import Points

while True:
    points = Points()
    (screen, width, height) = points.get_screen()

    #(xPoints, yPoints, points_idx) = points.detect_points_to_eat(screen, width, height)
    #for idx in points_idx:
        #points.add_point(Point([0, 0, 250], xPoints[idx], yPoints[idx]))

    #(enemy_x, enemy_y) = points.detect_closest_enemy(screen, width, height)
    #if enemy_x != -1:
        #points.add_point(Point([0, 0, 250], enemy_x, enemy_y))


    (friend_x, friend_y) = points.detect_closest_friend(screen, width, height)

    if friend_x != -1:
        points.add_point(Point([0, 0, 250], friend_x, friend_y))

    points.draw_points()

