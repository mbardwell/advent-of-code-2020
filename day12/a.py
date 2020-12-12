import re
from pathlib import Path

ship_dir = "E"
ship_pos = [0,0]
abs_truth = {"N": 0, "E": 90, "S": 180, "W": 270}
abs_truth_ = {0: "N", 90: "E", 180: "S", 270: "W"}

def update_ship_dir(LorR, value):
    global ship_dir
    rot = 1
    if LorR is "L":
        rot *= -1
    current_direction = abs_truth[ship_dir]
    new_dir = (current_direction + (rot*value)) % 360
    ship_dir = abs_truth_[new_dir]

def move_ship_(NESW, value):
    global ship_pos
    if NESW is "N":
        ship_pos[1] += value
    elif NESW is "E":
        ship_pos[0] += value
    elif NESW is "S":
        ship_pos[1] -= value
    elif NESW is "W":
        ship_pos[0] -= value
    else:
        print(f"Error! move_ship_ {NESW}"); exit()

def move_ship(instr_and_value):
    global ship_pos
    global ship_dir
    instr = instr_and_value[0]
    value = instr_and_value[1]
    if instr in "LR":
        update_ship_dir(instr, value)
    elif instr in "NESW":
        move_ship_(instr, value)
    elif instr in "F":
        move_ship_(ship_dir, value)
    else:
        print(f"Error! move_ship {instr}"); exit()

def solve(list_):
    for instruction in list_:
        move_ship(instruction)
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