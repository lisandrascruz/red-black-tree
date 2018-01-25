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
    #rotaciona a esquerda
    def leftRotate(self, node):
        y=node.right #define Y (quem vai rotacionar com X)
        node.right=y.left #caso o filho esquerdo de Y nao seja nulo Y e o node
        if y.left is not None:#caso o filho esquerdo de Y nao seja nulo Y e o node
            y.left.parent=node
        y.parent=node.parent#liga o pai de x a y
        if node.parent == None:
            self.root=y
        elif node == node.parent.left:#coso o no seja filho direito do seu pai
            node.parent.left=y
        else:
            node.parent.right=y
        y.left=node#a esquerda de Y recebe o no
        node.parent=y
    #rotaciona a direita
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
    #insere o no
    def insertNode(self,node):
        y=None
        nodeRoot=self.root
        while nodeRoot is not None: #para quando a raiz for conhecida
            y=nodeRoot
            #verifica a posicao em que o no sera inserido
            if node.key < nodeRoot.key:
                nodeRoot=nodeRoot.left
            elif node.key > nodeRoot.key:
                nodeRoot=nodeRoot.right
            else:
                 return None
        #define para node quem e o seu pai
        node.parent=y

        #define para Y quem e seu filho
        if y == None:
            self.root=node
        elif node.key < y.key:
            y.left=node
        else:
            y.right=node
        node.left=None
        node.right=None
        node.color= Color.RED;
        self.insertFixupNode(node)
    #redefine as cores e balanceia a arvore
    def insertFixupNode(self, node):
        while node.parent is not None and node.parent.color==Color.RED: #enquanto o pai do no tiver a cor vermelha
            grandFatherNode=node.parent.parent #avo do no
            #verifica se o no e filho esquerdo
            if node.parent == grandFatherNode.left:
                y=grandFatherNode.right
                #caso 1: o node e seu pai sao vermelho, violando propriedades
                #se o tio tambem seja vermelho basta recolorir os nos e o no passa a ser o no dois niveis de cima na arvore
                if y.color==Color.RED:
                    node.parent.color=Color.BLACK
                    y.color=Color.BLACK
                    grandFatherNode.color=Color.RED
                    node=grandFatherNode
                #caso 2: pai e filho tem nos vermelhos e tio e vermelho
                #se o no for filho direito do seu pai e feita uma rotacao a esquerda
                elif node==node.parent.right:
                    node=node.parent
                    # print 'left rotate'
                    # self.show(node)
                    self.leftRotate(node)
                #caso 3: pai e filho tem nos vermelhos e tio e preto
                #se o no for filho a esquerda do seu pai a arvore e colorida novamente e uma rotacao a direita e aplicada
                else:
                    node.parent.color=Color.BLACK
                    grandFatherNode.color=Color.RED
                    self.rightRotate(grandFatherNode)
            #caso o no seja filho direito
            else:
                y=grandFatherNode.left
                if y.color==Color.RED:
                    node.parent.color=Color.BLACK
                    y.color=Color.BLACK
                    grandFatherNode.color=Color.RED
                    node=grandFatherNode
                elif node==node.parent.left:
                    node=node.parent
                    self.rightRotate(node)
                else:
                    node.parent.color=Color.BLACK
                    grandFatherNode.color=Color.RED
                    self.leftRotate(grandFatherNode)
        self.root.color=Color.BLACK
    #procura um no na arvore
    def search(self, key, x = None):
        if x is None:
            x = self.root
        while x and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x
    #movimenta a arvore substituindo uma subarvore como um filho de seu pai por outra subarvore
    def transplant(self, u, v):
        if u.parent == None:
            self.root=v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    #pegar o objeto de menor key na arvore
    def treeMinimun(self, node):
        while node.left is not None:
            node=node.left
        return node
    #pegar o objeto de maior key na arvore
    def getMax(self):
        if self.root:
            node=self.root
            while node.right is not None:
                node=node.right
            return node.key
        else:
            return 0
    #redefine as cores e balanceia a arvore
    def deleteFixup(self, node):
        while node != self.root and node.color == Color.BLACK:
            #verifica se o no e filho esquerdo
            if node == node.parent.left:
                w = node.parent.right
                #caso1: se o irmao do no for vermelho
                if w.color==Color.RED:
                    w.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.leftRotate(node.parent)
                    w = node.parent.right
                #caso2: se o irmao for preto e os filhos do irmao forem pretos
                if (w.left!=None and w.right!=None)and (w.left.color==Color.BLACK and w.right.color==Color.BLACK):
                    w.color = Color.RED
                    node = node.parent
                #caso3:se o irmao nao tem filhos
                elif(w.left==None and w.right==None):
                    w.color = Color.RED
                    node = node.parent
                #case4: se o filho direito do irmao e preto e diferente de vazio
                elif ((w.right!=None) and (w.right.color == Color.BLACK)) or (w.right==None):
                    if(w.left!=None):
                        w.left.color = Color.BLACK
                    w.color = Color.RED
                    self.rightRotate(w)
                    w = node.parent.right
                    node.parent.color=Color.BLACK
                    if(w.left!=None):
                        w.left.color=Color.BLACK
                    self.leftRotate(node.parent)
                    node = self.root
            #caso o no seja filho direito
            else:
                w = node.parent.left
                if w.color==Color.RED:
                    w.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.rightRotate(node.parent)
                    w = node.parent.leftleft
                if (w.left!=None and w.right!=None)and (w.left.color==Color.BLACK and w.right.color==Color.BLACK):
                    w.color = Color.RED
                    node = node.parent
                elif(w.left==None and w.right==None):
                    w.color = Color.RED
                    node = node.parent
                elif ((w.left!=None) and (w.left.color == Color.BLACK)) or (w.left==None):
                    if(w.right!=None):
                        w.right.color = Color.BLACK
                    w.color = Color.RED
                    self.leftRotate(w)
                    w = node.parent.left
                    w.color=node.parent.color
                    node.parent.color=Color.BLACK
                    if(w.right!=None):
                        w.right.color=Color.BLACK
                    self.rightRotate(node.parent)
                    node = self.root
    #deleta um objeto da arvore
    def deleteNode(self, node):
        y = node
        yOriginColor= y.color
        x=None

        #caso1: o no nao tem filhos
        #apenas removemos o no
        if node.left == None and node.right==None:
            if node.parent is not None:
                if node == node.parent.left:
                    node.parent.left=None
                else:
                    node.parent.right=None
            else:
                self.root=None

        #caso2: tem um filho
        #apenas extraimos o no e mantemos a ligacao do neto com o avo
        elif node.left == None and node.right != None:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == None and node.left != None:
            x = node.left
            self.transplant(node, node.left)

        #caso3: tem dois filhos
        #extraimos o sucessor q tem no maximo um filho e colocamos no lugar do node
        else:
            y = self.treeMinimun(node.right)
            yOriginColor = y.color
            x = y.right
            if y.parent == node:
                if x != None:
                    x.parent = y
            else:
                self.transplant(y,y.right)
                y.right=node.right
                y.right.parent=y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if yOriginColor == Color.BLACK:
            if x!=None:
                self.deleteFixup(x)
        node.parent=None
        node.left=None
        node.right=None
    #metodo para printar testes
    def show(self, node):
        print ("No: ", str(node.key))
        print ("Cor: ", str(node.color.value))
        if node.parent is not None:
            print ("Pai: ", str(node.parent.key))
        if node.right is not None:
            print ("Filho direito: ", str(node.right.key))
        if node.left is not None:
            print ("Filho esquerdo: ", str(node.left.key)+"\n")
        print ("------------------")
