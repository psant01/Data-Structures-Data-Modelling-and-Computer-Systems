# Implementation of a LinkedList data structure in Python
# This is an example of a singly linked list where each node (except the final node)
# points to the next element in the list

# Dr Paul Sant
# The University of Law
# Sample code created for the Data Structures, Data Modelling and Computer Systems module
# Level 4 - BSc (Hons) Computer Science

# A class used to represent a node in the Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr(self):
        return self.data
    
class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node  = node.next
        nodes.append("None")
        return "->".join(nodes)
    def add_first(self,node):
        node.next = self.head
        self.head = node
    def add_last(self,node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    def add_after(self,target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empoty")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empoty")
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)
    
# Now lets use our classes to test out the creation of a Linked List
    
llist = LinkedList() # Create an empty LinkedList object

print(llist)

# Now lets create a node and add it to the LinkedList

first_node = Node("a")
llist.head = first_node
print(llist)

# Now add a second item

second_node = Node("b")
first_node.next = second_node

# Now add a third node

third_node = Node("c")

second_node.next = third_node

# Now print the final list

print(llist)