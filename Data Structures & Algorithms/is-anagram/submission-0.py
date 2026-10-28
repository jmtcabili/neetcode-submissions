class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #map entries of all chars

        #if diff lenght return false
        if (len(s) != len (t)):
            return False

        map1 = {}
        map2 = {}
        for char in s:
            if char in map1:
                map1[char]+=1
            else:
                map1[char] = 0
        for char in t:
            if char in map2:
                map2[char]+=1
            else:
                map2[char] = 0
        return map1 == map2
        
        

