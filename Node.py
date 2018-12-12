'''
Created on Dec 6, 2018

@author: rajat.arora07
'''

class Node():
    
    def __init__(self, value, left=None, right=None):
        self.__left = left
        self.__right = right
        self.__value = value
    
    def set_left(self,node):
        self.__left = node
        
    def get_left(self):
        return self.__left
        
    def set_right(self,node):
        self.__right = node
        
    def get_right(self):
        return self.__right
    
    def set_value(self,value):
        self.__value = value
    
    def get_value(self):
        return self.__value
    