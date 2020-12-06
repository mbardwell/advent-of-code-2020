import re
from pathlib import Path

def to_matrix(_list):
    ret = []
    for line in _list:
        new_line = 120*line
        ret.append(new_line)
    return ret

def traverse(_list, xhop, yhop):
    x = 0
    y = 0
    trees = 0
    try:
        while True:
            if _list[y][x] == "#":
                trees += 1
            x += xhop
            y += yhop
    except Exception as e:
        print("I hit {} trees. Exc: {}, x: {}, y: {}".format(trees, e, x, y))
    return trees

def main():
    file = Path("day3.input")
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    list_o_dict = to_matrix(lines)
    v = 1
    for a,b in ((1,1), (3,1), (5,1), (7,1), (1,2)):
        print("a: {}, b: {}".format(a,b))
        v *= traverse(list_o_dict, a, b)
    print(v)

if __name__ == "__main__":
    main()
