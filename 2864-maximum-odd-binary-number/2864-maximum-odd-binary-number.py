class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Step 1: '1'의 개수 세기
        count_1 = s.count('1')
        
        # Step 2: '0'의 개수 세기
        count_0 = len(s) - count_1
        
        # Step 3: 새로운 문자열 구성
        # (count_1 - 1)개의 '1'을 앞에 배치하고, '0'들을 중간에 배치하고, 마지막에 '1'을 배치
        result = '1' * (count_1 - 1) + '0' * count_0 + '1'
        
        return result