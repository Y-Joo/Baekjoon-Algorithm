def IsValid(strs:str)->bool:
    stack=[]
    table={
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    for char in strs:
        if char not in table:
            stack.append(char)
        elif not stack or table[char]!=stack.pop():
            return False
    return len(stack) == 0

