class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash maps. 
        # hmap-> {key:value} pair 

        hmap ={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in hmap and hmap[diff]!=i:
                return [hmap[diff],i]
            hmap[n]=i
        return []
