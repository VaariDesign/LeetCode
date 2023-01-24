class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits) == 0):
            return []

        digit2char = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}

        result = ['']

        for d in digits:
            tem = []
            for c in digit2char[d]:
                tem = tem + [r + c for r in result]

            result = tem

        return result
        
