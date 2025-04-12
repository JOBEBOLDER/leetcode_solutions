class TrieNode:
    def __init__(self):
        self.children = {} #a: TreeNode
        self.Word = False
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self,word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                #keep doing the next c
            cur = cur.children[c]
        cur.word = True


    def search(self,word:str)->bool:
        def dfs(j,root):
            cur = root

            for i in range(j , len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.value():
                        if dfs(i + 1,child):
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.word
        return dfs(0, self.root)

