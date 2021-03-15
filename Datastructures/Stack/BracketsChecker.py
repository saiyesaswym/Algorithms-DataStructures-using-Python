from Stack import Stack

def bracketsChecker(expr):
    s = Stack()
    balanced = True
    for i in expr:
        if(i in "[{("):
            s.push(i)
        elif(i in "]})"):
            if(s.isEmpty()):
                balanced = False
            else:
                top = s.pop()
                if not matches(top, i):
                    balanced = False

    if(balanced and s.isEmpty()):
        return True
    else:
        return False

def matches(open, close):
    opens = "[{("
    closers = "]})"
    print(opens.find(open))
    print(closers.find(close))
    return opens.find(open) == closers.find(close)

val = input("Enter an expression: ")
print(bracketsChecker(val))
