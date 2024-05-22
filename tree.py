import random

## Node class that encapsulates tree node for more complex tree structures
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.depth = None
        
    def __str__(self):
        return f"Node(value={self.value}, depth={self.depth})"
     
    def __repr__(self):
        pass    

    ## Node properties
    def is_leaf(self):
        return self.left == None and self.right == None

    def is_internal(self):
        return not self.is_leaf()

    def is_root(self):
        return self.depth == 1        
        
    def has_left(self):
        return self.left != None

    def has_right(self):
        return self.right != None

    def has_children(self):
        return self.has_left() or self.has_right()

    def get_children(self):
        return [self.left, self.right]


## Binary Search Tree class encapsulating the basic operations, such as
## insert, delete, search, etc.
class BTree():    
    def __init__(self, root: Node):
        self.root = root
        self.root.depth = 0
        self.height = 0
        self.size = 0
    
    ## Basic insert, delete and visit operations
    ## TODO; parent implementation should be done
    def insert(self, node: Node, verbose=False):        
        if(self.root == None):
            self.root = node
        
        curr = self.root
        depth = 1
        while(curr):
            depth += 1
            if(node.value < curr.value):
                if(curr.left is None):
                    node.depth = depth
                    curr.left = node
                    if(verbose):
                        print(f"Inserting {node} left of {curr}")
                    break
                else:                    
                    curr = curr.left
            else:
                if(curr.right is None):
                    node.depth = depth
                    curr.right = node
                    if(verbose):
                        print(f"Inserting {node} right of {curr}")     
                    break
                else:
                    curr = curr.right

    def rinsert(self, node: Node, curr=None):
        if(self.root is None):
            self.root = node
            return

        if(curr is None):
            curr = self.root

        if(node.value > curr.value):
            if(curr.left is None):
                node.parent = curr
                curr.left = node
            else:
                self.rinsert(node, curr.left)
        else:
            if(curr.right is None):
                node.parent = curr
                curr.right = node
            else:
                self.rinsert(node, curr.right)    
         
    def delete(self, value):
        pass

    def visit(self, node):
        print(node.value)
        return node

    ## Traversal operations
    def inorder(self, visited=[], node=None):
        if(node is None):
            node = self.root

        if(node.left):
            self.inorder(visited, node.left)

        visited.append(node)

        if(node.right):
            self.inorder(visited, node.right)                        
        return visited
    
    def preorder(self, node=None):
        if node is None:
            node = self.root

        self.visit(node)

        if(node.left):
            self.preorder(node.left)

        if(node.right):
            self.preorder(node.right)

    def postorder(self, node=None):
        if node is None:
            node = self.root

        if(node.left):
            self.postorder(node.left)

        if(node.right):
            self.postorder(node.right)
        
        self.visit(node)

    ## Search operation
    def find(self, value):
        pass
    
    ## Calculating tree features using depth-first search
    ## such as height, size, etc.
    def dfs(self, node=None):            
        if(node is None):
            node = self.root

        if(node.left):
            self.dfs(node.left)
            
        if(node.right):
            self.dfs(node.right)        

    ## Calculating tree features using depth-first search
    ## using stack based method instead
    def sdfs(self, node=Node):
        pass

        
    ## Tree properties
    def getHeight(self, node=None, depth=0):            
        if(node is None):
            node = self.root
            depth += 1

        if(node.left):
            self.getHeight(node.left, depth+1)
            
        if(node.right):
            self.getHeight(node.right, depth+1)        
        self.height = max(self.height, depth)
        return self.height       

    def getSize(self, node=None):
        visited = []        
        
        if(node is None):
            node = self.root

        if(node not in visited):
            visited.append(node)
            self.size += 1

        if(node.left):
            self.getSize(node.left)
            
        if(node.right):
            self.getSize(node.right)     
        return self.size   
    
    def getLCA(self, node1, node2):
        if(node1 is None or node2 is None):
            return None

        path1 = self.getPathToRoot(node1, [])
        path2 = self.getPathToRoot(node2, [])
        
        if(path1 is None or path2 is None):
            return None

        lca = None
        minPath = self.getMinPath(path1, path2)
        for i in range(len(minPath)):               
            if(minPath[i] in (path2 and path1)):              
                lca = minPath[i]
                break
        return lca                
    
    def getMinPath(self, path1, path2):
        return path1 if len(path1) < len(path2) else path2

    def getPathToRoot(self, node, path=[]):
        if(node is None):
            return None
        
        path.append(node)        
        
        if(node.parent):
            self.getPathToRoot(node.parent, path)
        
        return path





    def is_balanced(self):
        pass

    def is_complete(self):
        pass

    def is_full(self):
        pass

    def is_perfect(self):
        pass

    def is_symmetric(self):
        pass

    ## Brute force tree balancing operations nodes must be sorted
    def balance(self, nodes=[]):        
        nodes = sorted(nodes)
        
        if not nodes:
            return None

        mid = len(nodes) // 2
        root = Node(nodes[mid])
        root.left = self.balance(nodes[:mid])
        root.right = self.balance(nodes[mid+1:])
        
        return root

    def rebalance(self):
        pass

    ## Tree visualization
    def display(self, root, level=0):
        if(root is None):
            root = self.root
        print(" " * 4 * level, root.data)
        self.display(root.left, level + 1)
        self.display(root.right, level + 1)

    ## Tree comparison
    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    ## Tree serialization
    def serialize(self):
        pass

    def deserialize(self):
        pass


class AVLTree(BTree):
    def __init__(self, root: Node):
        super().__init__(root)


def main():
    tree = BTree(Node(-1))
    
    ## Generating series of random integers to be inserted into the tree
    # for i in range(10):
    #     tree.insert(Node(random.randint(0, 100)), verbose=True)
    
    ## For simplicty for debugging the tranversal, we will use static
    ## values to insert into the tree
    values = [0, 3, -2, 4 ,8]

    ## Inserting above values into tree
    for value in values:
        tree.rinsert(Node(value), tree.root)

    root = tree.root
    lca = tree.getLCA(root.left.left, root.left.left.left)
    print(lca)

    ## Inorder traversal of the tree
    # visited = tree.inorder()
    # tree.balance(visited)
    
    ## Preorder traversal of the tree
    # tree.preorder()

    ## Calculating tree features using depth-first search, getHeight and getSize
    ## methods uses recursive dfs to calculate the height and size of the tree
    # print(f"Tree height: {str(tree.getHeight())}")
    # print(f"Tree size: {str(tree.getSize())}")
    
    ## Displaying the tree
    # tree.display()


if __name__ == "__main__":
    main()

