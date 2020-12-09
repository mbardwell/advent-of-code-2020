import re
from pathlib import Path

def dictify(_list):
    ret = []
    for line in _list:
        blah = re.split(' |:', line)
        ret.append({
            "min": int(blah[0].split("-")[0]),
            "max": int(blah[0].split("-")[1]),
            "letter": blah[1],
            "password": blah[3]
            })
    return ret

def solve(list_o_dict):
    valid = 0
    for _dict in list_o_dict:
        count = _dict["password"].count(_dict["letter"])
        if count >= _dict["min"] and count <= _dict["max"]:
            valid += 1
    print(f"the answer is ", valid)

def solve2(list_o_dict):
    # min, max are misnamed here but w/e"
    valid = 0
    for i, _dict in enumerate(list_o_dict):
        _this = 0
        if _dict["password"][_dict["min"]-1] == _dict["letter"]:
            _this += 1
        if _dict["password"][_dict["max"]-1] == _dict["letter"]:
            _this += 1
        if _this == 1:
            valid += 1
    print(f"the answer is ", valid)

def main():
    file = Path("day2.input")
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    list_o_dict = dictify(lines)
    solve(list_o_dict)
    solve2(list_o_dict)

if __name__ == "__main__":
    main()
