'''
Created on Dec 6, 2018

@author: rajat.arora07
'''
from Trees.Node import Node

 
class BST():
    '''
    classdocs
    '''
 
    __count = 0
    def __init__(self, value):
        '''
        Constructor
        '''
        self.set_root(Node(value))
        
    def set_root(self, node):
        
        self.__root = node
            
    def get_root(self):
        
        return self.__root
               
    def insert(self, current_node, new_node):
        
        print current_node.get_value(), new_node.get_value()
        if new_node.get_value() < current_node.get_value():
            #print 'towards left'
            if current_node.get_left() is None:
                #print 'first left only'
                current_node.set_left(new_node)
            else:
                #print 'left'
                self.insert(current_node.get_left(), new_node)
        elif new_node.get_value() > current_node.get_value():
            #print 'towards right'
            if current_node.get_right() is None:
                #print 'first right'
                current_node.set_right(new_node)
            else:
                #print 'right'
                self.insert(current_node.get_right(), new_node)
      
    def search(self, current_node, value):
        #print current_node.get_value(), value
      
        if current_node.get_value() == value:
            return 'Found'
        else:
            if value > current_node.get_value():
                #print 'right'
                if current_node.get_right() is None:
                    return 'Not found'
                return self.search(current_node.get_right(), value)
            else:
                #print 'left'
                if current_node.get_left() is None:
                    return 'Not found'
                return self.search(current_node.get_left(), value)
            
    def inorder(self,root): 
        if root: 
            self.inorder(root.get_left()) 
            print(root.get_value()) 
            self.inorder(root.get_right()) 
       
         
               
list_of_items = [3,2,4,7,6,8]
 
tree_object = BST(5)

for i in range(len(list_of_items)):
    tree_object.insert(tree_object.get_root(),Node(list_of_items[i]))
tree_object.inorder(tree_object.get_root())

print tree_object.search(tree_object.get_root(), 9)

