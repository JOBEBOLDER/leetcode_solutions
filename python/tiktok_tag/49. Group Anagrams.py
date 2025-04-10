class Solution:
    #space:On
    #time:On*k
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use a dictionary to record the key as the string,and find the same code

        code_to_value = {}
        for s in strs:
            decode = self.encode(s)

            if decode not in code_to_value:
                code_to_value[decode] = []
            code_to_value[decode].append(s)

        res = []
        for value in code_to_value.values():
            res.append(value)
        return res




    def encode(self, s:string):
        code = [0] * 26

        for c in s:
            delta = ord(c) - ord('a')

            code[delta] += 1

        return str(code)