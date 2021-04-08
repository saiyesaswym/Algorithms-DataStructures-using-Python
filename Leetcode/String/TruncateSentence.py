"""
First approach: One liner using join and split methods
Time complexity: O(n)
Run time: 28ms
"""
def truncateSentence1(s: str, k: int) -> str:
    return ' '.join(s.split()[:k])

s = "What is the solution to this problem"
k = 4
print(truncateSentence1(s,k))


"""
Second approach: Brute force approach
Looping through the string and stopping at k
Time complexity: O(n)
Run time: 24ms
Faster than 97.04%
"""
def truncateSentence2(s: str, k: int) -> str:
    cnt=0
    ans=''
    for i in s:
        if(i==' '):
            cnt+=1
        if(cnt==k):
            break
        ans=ans+i
    return ans

print(truncateSentence2(s,k))
