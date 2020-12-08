import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
VALID_ECL = ['amb','blu','brn','gry','grn','hzl','oth']

# Part 1
cnt = 0
with open('input/day4.txt', 'r') as f:
    lines = f.readlines()
    i = 0

    while i < len(lines):
        present_fields = set()

        while i < len(lines) and lines[i] != "\n":
            entries = lines[i].split()
            for entry in entries:
                field = entry.split(':')[0]
                present_fields.add(field)
            i += 1

        has_all = True
        for f in REQUIRED_FIELDS:
            if f not in present_fields:
                has_all = False
                break

        if has_all:
            cnt += 1
        i += 1

print(cnt)

# Part 2
'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
'''

cnt = 0
with open('input/day4.txt', 'r') as f:
    lines = f.readlines()
    i = 0

    while i < len(lines):
        present_fields = dict()

        while i < len(lines) and lines[i] != "\n":
            entries = lines[i].rstrip().split()
            for entry in entries:
                field, value = entry.split(':')
                present_fields[field] = value
            i += 1

        has_all = True
        for f in REQUIRED_FIELDS:
            if f not in present_fields.keys():
                has_all = False
                break

        if has_all:
            hgt_units = present_fields['hgt'][-2:]
            try:
                hgt_val = int(present_fields['hgt'][:-2])
            except:
                hgt_val = 0

            if hgt_units != 'cm' and hgt_units != 'in':
                pass
            elif int(present_fields['byr']) < 1920 or int(present_fields['byr']) > 2002:
                pass
            elif int(present_fields['iyr']) < 2010 or int(present_fields['iyr']) > 2020:
                pass
            elif int(present_fields['eyr']) < 2020 or int(present_fields['eyr']) > 2030:
                pass
            elif (hgt_units == 'cm' and (hgt_val < 150 or hgt_val > 193)) or (hgt_units == 'in' and (hgt_val < 59 or hgt_val > 76)):
                pass
            elif not re.search('^#([0-9]|[a-f]){6}$', present_fields['hcl']):
                pass
            elif present_fields['ecl'] not in VALID_ECL:
                pass
            elif not re.search('^[0-9]{9}$', present_fields['pid']):
                pass
            else:
                cnt += 1

        i += 1

print(cnt)