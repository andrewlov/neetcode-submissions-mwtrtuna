class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        # tempCountOfLetters = [0] * 26 # a-z
        for string in strs:
            
            tempCountOfLetters = [0] * 26
            for letter in string:
                tempCountOfLetters[ord(letter) - ord('a')] += 1
                #print(tuple(tempCountOfLetters))
            result[tuple(tempCountOfLetters)].append(string)
        return list(result.values())