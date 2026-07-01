class PrefixTree:

    def __init__(self):
        self.prefixDict = {}

    def insert(self, word: str) -> None:
        self.prefixDict[word] = []

    def search(self, word: str) -> bool:
        if word in self.prefixDict:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for k in self.prefixDict.keys():
            if k.startswith(prefix):
                return True
        return False
        
        