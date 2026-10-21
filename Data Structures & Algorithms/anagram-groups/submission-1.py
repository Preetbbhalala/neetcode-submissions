class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using hash maps. 

        hmap =defaultdict(list)
        for word in strs:
            count = [0]*26
            for chars in word:
                count[ord(chars)-ord('a')]+=1
            hmap[tuple(count)].append(word)
        return list(hmap.values())