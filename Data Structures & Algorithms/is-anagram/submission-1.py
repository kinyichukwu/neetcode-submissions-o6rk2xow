class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstSet = {}
        secondSet = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in firstSet:
                    firstSet[s[i]] = firstSet[s[i]] + 1
                else:
                    firstSet[s[i]] = 1

                if t[i] in secondSet:
                    secondSet[t[i]] = secondSet[t[i]] + 1
                else:
                    secondSet[t[i]] = 1

            return firstSet == secondSet
                