import argparse

def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()

        max_calories = 0
        curr_calories = 0
        for line in lines:
            if line == '':
                curr_calories = 0
            else:
                curr_calories += int(line)
            max_calories = max(max_calories, curr_calories)

        print(max_calories)

def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()

        calories = []
        curr_calories = 0
        for line in lines:
            if line == '':
                calories.append(curr_calories)
                curr_calories = 0
            else:
                curr_calories += int(line)
        calories.append(curr_calories)

        print(sum(sorted(calories)[-3:]))

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true', help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
