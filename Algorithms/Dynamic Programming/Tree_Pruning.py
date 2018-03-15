#!/bin/python

import sys

class Node():
    def __init__(self, val=None, child_val=None, parent=None, children=None):
        self.val = val
        self.child_val = child_val
        self.parent = parent
        self.children = [] if not children else children

    def add_child(self, node):
        if not isinstance(node, Node):
            raise ValueError("Cannot append node of type: [%s]" % type(node))
        else:
            self.children.append(node)

def is_terminal(e):
    return len(e) == 2 and type(e[0]) == int and type(e[1]) == int

def from_list(lst, weights, root):
    lst = list(lst)
    if not lst:
        return
    for e in lst:
        if is_terminal(e):
            val, child_val, parent, children = weights[e[0]-1], weights[e[1]-1], e[0], e[1]
            print("terminal", val, "with root", root.val)
            root.add_child(Node(val=val,child_val=child_val, children=children, parent=parent))
        # else:
        #     e = list(e)
        #     val, parent, children = weights, e.pop(0), e
        #     print("non terminal", val, "with root", root.val)
        #     newroot = Node(val=val, parent=root)
        #     root.add_child(newroot)
        #     from_list(e, val, root=newroot)

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    weights = [int(arr_temp) for arr_temp in input().strip().split(' ')]    
    edges = []
    for arr_i in range(n-1):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       edges.append(arr_t)
    print(edges, weights)
    e = edges[0]
    root = Node(val=weights[e[0]], child_val=weights[e[1]], parent=e[0], children=e[1])
    from_list(edges, weights, root=root)