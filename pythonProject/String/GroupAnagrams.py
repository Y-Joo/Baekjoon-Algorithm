import collections
def groupAnagrams(strs:list[str])->list[str]:
    anagram=collections.defaultdict(list)
    for str in strs:
        anagram[''.join(sorted(str))].append(str)
    return anagram.values()
