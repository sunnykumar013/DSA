class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)

        for s in strs:
            sorted_word = sorted(s)
            string_sorted_word = ('').join(sorted_word)

            dict1[string_sorted_word].append(s)
        print(dict1.values())

        return dict1.values()