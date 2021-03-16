from Stack import Stack

def decimalToBinary(num):
    s = Stack()
    binstring=''
    ans = num
    while ans!=0:
        s.push(ans%2)
        ans = ans//2

    while not s.isEmpty():
        binstring = binstring + str(s.pop())
    return binstring

val = input("Enter a number: ")
print(decimalToBinary(int(val)))
