import ast
import copy
import math

def explode(sf_num, depth=1):
    # print(sf_num[0], sf_num[1])
    if depth >= 4:
        left, right = None, None
        if isinstance(sf_num[0], list) and isinstance(sf_num[1], int):
            left = sf_num[0][0]
            sf_num[1] += sf_num[0][1]
            sf_num[0] = 0
        if isinstance(sf_num[0], int) and isinstance(sf_num[1], list):
            right = sf_num[1][1]
            sf_num[0] += sf_num[1][0]
            sf_num[1] = 0
        return left, right
    
    if isinstance(sf_num[0], list):
        left, right = explode(sf_num[0], depth+1)
        
        if left:
            return left, right
        if right:
            if isinstance(sf_num[1], int):
                sf_num[1] += right
                return None, None
            return None, right

    if isinstance(sf_num[1], list):
        left, right = explode(sf_num[1], depth+1)

        if left:
            if isinstance(sf_num[0], int):
                sf_num[0] += left
                return None, None
            return left, None
        if right:
            return None, right
    
    return False
            
def split(sf_num):
    if isinstance(sf_num[0], int) and sf_num[0] >= 10:
        sf_num[0] = [math.floor(sf_num[0] / 2), math.ceil(sf_num[0] / 2)]
        return True
    if not isinstance(sf_num[0], list) or not split(sf_num[0]):
        if isinstance(sf_num[1], int) and sf_num[1] >= 10:
            sf_num[1] = [math.floor(sf_num[1] / 2), math.ceil(sf_num[1] / 2)]
            return True
        if isinstance(sf_num[1], list):
            return split(sf_num[1])
    return False

def magnitude(sf_num):
    if isinstance(sf_num, int):
        return sf_num
    
    return 3*magnitude(sf_num[0]) + 2*3*magnitude(sf_num[1])

with open('day18.txt', 'r') as f:
    lines = f.read().splitlines()
    
    line = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
    sf_num = ast.literal_eval(line)

    print(sf_num)
    while True:
        sf_num_next = copy.deepcopy(sf_num)
        while explode(sf_num_next):
            print('after exploding:', sf_num_next)
            pass

        split(sf_num_next)
        print('after splitting:', sf_num_next)

        if sf_num_next == sf_num:
            sf_num = sf_num_next
            break

        sf_num = sf_num_next

    print(magnitude(sf_num))
