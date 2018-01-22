class RBNode(object):
    def __init__(self, key, color='b', value=None, left=None, right=None, parent=None):
        self.key=key
        self.color=color
        self.value=value
        self.left=left
        self.right=right
        self.parent=parent

class RBTree(object):
    def __init__(self, root=None):
        self.root=root

    def insert(self, node):
        y=None
        x=self.root
        while x is not None:
            y=x
            if node.key < x.key:
                x=x.left
            else:
                x=x.right
        node.parent=y
        if y == None:
            self.root=node
        elif node.key < y.key:
            y.left=node
        else:
            y.right=node
        node.left=None
        node.right=None
        node.color='r'
        insertFixup(self, node)

    def insertFixup(self, node):
        while node.parent.color=='r':
            if node.parent == node.parent.parent.left
                y=node.parent.parent.right
                if y.color='r':
                    node.parent.color='b'
                    y.color='b'
                    node.parent.parent.color='r'
                    node=node.parent.parent
                else if node=node.parent.right:
                        node=node.parent
                        leftRotate(self, node)
                    node.parent.color='b'
                    node.parent.parent.colot='r'
                    rightRotate(self, node.parent.parent)
                else:
                    y=node.parent.parent.left
                    if y.color='r':
                        node.parent.color='b'
                        y.color='b'
                        node.parent.parent.color='r'
                        node=node.parent.parent
                    else if node=node.parent.left
                            node=node.parent
                            leftRotate(self, node)
                        node.parent.color='b'
                        node.parent.parent.colot='r'
                        rightRotate(self, node.parent.parent)
        self.root.color='b'
def main():
        nodeRoot = RBNode(20)
        node = RBNode(5)
        tree = RBTree(nodeRoot)

        tree.insert(nodeRoot)
        tree.insert(node)

main()
