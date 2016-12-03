#!/usr/bin/env python

"""bezier.py: Magical bezier curve generation"""

import math

__author__ = "Wesley Soo-Hoo"
__license__ = "MIT"


def bezier(points, t):
    if len(points) == 1:
        return points[0]
    else:
        return (1-t)*bezier(points[:-1], t) + t*bezier(points[1:], t)


if __name__ == '__main__':

    x0, y0 = 0, 0
    x1, y1 = 0, .25
    x2, y2 = 1, .75
    x3, y3 = 1, 1

    f = "t\tx(t)\ty(t)\tTheta\n"

    t = 0.0
    x, y = -x1, -y1
    theta = (-(math.atan2((y1-y0), (x1-x0)) * (180/math.pi) - 90) + 360) % 360
    while True:
        # Update last x and last y
        last_x = x
        last_y = y

        # calculate the x and y cords
        # NOTE: t is NOT time. It is just a variable used to link the parametric equations x(t) and y(t)
        x = bezier([x0, x1, x2, x3], t)
        y = bezier([y0, y1, y2, y3], t)

        # calculate angle
        theta = (-(math.atan2((y - last_y), (x - last_x)) * (180 / math.pi) - 90) + 360) % 360

        f += str(t) + "\t" + str(x) + "\t" + str(y) + "\t" + str(theta) + "\n"
        if abs(x-x3) + abs(y-y3) < .0001 or t > 10:
            break
        t += .01

open("../tests/bezier.txt", 'w').write(f)
