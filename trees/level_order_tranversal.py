from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        while queue:
            lvl = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node: 
                    lvl.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            if len(lvl) > 0: res.append(lvl)
        return res
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        lvls = []

        def helper(root, lvl):
            if root == None: return
            
            if len(lvls) == lvl:
                lvls.append([])
            lvls[lvl].append(root.val)

            if root.left: helper(root.left, lvl + 1)
            if root.right: helper(root.right, lvl + 1)

        helper(root, 0)
        return lvls