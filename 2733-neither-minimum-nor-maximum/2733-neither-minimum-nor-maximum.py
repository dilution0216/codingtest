class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # 배열의 길이가 2 이하인 경우 최소값과 최대값을 제외한 요소가 없으므로 -1 반환
        if len(nums) <= 2:
            return -1
        
        # 배열에서 최소값과 최대값을 찾음
        min_val = min(nums)
        max_val = max(nums)
        
        # 최소값과 최대값이 아닌 요소를 탐색
        for num in nums:
            if num != min_val and num != max_val:
                return num
        
        # 조건에 맞는 요소가 없을 경우 -1 반환
        return -1        