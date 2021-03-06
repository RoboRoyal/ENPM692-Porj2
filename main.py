
#Dakota Abernathy
#ENPM692-Porj2
import math

import pygame
import time
from random import randint

HEIGHT = 300
WIDTH = 400
SCALE = 1

board = None
start = None
target = None

WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

class node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

def makeBoard():
    global board
    pygame.init()
    board = pygame.display.set_mode((int(WIDTH * SCALE), int(HEIGHT * SCALE)))
    pygame.display.set_caption("Path finding algorithm")
    board.fill(WHITE)

    #
    pygame.draw.circle(board, BLACK, [90 * SCALE, (HEIGHT - 70) * SCALE], 35 * SCALE)
    pygame.draw.ellipse(board, BLACK, [186 * SCALE, (HEIGHT - 175) * SCALE, 120 * SCALE, 60 * SCALE], 0 * SCALE)

    # Line Segment
    pygame.draw.polygon(board, BLACK,
                        [(48 * SCALE, (HEIGHT - 108) * SCALE), (37 * SCALE, (HEIGHT - 124) * SCALE),
                         (159 * SCALE, (HEIGHT - 210) * SCALE), (170 * SCALE, (HEIGHT - 194) * SCALE)])

    # C shape
    pygame.draw.polygon(board, BLACK,  # back
                        [(200 * SCALE, (HEIGHT - 270) * SCALE), (210 * SCALE, (HEIGHT - 270) * SCALE),
                         (210 * SCALE, (HEIGHT - 240) * SCALE), (200 * SCALE, (HEIGHT - 240) * SCALE)])
    pygame.draw.polygon(board, BLACK,  # top
                        [(200 * SCALE, (HEIGHT - 280) * SCALE), (230 * SCALE, (HEIGHT - 280) * SCALE),
                         (230 * SCALE, (HEIGHT - 270) * SCALE), (200 * SCALE, (HEIGHT - 270) * SCALE)])
    pygame.draw.polygon(board, BLACK,  # bottom
                        [(200 * SCALE, (HEIGHT - 240) * SCALE), (230 * SCALE, (HEIGHT - 240) * SCALE),
                         (230 * SCALE, (HEIGHT - 230) * SCALE), (200 * SCALE, (HEIGHT - 230) * SCALE)])

    # Polygon ---- whats the error allowed? lot of rounding and re-rounding
    pygame.draw.polygon(board, BLACK,  # why is this so ugly
                        [(354 * SCALE, (HEIGHT - 138) * SCALE), (380 * SCALE, (HEIGHT - 170) * SCALE),
                         (380 * SCALE, (HEIGHT - 115) * SCALE), (328 * SCALE, (HEIGHT - 63) * SCALE),
                         (286 * SCALE, (HEIGHT - 105) * SCALE), (325 * SCALE, (HEIGHT - 143) * SCALE)])


def in_circle(x, y):
    if math.pow(x - 90, 2) + math.pow(y - 70, 2) >= 1225:
        return False
    return True


def in_ellipse(x, y):
    center_x = 246
    center_y = 146
    horizontal_axis = 60
    vertical_axis = 30
    if ((math.pow(x - center_x, 2) / math.pow(horizontal_axis, 2)) +
        (math.pow(y - center_y, 2) / math.pow(vertical_axis, 2))) <= 1:
        return True
    return False

def in_c_shape(x, y):
    if (x >= 200 and x <= 210 and y <= 280 and y >= 230) or \
        (x >= 210 and x <= 230 and y >= 270 and y <= 280) or \
        (y >= 230 and y <= 240 and x >= 210 and x <= 230):
        return True
    return False

def in_poly(x, y):
    if ((y - 1 * x + 181.6) < 0 and (y + 0.3 * x - 239.9) < 0 and (y + 249.2 * x - 95054.25) <
        0 and (y - x + 265) > 0 and (y + 1 * x - 389.3) > 0) or \
        ((y - 1.13 * x + 260.75) < 0 and (y + 249.2 * x - 95054.25) < 0 and (y + .3 * x - 240.6) > 0):
        return True
    return False


def in_line_segment(x, y):
    if (y + 1.4 * x - 176.5) > 0 and (y - 0.7 * x - 74.4) > 0 \
        and (y - 0.7 * x - 98.8) < 0 and (y + 1.4 * x - 438.1) < 0:
        return True
    return False


def in_obstacle(x, y):
    if in_circle(x, y) or in_ellipse(x, y) or in_c_shape(x, y) or \
            in_line_segment(x, y) or in_poly(x, y):
        return True
    return False


def point_valid(x, y, talk = True):
    if x < 0 or x >= WIDTH:
        if talk:
            print("X is outside of boundary [0,", WIDTH, "]")
        return False
    if y < 0 or y >= HEIGHT:
        if talk:
            print("Y is outside of boundary [0,", HEIGHT, "]")
        return False
    if in_obstacle(x, y):
        if talk:
            print("Point is inside an obstacle")
        return False
    return True

def test_point():
    for i in range(100000):
        x = randint(0,400)
        y = randint(0, 300)
        if point_valid(x, y):
            pygame.draw.circle(board, RED, [x, HEIGHT - y], 1 * SCALE)
        else:
            pygame.draw.circle(board, GREEN, [x, HEIGHT - y], 1 * SCALE)
        pygame.display.update()

if __name__ == "__main__":
    makeBoard()
    pygame.display.update()
    test_point()
    time.sleep(50)