"""
Time complexity: O(n)
Space complexity: O(n)
Runtime: 28ms
Memory: 14.3MB
"""
def isValid(s: str) -> bool:
    bracket_map = {"(":")", "[":"]", "{":"}"}
    stack=[]
    for i in s:
        if i in ('(','[','{'):
            stack.append(i)
        elif stack and i==bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []


print(isValid("((((([])))))"))
