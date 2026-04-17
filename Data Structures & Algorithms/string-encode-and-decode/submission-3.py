class Solution:
    def __init__(self):
        self.sentence_dict = {}

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i, sentence in enumerate(strs):
            self.sentence_dict[i] = len(sentence)
            s += sentence + " "
        return s

        

    def decode(self, s: str) -> List[str]:
        to_list = []
        for space in self.sentence_dict.values():
            to_list.append(s[:space])
            s = s[space+1:]

        return to_list
        

        
