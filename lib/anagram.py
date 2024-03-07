# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        for candidate in word_list:
            if self.is_anagram(candidate.lower()):
                matches.append(candidate)
        return matches

    def is_anagram(self, candidate):
        return sorted(self.word) == sorted(candidate) and self.word != candidate
