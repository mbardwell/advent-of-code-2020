import math
from pathlib import Path

ship_pos = [0,0]
waypoint = [10,1]
rot_matrix = [[math.cos, math.sin], [math.sin, math.cos]]

def matmul(A,B,value_rad):
    return list(map(round, [(B[0]*A[0][0](value_rad) - B[1]*A[0][1](value_rad)), (B[0]*A[1][0](value_rad) + B[1]*A[1][1](value_rad))]))

def rotate_waypoint_(LR, value):
    if LR in "LR":
        global waypoint
        value_rad = value * math.pi / 180
        if LR is "R":
            value_rad *= -1
        waypoint = matmul(rot_matrix, waypoint, value_rad)

def move_waypoint_(NESW, value):
    global waypoint
    if NESW is "N":
        waypoint[1] += value
    elif NESW is "E":
        waypoint[0] += value
    elif NESW is "S":
        waypoint[1] -= value
    elif NESW is "W":
        waypoint[0] -= value

def move_ship_(F, value):
    global waypoint
    global ship_pos
    if F in "F":
        for _ in range(value):
            ship_pos[0] += waypoint[0]
            ship_pos[1] += waypoint[1]

def solve(list_):
    for instr, value in list_:
        rotate_waypoint_(instr, value)
        move_waypoint_(instr, value)
        move_ship_(instr, value)
        print(ship_pos, waypoint)
    print(f"Solution: {ship_pos}. Manhattan distance: {abs(ship_pos[0]) + abs(ship_pos[1])}")

def main():
    file = Path("day12.input")
    input = []
    with open(file, 'r') as f:
        for line in f.readlines():
            input.append((line[0], int(line[1:])))
    solve(input)

if __name__ == "__main__":
    main()