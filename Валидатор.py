s = input()

def is_valid(s):
    stack = []
    match = {'(':')', '[':']', '{':'}'}
    for c in s:
        if c in ['(','[','{']:
            stack.append(c)
        elif not stack or match[stack.pop()] !=c:
            return False
    
    return not stack

result = is_valid(s)
print(result)