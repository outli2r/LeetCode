class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            key = tuple(sorted(list(s)))
            dic[key].append(s)
        '''
        for s in strs:
            dic[''.join(sorted(s)].append(s)
        '''
        return dic.values()
