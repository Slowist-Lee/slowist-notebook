# 定义二叉树节点
from typing import Optional, List
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
# 遍历
class Solution:
    def behindtraverse(self,root:Optional[TreeNode]) -> List[int]:
        result=[]
        def traverse(node):
            if node == None:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
        traverse(root)
        return result
def buildTree(a,b):
    if not a or not b:
        return None
    value=a[0]
    root=TreeNode(value)
    root_index=b.index(value) #root's index in the inorder traverse, also the number of the left binary tree 
    root.left=buildTree(a[1:root_index+1],b[:root_index])
    root.right=buildTree(a[root_index+1:],b[root_index+1:])
    return root
cnt=0
result_all=['' for i in range(1000)]
while True:
    try:
        s = input()
        if not s:
            break
        a, b = s.split()
        root = buildTree(a, b)
        solution = Solution()
        result = solution.behindtraverse(root)
        result_all[cnt]="".join(result)
        cnt+=1
    except EOFError:
        break# 定义二叉树节点
from typing import Optional, List
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
# 遍历
class Solution:
    def behindtraverse(self,root:Optional[TreeNode]) -> List[int]:
        result=[]
        def traverse(node):
            if node == None:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
        traverse(root)
        return result
def buildTree(a,b):
    if not a or not b:
        return None
    value=a[0]
    root=TreeNode(value)
    root_index=b.index(value) #root's index in the inorder traverse, also the number of the left binary tree 
    root.left=buildTree(a[1:root_index+1],b[:root_index])
    root.right=buildTree(a[root_index+1:],b[root_index+1:])
    return root
cnt=0
result_all=['' for i in range(1000)]
while True:
    try:
        s = input()
        if not s:
            break
        a, b = s.split()
        root = buildTree(a, b)
        solution = Solution()
        result = solution.behindtraverse(root)
        result_all[cnt]="".join(result)
        cnt+=1
    except EOFError:
        break
for i in range(cnt):
    print(result_all[i])
