def twoSum(nums, target):
    
    nums_len = len(nums)
    #main loop
    for item in range(nums_len):
        #inner loop
        for item2 in range(item+1, nums_len):
            #condition check
            if nums[item] + nums[item2] == target :
                
                return [item,item2]

'''
Input 
[1,20,15,20]
40

Output
[1,3]

'''

#code by santhoshGoku
