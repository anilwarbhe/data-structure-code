class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c

b.left = d
b.right = e

c.right = f

def dfs_preorder_traversal(root):
    stack = list()
    preorder = list()
    if root == None: 
        return []
    stack.append(root)        
    while(len(stack) != 0):
        el = stack.pop()
        preorder.append(el.val)
        if el.right != None:
            stack.append(el.right)
        if el.left != None:
            stack.append(el.left)
    print(preorder)

def dfs_postorder_traversal(root):
    stack = list()
    postorder = list()
    if root == None:
        return []
    stack.append(root)
    while(len(stack)!=0):
        el = stack.pop()
        postorder.append(el.val)
        if el.left != None:
            stack.append(el.left)
        if el.right != None:
            stack.append(el.right)
    postorder.reverse()
    print(postorder)

def dfs_inorder_traversal(root):
    stack = list()
    inorder = list()
    if root == None:
        return []
    stack.append(root)
    while(len(stack)!=0):
        while root.left != None:
            stack.append(root.left)
            root = root.left
        el = stack.pop()    
        inorder.append(el)
        if el.right != None:
            el = el.right
    return inorder

def dfs_preorder_traversal_rec(root):
    if root ==  None:
        return []
    leftValues = dfs_preorder_traversal_rec(root.left)
    rightValues = dfs_preorder_traversal_rec(root.right)
    return [root.val] + leftValues + rightValues

def dfs_postorder_traversal_rec(root):
    if root ==  None:
        return []
    leftValues = dfs_postorder_traversal_rec(root.left)
    rightValues = dfs_postorder_traversal_rec(root.right)
    return [root.val] + leftValues + rightValues

# dfs_preorder_traversal(a)
# print(dfs_preorder_traversal_rec(a))

def dfs_inorder_traversal_rec(root):
    if root == None:
        return []
    leftValues = dfs_inorder_traversal_rec(root.left)
    rightValues = dfs_inorder_traversal_rec(root.right)
    return leftValues + [root.val] + rightValues       

def dfs_postorder_traversal_rec(root):
    if root == None:
        return []
    leftValues = dfs_postorder_traversal_rec(root.left)
    rightValues = dfs_postorder_traversal_rec(root.right)
    return leftValues  + rightValues + [root.val]  
    
print("####### PREORDER DFS TRAVERSAL #########")
print(dfs_preorder_traversal_rec(a))
print("Without REcursion")
dfs_preorder_traversal(a)
print("####### INORDER DFS TRAVERSAL #########")
print(dfs_inorder_traversal_rec(a))
print("Without REcursion")
dfs_inorder_traversal(a)
print("####### POSTORDER DFS TRAVERSAL #########")
print(dfs_postorder_traversal_rec(a))
print("Without REcursion")
dfs_postorder_traversal(a)