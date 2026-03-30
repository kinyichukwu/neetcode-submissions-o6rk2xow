class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if store.get(nums[i]):
                current = store.get(nums[i])
                store[nums[i]] = current + [i]
            else:
                store[nums[i]] = [i]

        print(store)
        
        for num in nums:
            if target-num == num:
                if len(store[num]) > 1:
                    return [store[num][0], store[num][1]]
                    break
            if target-num in store and target-num != num:
                return [min(store[num][0], store[target-num][0]), max(store[num][0], store[target-num][0])]
                break