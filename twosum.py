
# nums = [2,7,11,15]
# pair = list()
# target = 9

# i=0
# j=0
# for v in nums:
#     for y in nums:
#         tup = (v,y)
#         pair.append(tup)
#         j=j+1
#     i = i+1

# print(pair)

# new_pair = list()
# for key,value in pair:
#     num_1 = int(key)
#     num_2 = int(value)
#     total = num_1 + num_2
#     if total == target:
#         new_tup = (key,value)
#         new_pair.append(new_tup)

# updated_list = list()
# for key,value in new_pair:
#     updated_list.append(key)
#     updated_list.append(value)

# print(updated_list)

# index = list()
# t=0
# for w in updated_list:
#     if w == nums[t]:
#         index.append(t)
#     t = t+1

# print(index)

class Solution(object):
    def twoSum(nums, target):
        pair = list()

        i=0
        j=0
        for v in nums:
            for y in nums:
                tup = (v,y)
                pair.append(tup)
                j=j+1
            i = i+1

        new_pair = list()
        for key,value in pair:
            num_1 = int(key)
            num_2 = int(value)
            total = num_1 + num_2
            if total == target:
                new_tup = (key,value)
                new_pair.append(new_tup)

        updated_list = list()
        for key,value in new_pair:
            updated_list.append(key)
            updated_list.append(value)

        index = list()
        t=0
        for w in updated_list:
            if w == nums[t]:
                index.append(t)
            t = t+1

        print(index)
    
    twoSum([2,7,11,15],9)