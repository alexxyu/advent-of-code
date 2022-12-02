SCORE_PARENS = 1
SCORE_SQUARE = 2
SCORE_BRACE = 3
SCORE_ANGLE = 4

with open('day10.txt', 'r') as f:
    lines = f.read().splitlines()

    scores = []
    for line in lines:
        stack = []
        is_incorrect = False
        for c in line:
            if c == '(' or c == '[' or c == '{' or c == '<':
                stack.append(c)
            elif (c == ')' and (len(stack) == 0 or stack[-1] != '(')) or \
                 (c == ']' and (len(stack) == 0 or stack[-1] != '[')) or \
                 (c == '}' and (len(stack) == 0 or stack[-1] != '{')) or \
                 (c == '>' and (len(stack) == 0 or stack[-1] != '<')):
                is_incorrect = True
                break
            else:
                stack.pop()

        if not is_incorrect:
            score = 0
            while stack != []:
                p = stack.pop()
                if p == '(':
                    score = (score * 5) + SCORE_PARENS
                elif p == '[':
                    score = (score * 5) + SCORE_SQUARE
                elif p == '{':
                    score = (score * 5) + SCORE_BRACE
                elif p == '<':
                    score = (score * 5) + SCORE_ANGLE
            scores.append(score)
        
    print(sorted(scores)[len(scores)//2])
