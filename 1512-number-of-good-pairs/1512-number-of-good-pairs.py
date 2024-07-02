class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 숫자의 빈도를 저장할 딕셔너리
        frequency = defaultdict(int)
        
        # 배열을 순회하며 빈도 계산
        for num in nums:
            frequency[num] += 1
        
        # 좋은 쌍의 수를 계산
        good_pairs = 0
        for count in frequency.values():
            if count > 1:
                good_pairs += count * (count - 1) // 2
        
        return good_pairs