"""
BottomUp iterative approach - Tabulation
Time complexity: O(n^2)
Space complexity: O(n)
"""
def canJump(self, nums: List[int]) -> bool:
    n = len(nums)

    table = [False for _ in range(n)]

    if nums[0]==0 and len(nums)>1:
        return False

    #BaseCase
    table[0] = True

    #Check if every position can be reached from any of the previous positions
    for i in range(1,n):
        idx=0
        for j in range(i-1,-1,-1):
            if nums[j]>idx:
                table[i]=True
                break
            idx+=1
        #If any of the positions are not reachable, return False
        if table[i]==False:
            return False

    return True


"""
Greedy Approach
Time complexity: O(n)
Space complexity: O(1)
"""
def canJump(self, nums: List[int]) -> bool:
    n=len(nums)

    last_house=n-1

    #Start from last but one house and  check if it max jump from there take us to last house
    for curr_house in range(n-2,-1,-1):
        if nums[curr_house]+curr_house >=last_house:
            last_house=curr_house
    return last_house==0
