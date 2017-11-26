# 734. Sentence Similarity
class Solution:
    def search_in_pair(self, str1, str2, pairs):
        for item in pairs:
            if str1 == item[0] and str2 == item[1]:
                return True
            if str1 == item[1] and str2 == item[0]:
                return True
        return False

    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        len1 = len(words1)
        len2 = len(words2)
        if len1 != len2:
            return False
        for i in range(len1):
            str1 = words1[i]
            str2 = words2[i]
            if str1 != str2:
                in_tag = self.search_in_pair(str1, str2, pairs)
                if not in_tag:
                    return False
        return True


if __name__ == '__main__':
    word1 = [
        ["great", "acting", "skills"],
        ["great", "acting", "11"],
        ["great"],
    ]
    word2 = [
        ["fine", "drama", "talent"],
        ["fine", "drama", "22"],
        ["great"],
    ]
    pairs = [
        [["great", "fine"], ["acting", "drama"], ["skills", "talent"]],
        [["great", "fine"], ["acting", "drama"], ["skills", "talent"]],
        [],
    ]
    output = [
        True,
        False,
        True,
    ]
    for i in range(len(word1)):
        sol = Solution().areSentencesSimilar(word1[i], word2[i], pairs[i])
        print(sol)
        print("solution is right" if sol == output[i] else "solution is wrong")
