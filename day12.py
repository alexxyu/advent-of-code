'''
0: East
90: North
180: West
270: South
'''

# Part 1
with open('input/day12.txt', 'r') as f:
    lines = f.read().splitlines()

    x = 0
    y = 0
    dir = 0

    for line in lines:
        action = line[0]
        units = int(line[1:])

        if action == 'N':
            y += units
        elif action == 'S':
            y -= units
        elif action == 'W':
            x -= units
        elif action == 'E':
            x += units
        elif action == 'L':
            dir += units
            dir %= 360
        elif action == 'R':
            dir -= units + 360
            dir %= 360
        else:
            if dir == 0:
                x += units
            elif dir == 90:
                y += units
            elif dir == 180:
                x -= units
            else:
                y -= units

        #print(x, y)

    print(abs(x) + abs(y))


# Part 2
import math

def rotate(point, angle):
    """
    Rotate a point counterclockwise by a given angle around (0,0).

    The angle should be given in radians.
    """

    angle *= math.pi / 180
    px, py = point

    qx = math.cos(angle) * (px) - math.sin(angle) * (py) 
    qy = math.sin(angle) * (px) + math.cos(angle) * (py)
    return round(qx), round(qy)

with open('input/day12.txt', 'r') as f:
    lines = f.read().splitlines()

    waypoint_x = 10
    waypoint_y = 1

    x = 0
    y = 0
    dir = 0

    for line in lines:
        action = line[0]
        units = int(line[1:])

        if action == 'N':
            waypoint_y += units
        elif action == 'S':
            waypoint_y -= units
        elif action == 'W':
            waypoint_x -= units
        elif action == 'E':
            waypoint_x += units
        elif action == 'L' or action == 'R':
            if action == 'R':
                units = 360 - units

            waypoint_x, waypoint_y = rotate((waypoint_x, waypoint_y), units)
        else:
            x += (units * waypoint_x)
            y += (units * waypoint_y)

    print(abs(x) + abs(y))
