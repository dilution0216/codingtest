# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # 리프 노드인 경우 해당 값을 반환
        if not root.left and not root.right:
            return root.val == 1

        # 왼쪽과 오른쪽 자식 노드를 재귀적으로 평가
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        # 현재 노드가 OR 연산자인 경우
        if root.val == 2:
            return left_val or right_val
        
        # 현재 노드가 AND 연산자인 경우
        if root.val == 3:
            return left_val and right_val

        # 기본적으로 False 반환 (논리적 오류 방지)
        return False
