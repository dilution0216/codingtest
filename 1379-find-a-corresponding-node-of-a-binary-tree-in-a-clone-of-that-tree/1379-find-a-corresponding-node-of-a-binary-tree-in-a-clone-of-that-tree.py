# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(o: TreeNode, c: TreeNode) -> TreeNode:
            if o:
                # original 트리에서 target 노드를 찾으면 cloned 트리의 현재 노드를 반환
                if o == target:
                    return c
                # 왼쪽 자식을 탐색
                left = dfs(o.left, c.left)
                if left:
                    return left
                # 오른쪽 자식을 탐색
                return dfs(o.right, c.right)
            return None

        return dfs(original, cloned)
