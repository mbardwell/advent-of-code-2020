import re
from pathlib import Path

reqs = ['pid', 'eyr', 'hgt', 'hcl', 'iyr', 'byr', 'ecl']
passports = []

def fill_passports(lines):
    pattern = "([a-z]{3}):\S"
    passport = []
    for line in lines:
        if line == "":
            passport_d = {passport[i]: "" for i in range(len(passport))}
            passports.append(passport_d)
            passport = []
        m = re.findall(pattern, line)
        if m:
            passport = m + passport

def check_passport(passport):
    count_it = True
    for req in reqs:
        if req not in passport:
            count_it = False
            break
    return count_it

def check_passports():
    count = 0
    for i, passport in enumerate(passports):
        if check_passport(passport):
            count += 1
    print(count)

def fill_passports2(lines):
    pattern = "([a-z]{3}):(\S+)"
    passport = []
    for line in lines:
        if line == "":
            passport_d = {k:v for (k,v) in passport}
            passports.append(passport_d)
            passport = []
        m = re.findall(pattern, line)
        if m:
            passport = m + passport

reqs2 = ['pid', 'eyr', 'hgt', 'hcl', 'iyr', 'byr', 'ecl']
def check_passports2():
    count = 0
    for i, passport in enumerate(passports):
        count_it = True
        for k, v in passport.items():
            if k == "byr" and not (int(v) >= 1920 and int(v) <= 2002):
                print("byr")
                count_it = False
            if k == "iyr" and not (int(v) >= 2010 and int(v) <= 2020):
                print("iyr")
                count_it = False
            if k == "eyr" and not (int(v) >= 2020 and int(v) <= 2030):
                print("eyr")
                count_it = False
            if k == "hgt":
                if "cm" in v:
                    n = v.split("c")[0]
                    if not (int(n) >= 150 and int(n) <= 193):
                        count_it = False
                        print("hgt cm")
                elif "in" in v:
                    n = v.split("i")[0]
                    if not (int(n) >= 59 and int(n) <= 76):
                        count_it = False
                        print("hgt in")
                else:
                    count_it = False
                    print("hgt no unit")
            if k == "hcl" and not re.match("#[0-9a-f]{6}", v):
                print("hcl")
                count_it = False
            if k == "ecl" and not (v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                print("ecl")
                count_it = False
            if k == "pid" and not re.match("[0-9]{9}", v):
                print("pid")
                count_it = False
            if k not in reqs:
                print(f"k {k}")
                count_it = False
            if not count_it:
                print(f"bad: {i}")
                break
        if count_it and check_passport(passport):
            count += 1
    print(count)

def main():
    file = Path("day4.input")
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    fill_passports2(lines)
    check_passports2()

if __name__ == "__main__":
    main()
