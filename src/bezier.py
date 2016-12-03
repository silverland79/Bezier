#!/usr/bin/env python

"""bezier.py: Magical bezier curve generation"""

import math

__author__ = "Wesley Soo-Hoo"
__license__ = "MIT"


def linear(p0, p1, t):
    return (1-t)*p0 + t*p1


def quadratic(p0, p1, p2, t):
    return (1-t)*(linear(p0, p1, t)) + t*(linear(p1, p2, t))


def cubic(p0, p1, p2, p3, t):
    return (1-t)*(quadratic(p0, p1, p2, t)) + t*(quadratic(p1, p2, p3, t))


if __name__ == '__main__':

    x0, y0 = 0, 0
    x1, y1 = 0, .25
    x2, y2 = 1, .75
    x3, y3 = 1, 1

    print("t\tx(t)\ty(t)\tTheta")

    t = 0.0
    x, y = -x1, -y1
    theta = (-(math.atan2((y1-y0), (x1-x0)) * (180/math.pi) - 90) + 360) % 360
    while True:
        # Update last x and last y
        last_x = x
        last_y = y

        # calculate the x and y cords
        # NOTE: t is NOT time. It is just a variable used to link the parametric equations x(t) and y(t)
        x = cubic(x0, x1, x2, x3, t)
        y = cubic(y0, y1, y2, y3, t)

        # calculate angle
        theta = (-(math.atan2((y - last_y), (x - last_x)) * (180 / math.pi) - 90) + 360) % 360

        print(str(t) + "\t" + str(x) + "\t" + str(y) + "\t" + str(theta))
        if abs(x-x3) + abs(y-y3) < .0001 or t > 10:
            break
        t += .01
