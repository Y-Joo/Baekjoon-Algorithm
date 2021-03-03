def ArrayPartition(nums:list[int])->int:
    return sum(sorted(nums)[::2])