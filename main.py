
#Dakota Abernathy
#ENPM692-Porj2

import math
import pygame
import time
from random import randint

HEIGHT = 300
WIDTH = 400
SCALE = 2

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

nodes_visited = []
path = []


class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "["+str(self.x)+", "+str(self.y) + "]"

def make_board():
    global board
    pygame.init()
    board = pygame.display.set_mode((int(WIDTH * SCALE), int(HEIGHT * SCALE)))
    pygame.display.set_caption("Path finding algorithm")
    board.fill(WHITE)

    # easy
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


def point_valid(x, y, talk=True):
    if x < 0 or x >= WIDTH:
        if talk:
            print("X is outside of boundary [0,", WIDTH, "]")
        return False
    if y < 0 or y > HEIGHT:
        if talk:
            print("Y is outside of boundary [0,", HEIGHT, "]")
        return False
    if in_obstacle(x, y):
        if talk:
            print("Point is inside an obstacle")
        return False
    return True


def sanity_check():
    for i in range(100000):
        x = randint(0, 400)
        y = randint(0, 300)
        if point_valid(x, y):
            pygame.draw.circle(board, RED, [x * SCALE, (HEIGHT - y) * SCALE], 1 * SCALE)
        else:
            pygame.draw.circle(board, GREEN, [x * SCALE, (HEIGHT - y) * SCALE], 1 * SCALE)
        pygame.display.update()

def get_point_from_user(word):
    valid = False
    while not valid:
        x = int(input("Enter the X coordinate of the "+word+" point: "))
        y = int(input("Enter the Y coordinate of the " + word + " point: "))
        valid = point_valid(x, y, True)
    return x, y


def random_point():
    valid = False
    while not valid:
        x = randint(0, WIDTH)
        y = randint(0, HEIGHT)
        valid = point_valid(x, y, False)
    return x, y


def get_initial_conditions(human=True):
    if human:
        x1, y1 = get_point_from_user("start")
        x2, y2 = get_point_from_user("target")
    else:
        x1, y1 = random_point()
        x2, y2 = random_point()
    return Node(x1, y1, None), Node(x2, y2, None)


def get_neighbors(parent):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if point_valid(parent.x + i, parent.y + j, False):
                new_node = Node(parent.x + i, parent.y + j, parent)
                if new_node in nodes_visited:
                    continue
                neighbors.append(new_node)
    return neighbors

def BFS():
    to_explore = [start]
    while len(to_explore):
        next_node = to_explore.pop(0)
        print(next_node.x, next_node.y)
        pygame.draw.circle(board, GREEN, [next_node.x * SCALE, (HEIGHT - next_node.y) * SCALE], 1 * SCALE)
        pygame.display.update()
        nodes_visited.append(next_node)
        if next_node == target:
            print("Found path")
            return
        new_nodes = get_neighbors(next_node)
        for new_node in new_nodes:
            to_explore.append(new_node)
    print("No path")
    # target has been found

def back_track():
    next = target
    while next != start:
        print(next)
        path.append(next)
        next = next.parent


if __name__ == "__main__":
    start, target = get_initial_conditions()
    make_board()
    BFS()

    pygame.display.update()
    # back track for path
    # display explored nodes and path
    print(path)
    # time.sleep(50)
