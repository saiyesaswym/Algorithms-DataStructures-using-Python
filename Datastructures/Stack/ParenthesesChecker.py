from Stack import Stack

def parChecker(expr):
    s = Stack()
    balanced = True
    for i in expr:
        if(i=='('):
            s.push(i)
        elif(i==')'):
            if(s.isEmpty()):
                balanced = False
            else:
                s.pop()
    
    if(balanced and s.isEmpty()):
        return True
    else:
        return False

val = input("Enter an expression: ")
print(parChecker(val))
