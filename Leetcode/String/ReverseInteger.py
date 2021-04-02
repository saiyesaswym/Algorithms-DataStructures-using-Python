"""
First approach: Int to String conversion
Reversing string - using slicing in Python - fastest way
Time complexity: O(n)
Run time: 28ms
"""
def reverse(x: int):
    if(x<0):
        rev = int('-'+str(abs(x))[::-1])
    else:
        rev = int(str(x)[::-1])

    if(-2**31 <= rev <= 2**31 - 1):
        return rev
    else:
        return 0

x = -123
print(reverse(x))


"""
Second approach: Pop and push digits
Without converting integer to String
Time complexity: O(n)
"""
def reverse(x: int) -> int:
        rev = 0
        n = abs(x)
        while n!=0:
            temp = n%10
            n = n//10
            if (rev > (2**31 - 1)/10 or (rev == (2**31 - 1)/10 and pop > 7)): return 0;
            if (rev < (-2**31)/10 or (rev == (-2**31) / 10 and pop < -8)): return 0;
            rev = rev*10 + temp
        if(x>=0):
            return rev
        else:
            return rev*-1

x = -123
print(reverse(x))
