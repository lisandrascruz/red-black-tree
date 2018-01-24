from enum import Enum

class Color(Enum):
    BLACK = "Black Node"
    RED = "Red Node"

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
        if y.left is not None:
            y.left.parent=node
        y.parent=node.parent #define o parent da raiz e nulo, pois x e raiz e raiz nao tem pai
        if node.parent == None:
            self.root=y
        elif node == node.parent.left:
            node.parent.left=y
        else:
            node.parent.right=y
        y.left=node
        node.parent=y

    def rightRotate(self, node):
        y=node.left #define Y
        node.left=y.right #transformar a subarvore da direita de Y na esquerda de X
        if y.right is not None:
            y.right=node
        y.parent=node.parent #define o parent da raiz e nulo, pois x e raiz e raiz nao tem pai
        if node.parent == None:
            self.root=y
        elif node == node.parent.right:
            node.parent.right=y
        else:
            node.parent.left=y
        y.right=node
        node.parent=y

    def insertNode(self,node):
        y=None
        nodeRoot=self.root
        while nodeRoot is not None: #para quando a raiz for conhecida
            y=nodeRoot
            if node.key < nodeRoot.key:
                nodeRoot=nodeRoot.left
            elif node.key > nodeRoot.key:
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
        node.color= Color.RED;
        # print "the insert: "
        # self.show(node)
        self.insertFixupNode(node)

    def insertFixupNode(self, node):
        while node.parent is not None and node.parent.color==Color.RED: #enquanto o pai do no tiver a cor vermelha
            grandFatherNode=node.parent.parent #avo do no
            if node.parent == grandFatherNode.left:
                y=grandFatherNode.right
                if y.color==Color.RED:
                    node.parent.color=Color.BLACK
                    y.color=Color.BLACK
                    grandFatherNode.color=Color.RED
                    node=grandFatherNode
                elif node==node.parent.right:
                    node=node.parent
                    # print 'left rotate'
                    # self.show(node)
                    self.leftRotate(node)
                else:
                    node.parent.color=Color.BLACK
                    grandFatherNode.color=Color.RED
                    self.rightRotate(grandFatherNode)
            else:
                y=grandFatherNode.left
                if y.color==Color.RED:
                    node.parent.color=Color.BLACK
                    y.color=Color.BLACK
                    grandFatherNode.color=Color.RED
                    node=grandFatherNode
                elif node==node.parent.left:
                    node=node.parent
                    # print 'right rotate'
                    # self.show(node)
                    self.rightRotate(node)
                else:
                    node.parent.color=Color.BLACK
                    grandFatherNode.color=Color.RED
                    self.leftRotate(grandFatherNode)
        self.root.color=Color.BLACK

    def show(self, node):
        print "No: "+str(node.key)
        print "Cor: "+str(node.color.value)
        if node.parent is not None:
            print "Pai: "+str(node.parent.key)
        if node.right is not None:
            print "Filho direito: "+str(node.right.key)
        if node.left is not None:
            print "Filho esquerdo: "+str(node.left.key)+"\n"
        print "------------------"
def main():
    #nos
    rootNode=RBNode(20)
    rightNode = RBNode(30)
    rightNode2 = RBNode(25)
    leftNode = RBNode(10)
    leftNode2 = RBNode(12)


    #arvores
    tree = RBTree()

    #inserir nos nas arvores
    tree.insertNode(rootNode)
    tree.insertNode(leftNode)
    tree.insertNode(rightNode)
    tree.insertNode(rightNode2)
    tree.insertNode(leftNode2)
    tree.show(rightNode)
    tree.show(rightNode2)
    tree.show(leftNode)
    tree.show(rootNode)
    tree.show(leftNode2)

    #testando
    # tree.show(rootNode)
    # tree.show(leftNode)
    # tree.show(rightNode)
    # tree.show(rightNode2)
    # print "No: "+str(rootNode.key)
    # print "Cor: "+str(rootNode.color.value)
    # print "Pai: "+str(rootNode.parent)
    # print "Filho direito: "+str(rootNode.right.key)
    # print "Filho esquerdo: "+str(rootNode.left.key)+"\n"
    #
    # print "No: "+str(leftNode.key)
    # print "Cor: "+str(leftNode.color.value)
    # print "Pai: "+str(leftNode.parent.key)
    # print "Filho direito: "+str(leftNode.right)
    # print "Filho esquerdo: "+str(leftNode.left)+"\n"
    #
    # print "No: "+str(rightNode.key)
    # print "Cor: "+str(rightNode.color.value)
    # print "Pai: " +str(rightNode.parent.key)
    # print "Filho direito: "+str(rightNode.right)
    # print "Filho esquerdo: "+str(rightNode.left.key)+"\n"
    #
    # print "No: "+str(rightNode2.key)
    # print "Cor: "+str(rightNode2.color.value)
    # print "Pai: " +str(rightNode2.parent.key)
    # print "Filho direito: "+str(rightNode2.right)
    # print "Filho esquerdo: "+str(rightNode2.left)+"\n"
main()
