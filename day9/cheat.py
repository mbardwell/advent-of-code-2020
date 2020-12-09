import re
from pathlib import Path

input = []

def sum_of_preamble(n, preamble):
    for i in preamble:
        for j in preamble:
            if i == j:
                continue
            if (i + j) == n:
                return True
    return False

def solve():
    pre_len = 25
    for i in range(len(input)-pre_len):
        if not sum_of_preamble(input[i+pre_len], input[i:i+pre_len]):
            print(input[i+pre_len])
            exit()

def solve2(last_Q_sol):

    def check_and_pop(n1, n2, list_):
        if n1 > n2:
            list_.pop(0)
            check_and_pop(sum(list_), n2, list_)
        return sum(list_), list_

    def verify(list_):
        assert sum(list_) == last_Q_sol

    temp_l = []
    temp_total = 0
    for i in input:
        temp_total += i
        temp_l.append(i)
        temp_total, temp_l = check_and_pop(temp_total, last_Q_sol, temp_l)
        if (temp_total == last_Q_sol) and len(temp_l) > 1:
            verify(temp_l)
            min_ = min(temp_l)
            max_ = max(temp_l)
            print(f"solution {min_+max_}. i: {i}, list: {temp_l}")
            exit()

def main():
    file = Path("day9.input")
    with open(file, 'r') as f:
        for line in f.readlines():
            input.append(int(line.strip()))
    solve2(1309761972)

if __name__ == "__main__":
    main()
