class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        for string in strs:
            sortedStr = "".join(sorted(string, key=str.lower))
            if sortedStr in sets:
                sets[sortedStr] = sets[sortedStr] + [string]
            else:
                sets[sortedStr] = [string]
        return list(sets.values())
