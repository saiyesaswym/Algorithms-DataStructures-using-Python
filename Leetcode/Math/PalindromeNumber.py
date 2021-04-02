"""
First approach: Int to String conversion
Reversing string - using slicing in Python - fastest way
Time complexity: O(n)
Run time: 56ms
"""
def isPalindrome(x: int) -> bool:
    return str(x)==str(x)[::-1]


"""
Second approach: Pop and push digits
Without converting integer to String
Run time: 80ms
"""
def isPalindrome2(x: int) -> bool:
    rev = 0
    n = abs(x)
    while n!=0:
        temp = n%10
        n = n//10
        if (rev > (2**31 - 1)/10 or (rev == (2**31 - 1)/10 and pop > 7)): return 0;
        if (rev < (-2**31)/10 or (rev == (-2**31) / 10 and pop < -8)): return 0;
        rev = rev*10 + temp
    if(x==rev):
        return True
    else:
        return False
