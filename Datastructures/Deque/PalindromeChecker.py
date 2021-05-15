from Deque import Deque

def palindromeChecker(word):
    s = Deque()

    for i in word:
        s.addRear(i)

    while s.size()>1:
        if(s.removeFront()==s.removeRear()):
            pass
        else:
            return False
    return True


val = input("Enter a string: ")
print(palindromeChecker(val))
