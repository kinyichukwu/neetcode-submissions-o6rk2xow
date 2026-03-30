class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set = {}
        for n in nums:
            if n in set:
                set[n] = set[n] + 1
            else:
                set[n] = 1
        sortedSet = list(dict(sorted(set.items(), key=lambda item: item[1], reverse=True)))
        return sortedSet[0:k]
        