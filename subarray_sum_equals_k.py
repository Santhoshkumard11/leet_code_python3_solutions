def subarraySum(nums, k) -> int:
    number_of_occurrence = 0
    length = len(nums)

    nums.sort()

    #early removal
    locate_k = nums.count(k)

    if locate_k != 0:
        nums = nums[0:nums.index(k)+1]

    #main loop
    for index,item in enumerate(nums) :
        
        for i in range(index , length+1):

            temp_sum = sum(nums[index:i])

            if temp_sum == k:

                number_of_occurrence += 1            

    return number_of_occurrence


'''
Input 
[1,2,1,2,1]
3

Output
4
'''
