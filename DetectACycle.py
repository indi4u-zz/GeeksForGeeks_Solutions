"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if(head.next is None):
        return(False)
    else:
        nodes_list = []
        current = head.next
        while(current is not None):
            nodes_list.append(current)
            if(current.next is None):
                return(0)
            elif(current.next in nodes_list):
                return(1)
            else:
                current = current.next

            
