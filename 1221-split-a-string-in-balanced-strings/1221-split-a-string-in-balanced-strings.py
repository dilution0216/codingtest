class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        answer = 0
        for alpha in s:
            if alpha is "R":
                counter += 1
            else:  # alpha is "L":
                counter -= 1

            if counter == 0:
                answer += 1

        return answer