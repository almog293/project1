#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - 209087592
#name2    - Yael Toledano



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
                self.left = node
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
                self.right = node
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
                self.parent = node
		return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
                self.value = value
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
                self.height = h
		return None

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return False if self is None else True
	
	###########################################
	        """retrieves the node with the maximum rank in a subtree

        @type node: AVLnode
        @pre: node != none
        @param node: the root of the subtree
        @rtype: AVLNode
        @returns: the node with the maximum rank in a subtree
        """
        def getMax(self):
                if getRight(self) == None:
                        return self
                return getMax(self.getRight())

	 """retrieves the node with the minimum rank in a subtree

        @type node: AVLnode
        @pre: node != none
        @param node: the root of the subtree
        @rtype: AVLNode
        @returns: the node with the minimum rank in a subtree
        """
        def getMin(self):
                if getLeft(self) == None:
                        return node
                return getMin(self.getLeft())
	
	
	 """retrieves the balance factor of an AVLNosde

        @type self: AVLnode
        @pre: self != none
        @rtype: int
        @returns: the balance factor of the given node.
        def getBF(self):
                return(getLeft(self).height - getRight(self).height)
	#########################################


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.first = self.root
		self.last = self.root
		self.size = 0
		# add your fields here

        
	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return True if self.getRoot() is None else False


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the value of the i'th item in the list
	"""
	def retrieve(self, i):
                root = self.getRoot()
                rootRank = length(root.getLeft())+1
                return retrieveRec(self, self.getRoot(), rootRank, i)

        ###########################################
        def retrieveRec(self, node, nodeRank, i):
                if i == nodeRank:
                        return node
                if i < nodeRank:
                        node = node.getleft()
                        nodeRank = length(node.getLeft())+1
                else: 
                        node = node.getRight()
                        nodeRank = nodeRank + length(node.getLeft())+1
                return retrieveRec(self, node, nodeRank, i)
        ###########################################
                
        
	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		return -1


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.first

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.last

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
                return listToArrayRec(self.getRoot())

        ##########################################   
        def listToArrayRec(node):
                if node is None:
                        return []
		return listToArray(node.getLeft()) + self.getValue() + listToArray(node.getRight())
        ########################################## 
        
	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
                return lengthRec(self.getRoot())

        ########################################## 
        def lengthRec(self, node):
                if node is None:
                        return 0
                if node.getLeft() is None and node.getRight() is None:
                        return 1
                return node.getLeft().lengthRec() + 1 + node.getRight().lengthRec()
        ########################################## 
        
	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
                return searchRec(self, val, self,first, 0)

        ##################################################
        def searchRec(self, val, node, i):
                if i >= size:
                        return -1
                if node.getValue() == val:
                        return i
                return searchRex(self, val, getSuccessor(node), i+1)
        ##################################################

	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root
		
	#########################################
        """retrieves the successor

        @type node: AVLnode
        @pre: node != none
        @rtype: AVLNode
        @returns: the successor of node,  None if there is no left child
        """
	def getSuccessor(self, node):
                if self.last == node:
                        retrun None
                if node.getRight() is not None:
                        return getMin(node.getRight())
                parent = node.getParent()
                while (parent is not None and node = parent.getRight()):
                        node = parent
                        parent = node.getParent()
                return parent
 
        """retrieves the predecessor

        @type node: AVLnode
        @pre: node != none
        @rtype: AVLNode
        @returns: the predecessor of node,  None if there is no left child
        """    
        def getPredecessor(self, node):
                if self.first == node:
                        retrun None
                if node.getLeft() is not None:
                        return getMax(node.getLeft())
                parent = node.getParent()
                while (temp is not None and node = parent.getLeft()):
                        node = parent
                        parent = node.getParent()
                return parent
        #########################################

