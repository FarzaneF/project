class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def pre_order_traversal(node):
    if node:
        print(node.data, end=' ') 
        pre_order_traversal(node.left)  
        pre_order_traversal(node.right) 



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Pre-order traversal: ", end='')
pre_order_traversal(root)

#--------------------------------------------------    
#تابع غیر بازگشتی preorder


def gheire_bazgashti_preorder(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=' ')  
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

