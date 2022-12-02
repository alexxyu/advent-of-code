SCORE_PARENS = 3
SCORE_SQUARE = 57
SCORE_BRACE = 1197
SCORE_ANGLE = 25137

with open('day10.txt', 'r') as f:
    lines = f.read().splitlines()

    res = 0
    for line in lines:
        stack = []
        for c in line:
            if c == '(' or c == '[' or c == '{' or c == '<':
                stack.append(c)
            elif c == ')' and (len(stack) == 0 or stack[-1] != '('):
                res += SCORE_PARENS
                break
            elif c == ']' and (len(stack) == 0 or stack[-1] != '['):
                res += SCORE_SQUARE
                break
            elif c == '}' and (len(stack) == 0 or stack[-1] != '{'):
                res += SCORE_BRACE
                break
            elif c == '>' and (len(stack) == 0 or stack[-1] != '<'):
                res += SCORE_ANGLE
                break
            else: 
                stack.pop()

    print(res)
