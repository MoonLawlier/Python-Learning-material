def removeDuplicates(nums):
    for i,val in enumerate(nums):
        if nums.count(val) > 1:
            nums.remove(val)
            i += 1
        else:
            continue
    return nums