#!/bin/python

import sys

class Node(object):

    def __init__(self,id, weight):
      self.children = []
      self.id = id
      self.weight = weight

    def getChildren(self):
        return self.children
    def setNodeValue(self,value):
        self.id = value
    def getNodeValue(self):
        return self.id
    def setNodeWeight(self,weight):
        self.weight = weight
    def getNodeWeight(self):
        return self.weight

    def insertChild(self,edge, weight):
        inserted = False
        if self.id == edge[0]:
            self.children.append(Node(edge[1], weight[1]))
            inserted = True
        elif self.id == edge[1]:
            self.children.append(Node(edge[0], weight[0]))
            inserted = True
        elif self.children is not []:
            for children in self.children:
                if children.children is not [] :
                    inserted = children.insertChild(edge, weight)
                else:
                    if children.id == edge[0]:
                        children.append(Node(edge[1], weight[1]))
                        inserted = True
                    elif children.id == edge[1]:
                        children.append(Node(edge[0], weight[0]))
                        inserted = True
        return inserted

    def attachRoots(self,roots):
        if isinstance(roots, list):
            for root_children in roots:
                if self.children is not []:
                    for root in self.children:
                        if root.id == root_children.id:
                            if root_children.children is not []:
                                for child in root_children.children:
                                    root.children.append(child)
                            break
                        elif root.children is not []:
                            for children in root.children:
                                children.attachRoots(root_children)
        elif isinstance(roots, Node):
            if self.children is not []:
                for root in self.children:
                    if roots.id == root.id:
                        if roots.children != []:
                                for child in roots.children:
                                    root.children.append(child)
                        break
                    elif root.children is not []:
                        for children in root.children:
                            children.attachRoots(roots)
        return self

def printTree(tree):
        if isinstance(tree, Node):
            print(tree.getNodeValue(),tree.getNodeWeight())
            printTree(tree.getChildren())
        elif type(tree) is list and tree != []:
                for children in tree:
                    if isinstance(children, Node):
                        print(children.getNodeValue(),children.getNodeWeight())
                        printTree(children.getChildren())
            

# test tree

def testTree(edges,weights):
    roots = []
    intial_root = Node(edges[0][0],weights[edges[0][0]-1])
    roots.append(intial_root)
    for edge in edges:
        status_count = 0
        for root in roots:
            status = root.insertChild(edge,[weights[edge[0]-1],weights[edge[1]-1]])
            if status:
                print(edge," inserted")
                break
            if not status:
                print(edge," Not inserted")
                status_count += 1
            if status_count == len(roots):
                print(edge,'storing as root node')
                roots.append(Node(edge[0],weights[edge[0]-1]))
    for root in roots:
        print("printing")
        printTree(root)
    root = roots[0]
    tree = root.attachRoots(roots[1])
    print("printing final root")
    printTree(tree)

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    weights = [int(arr_temp) for arr_temp in input().strip().split(' ')]    
    edges = []
    for arr_i in range(n-1):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       edges.append(arr_t)
    print(edges, weights)
    testTree(edges, weights)