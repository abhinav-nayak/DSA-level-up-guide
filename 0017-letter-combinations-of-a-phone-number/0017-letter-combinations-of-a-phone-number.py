class Solution:
    def __init__(self):
        # create a hash map to map each digit with letters
        self.digitToLettersMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        # Since we have to find 'all possible' combinations, we can use backtracking
        result = []

        combination = []
        def dfs(i: int):
            if len(combination) == len(digits):
                c = "".join(combination)
                if c:
                    result.append(c)
                return

            letters = self.digitToLettersMap.get(digits[i])
            for j in range(len(letters)):
                combination.append(letters[j])
                dfs(i+1)
                combination.pop()

        
        dfs(0)
        return result
        