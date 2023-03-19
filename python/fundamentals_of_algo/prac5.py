class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
def inorder(root):
        if root is not None:
            inorder(root.left)
            print(root.key)
            inorder(root.right)
            
def insert(node,key):
        if node is None:
            return Node(key)
        if key<node.key:
            node.left=insert(node.left,key)
        else:
            node.right=insert(node.right,key)
        return node
    
def minval(node):
        cur=node
        while(cur.left is not None):
            cur=cur.left
        return cur
def delete(root,key):
        if root is None:
            return root
        if key<root.key:
            root.left=delete(root.left,key)
        elif key>root.key:
            root.right=delete(root.right,key)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            temp=minval(root.right)
            root.key=temp.key
            root.right=delete(root.right,temp.key)
        return root
            
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)

print("inorder!!!!")
inorder(root)
print("Delete 20 !!!!!!!!!")
root=delete(root,20)
inorder(root)

        
