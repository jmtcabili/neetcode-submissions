
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagrams have the same sorted arrangement
        #use same arrangement in as a key with value: [words]

        #define ans map
        ans = defaultdict(list)
        for word in strs:
            #sort letters then join to make string
            key = "".join(sorted(word))

            #add value to key
            ans[key].append(word)

        return list(ans.values()) #return values as list