class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # 1. nums 배열을 정렬
        nums.sort()
        
        # 2. target 값이 위치한 인덱스를 저장할 리스트
        result = []
        
        # 3. 정렬된 배열을 순회하며 target 값의 인덱스를 찾는다
        for index, value in enumerate(nums):
            if value == target:
                result.append(index)
        
        # 4. 찾은 인덱스를 반환
        return result