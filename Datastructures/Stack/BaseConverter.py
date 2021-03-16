from Stack import Stack

def decimalToBinary(num, base):
    s = Stack()
    digits = "0123456789ABCDEF"
    binstring=''
    ans = num
    while ans!=0:
        s.push(ans%base)
        ans = ans//base

    while not s.isEmpty():
        binstring = binstring + digits[s.pop()]
    return binstring

val1 = input("Enter a number: ")
val2 = input("Enter a base: ")
print(decimalToBinary(int(val1), int(val2)))
