from enum import Enum

class Color(Enum):
    BLACK=0
    RED=1

class RBNode(object):
    def __init__(self, key, color=Color.BLACK, value=None, left=None, right=None, parent=None):
        self.key=key
        self.color=color
        self.value=value
        self.left=left
        self.right=right
        self.parent=parent

class RBTree(object): #este object sera um node
    def __init__(self, root=None):
        self.root=root

    def leftRotate(self, node):
        y=node.right #define Y
        node.right=y.left #transformo a subarvore a esquerda de x na direita de Y
        if y.left == None:
            y.left.parent=node
        y.parent=node.parent #define o parent da raiz e nulo, pois x e raiz e raiz nao tem pai
        if node.parent == None:
            self.root=y
        elif node == self.fatherNode.left:
            node.parent.left=y
        else:
            node.parent.right=y
        y.left=node
        node.parent=y

    def rightRotate(self, node):
        y=node.left #define Y
        node.right=y.left #transformar a subarvore da direita de Y na esquerda de X
        if y.left == None:
            y.left=node
        y.parent=node.parent #define o parent da raiz e nulo, pois x e raiz e raiz nao tem pai
        if node.parent == None:
            self.root=y
        elif node == self.fatherNode.right:
            node.parent.right=y
        else:
            node.parent.left=y
        y.right=node
        node.parent=y

    def insert(self, node):
        y=None
        nodeRoot =self.root
        while nodeRoot is not None: #para quando a raiz for conhecida
            y=nodeRoot
            if node.key < nodeRoot.key:
                nodeRoot=nodeRoot.left
            elif node.key < nodeRoot.key:
                nodeRoot=nodeRoot.right
            else:
                 return None
        node.parent=y
        if y == None:
            self.root=node
        elif node.key < y.key:
            y.left=node
        else:
            y.right=node
        node.left=None
        node.right=None
        node.color= Color.BLACK;
        #insertFixup(node)

    def insertFixup(self, node):
        while node.parent.color==Color.RED:
            #if node.parent == node.parent.parent.left
            if node.parent == node.parent.parent.left:
                #y=node.parent.parent.right
                y=self.grandParentsNode.right
                if y.color==Color.RED:
                    node.parent.color==Color.BLACK
                    y.color==Color.BLACK
                    node.parent.parent.color==Color.RED
                    node=node.parent.parent
                elif node==node.parent.right:
                    node=node.parent
                    leftRotate(self, node)
                node.parent.color==Color.BLACK
                node.parent.parent.colo==Color.RED
                rightRotate(self, node.parent.parent)
                else:
                    y=node.parent.parent.left
                    if y.color==Color.RED:
                        node.parent.color==Color.BLACK
                        y.color==Color.BLACK
                        node.parent.parent.color==Color.RED
                        node=node.parent.parent
                    else if node=node.parent.left
                            node=node.parent
                            leftRotate(self, node)
                        node.parent.color==Color.BLACK
                        node.parent.parent.colot==Color.RED
                        rightRotate(self, node.parent.parent)
        self.root.color==Color.BLACK


def main():
    print "Arvore:"
    tree = RBTree()
    rootNode = RBNode(20)
    tree.insert(node=rootNode)
    print tree.root.key
    print tree.root.color

    leftNode = RBNode(10)
    tree.insert(node=leftNode)
    print leftNode.key
    print leftNode.color

    # tree.insert(RBNode(10))
    # tree.insert(RBNode(30))
    # print tree.root.key, tree.root.color

main()
