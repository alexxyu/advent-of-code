# Part 1
cnt = 0
with open('input/day6.txt', 'r') as f:
    lines = f.readlines()
    i = 0

    while i < len(lines):
        questions = set()
        while i < len(lines) and lines[i] != "\n":
            for c in lines[i]:
                if c != '\n':
                    questions.add(c)
            i += 1

        cnt += len(questions)
        i += 1

print(cnt)

# Part 2
cnt = 0
with open('input/day6.txt', 'r') as f:
    lines = f.readlines()
    i = 0

    while i < len(lines):
        questions = set()
        for c in lines[i]:
            if c != '\n':
                questions.add(c)
        i += 1

        tmp = questions.copy()
        while i < len(lines) and lines[i] != "\n":
            for c in tmp:
                if c not in lines[i] and c in questions:
                    questions.remove(c)
            i += 1

        cnt += len(questions)
        i += 1

print(cnt)
