s = input()
stack = []
for ch in s:
    if stack and ((stack[-1] == '(' and ch == ')') or (stack[-1] == '[' and ch == ']') or (stack[-1] == '{' and ch == '}')):
        stack.pop()
    else:
        stack.append(ch)

if stack:
    print('no')
else:
    print('yes')
