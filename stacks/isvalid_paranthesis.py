# Is Valid Paranthesis

def is_valid(s):
    stack = []
    hasher = {']': '[', '}': '{', ')': '('}
    for i in s:
        if i in '({[':
            stack.append(i)
        else:
            if not stack or stack[-1] != hasher[i]:
                return False
            stack.pop()
            
    return stack == []

