from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]: # YOUR ANSWER
    length_of_list = len(nums)
    answer_i = 0
    answer_j = 0
    finish = 0
    for i in range(length_of_list):
        for j in range(length_of_list):
            if (i==j):
                continue
            if(nums[i]+nums[j] == target):
                answer_i = i
                answer_j = j
                finish = 1
        if(finish==1):
            break
                

    return [answer_i, answer_j]