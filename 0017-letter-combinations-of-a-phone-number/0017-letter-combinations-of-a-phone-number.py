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
        # Since we have to loop through all digits and then again loop through each letter corresponding to each digit,
        # we will need to use a loop along with recursion.
        def dfs(i: int):
            if len(combination) == len(digits):
                c = "".join(combination)
                if c:
                    result.append(c)
                return

            letters = self.digitToLettersMap.get(digits[i])
            # Take each letter from current digit and search for different combinations in further digits.
            for j in range(len(letters)):
                combination.append(letters[j])
                dfs(i+1)
                # backtrack: deselect the previous choice of letters[j]
                combination.pop()

        dfs(0)
        return result

# Time complexity: O(n * 4^n) - while picking a letter for a digit, we have 4 choices in worst case (case of 7 or 9).
#                               So, number of solutions = number of leaves = 4^height= 4^n.
#                               And for each solution we will have n letters.
# Space complexity: O(n) - for recursion
#                   O(n * 4^n) - for reuslt output
# where n is lenght of digits