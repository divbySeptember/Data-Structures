import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import  DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # self.storage.add_to_head(value)
        # self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        # if self.size == 0:
        #     return
        # else:
        #     last = self.storage.remove_from_head()
        #     self.size -= 1
        #     return last
        return self.storage.remove_from_head()

    def len(self):
        # return self.size
        return self.storage.__len__()


stack = Stack()
print('Should be 0')
print(stack.len())
stack.push(4)
print('Should be 1')
print(stack.len())
stack.push(6)
print('Should be 2')
print(stack.len())
print('Should be 6')
print(stack.pop())