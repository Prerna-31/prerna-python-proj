"""
Hypothesis: height(root)  --->  returns the height from root.
            height(root->left)    ---> returns the height for left subtree.
            height(root->right)  --> returns the height for right subtree.
Induction: if max(leftsubtree's, rightsubTree's) height is h, height of tree would be h + 1(adding root)
Base Condition: if root=null , height will be 0.
"""
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def get_height(root):
    if(root == None):
        return 0

    lheight = get_height(root.left)
    rheight = get_height(root.right)

    return(1 + max(lheight, rheight))

if(__name__ == '__main__'):
    root = Node(12)
    root.left = Node(10)
    root.right = Node(16)
    root.left.left = Node(4)
    root.left.right = Node(7)
    root.right.left = Node(13)
    root.right.left.right = Node(20)

    print(get_height(root))