# def main():
#     #nos
#     rootNode=RBNode(20)
#     rightNode = RBNode(30)
#     rightNode2 = RBNode(25)
#     leftNode = RBNode(10)
#     leftNode2 = RBNode(12)
#     rightNode35 = RBNode(35)
#     rightNode33 = RBNode(33)
#     rightNode36 = RBNode(36)
#     rightNode34 = RBNode(34)
#
#     #arvores
#     tree = RBTree()
#
#     #inserir nos nas arvores
#     tree.insertNode(rootNode)
#     tree.insertNode(leftNode)
#     tree.insertNode(rightNode)
#     tree.insertNode(rightNode2)
#     tree.insertNode(leftNode2)
#     tree.insertNode(rightNode35)
#     tree.insertNode(rightNode33)
#     tree.insertNode(rightNode36)
#     tree.insertNode(rightNode34)
#     tree.deleteNode(rightNode36)
#
#     tree.show(rightNode)
#     tree.show(rightNode2)
#     tree.show(leftNode)
#     tree.show(rootNode)
#     tree.show(leftNode2)
#     tree.show(rightNode33)
#     tree.show(rightNode35)
#     tree.show(rightNode36)
#     tree.show(rightNode34)
#
#     #testando buscar
#     print('')
#     print("TESTANDO BUSCAR CHAVE NA ARVORE")
#     found = tree.search(330)
#     if found:
#         print('Chave encontrada: ', found.key, '\n\n')
#     else:
#         print('Chave nao encontrada.')
#
#     #testando
#     # tree.show(rootNode)
#     # tree.show(leftNode)
#     # tree.show(rightNode)
#     # tree.show(rightNode2)
#     # print "No: "+str(rootNode.key)
#     # print "Cor: "+str(rootNode.color.value)
#     # print "Pai: "+str(rootNode.parent)
#     # print "Filho direito: "+str(rootNode.right.key)
#     # print "Filho esquerdo: "+str(rootNode.left.key)+"\n"
#     #
#     # print "No: "+str(leftNode.key)
#     # print "Cor: "+str(leftNode.color.value)
#     # print "Pai: "+str(leftNode.parent.key)
#     # print "Filho direito: "+str(leftNode.right)
#     # print "Filho esquerdo: "+str(leftNode.left)+"\n"
#     #
#     # print "No: "+str(rightNode.key)
#     # print "Cor: "+str(rightNode.color.value)
#     # print "Pai: " +str(rightNode.parent.key)
#     # print "Filho direito: "+str(rightNode.right)
#     # print "Filho esquerdo: "+str(rightNode.left.key)+"\n"
#     #
#     # print "No: "+str(rightNode2.key)
#     # print "Cor: "+str(rightNode2.color.value)
#     # print "Pai: " +str(rightNode2.parent.key)
#     # print "Filho direito: "+str(rightNode2.right)
#     # print "Filho esquerdo: "+str(rightNode2.left)+"\n"
# main()
