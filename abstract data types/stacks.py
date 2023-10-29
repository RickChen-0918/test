""" 
Unit: Abstract Data Types
Presentation: 1 - Stacks - Basic

In this task you will create a basic stack that has the following operations:
  - push 
  - pop
  - isEmpty
  - peek

To complete this task follow the directions under each of the methods within 
the stack class. 

"""


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        try:
            self.elements.pop()
        except:
            pass

    def isEmpty(self):
        if self.elements:
            return False
        else:
            return True

    def peek(self):
        return self.elements[-1]
