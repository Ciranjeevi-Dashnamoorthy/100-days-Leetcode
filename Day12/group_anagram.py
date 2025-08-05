class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)

        for word in strs:
           word1= "".join(sorted(word))
           hashmap[word1].append(word)
        return list(hashmap.values())

        