import re
from pathlib import Path

input = []

def jolts(starting=0):
    sorted = list.copy(input)
    sorted.sort()
    diff = {1:0, 2:0, 3:1}
    diff[sorted[0]-starting] += 1
    for i in range(1,len(sorted)):
        diff[sorted[i]-sorted[i-1]] += 1
    print(diff[1]*diff[3])

def jolts2():
    sorted = list.copy(input)
    sorted.sort()
    sorted = [0] + sorted + [max(sorted)+3]
    possible=[1,2,3]
    diff = {}
    for i in sorted:
        diff[i] = []
        for j in possible:
            if (i+j) in sorted:
                diff[i].append(j)

    sol=0
    for k,v in diff.items():
        if len(v) in [2,3]:
            sol += 2**(len(v)-1)
    print(sol)


def main():
    file = Path("test2.input")
    with open(file, 'r') as f:
        for line in f.readlines():
            input.append(int(line.strip()))
    jolts2()

if __name__ == "__main__":
    main()


def jolts2(starting=0):
    def valid_next(list_o_four):
        diff = {1:0, 2:0, 3:0}
        for i in list_o_four[1:]:
            temp=(i - list_o_four[0])
            if temp in [1,2,3]:
                diff[temp] = 1
        print(f"{list_o_four[0]}: {diff}")

    sorted = list.copy(input)
    sorted.sort()
    valid_next([0]+sorted[:3])
    for i in range(len(sorted)-4):
        valid_next(sorted[i:i+4])
    valid_next(sorted[-2:]+[(sorted[-1]+3)])