from array import *

'''def show(arr):
    for i in arr:
        print(i, end=', ')

arr = array('i', [16, 27, 77, 71, 70,
                  75, 48, 19, 110])
show(arr)'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list=dict()
        for num in nums:
            if not num in num_list:
                num_list[num]=1
            else:
                num_list[num]+=1
        return max(num_list, key=num_list.get)

    majorityElement( nums= ['2','3','4','5','6','6','6','7'])

