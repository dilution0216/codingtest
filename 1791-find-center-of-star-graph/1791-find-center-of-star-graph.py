class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        v1=edges[0][0]
        v2=edges[0][1]
        u1=edges[1][0]
        u2=edges[1][1]
        if v1 == u1 or v1 == u2:
            return v1
        else:
            return v2