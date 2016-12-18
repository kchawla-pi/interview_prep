#!/bin/python3


import collections


class myStack(object):
    def __init__(self):
        self.stack = []
        self.next_min = []

    def __len__(self):
        return len(self.stack)

    def push(self, item):
        if not self.next_min:
            next_min = None
        elif not self.next_min[0]:
            next_min = self.stack[-1]
        else:
            next_min = min(self.next_min[-1], self.stack[-1])
        self.stack.append(item)
        self.next_min.append(next_min)
        return item

    def pop(self):
        if not self.stack: return None
        self.next_min.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self, max_size):
        return len(self.stack) >= max_size

    def stack_min(self):
        """
        Design a stack which, in addition to push and pop, has a function min which returns the minimum element.  Push, pop, and min should operate at O(1)
        """
        if not self.next_min[-1]: return self.stack[-1]
        return min(self.next_min[-1], self.stack[-1])


class Set_Of_Stacks(object):
    def __init__(self, max_size=10):
        self.stacks = []
        self.max_size = max_size

    def __len__(self):
        return len(self.stacks)

    def push(self, item):
        if not self.stacks or \
           (self.stacks and len(self.stacks[-1]) >= self.max_size) or \
           (self.stacks and self.stacks[-1].isFull(self.max_size)):
           self.stacks.append(myStack())

        # find next stack that isn't full, and put it there.
        i = 0
        while i < len(self.stacks) and self.stacks[i].isFull(self.max_size):
            i += 1
        self.stacks[i].push(item)
        return item

    def pop(self):
        if not self.stacks: return None
        temp = self.stacks[-1].pop()
        if self.stacks[-1].isEmpty():
            self.stacks.pop()
        return temp

    def pop_at(self, i):
        if not self.stacks or i > len(self.stacks) - 1:
            return None
        temp = self.stacks[i].pop()
        if self.stacks[i].isEmpty():
            self.stacks.pop(i)
        return temp

class StupidQueue(object):
    def __init__(self):
        """
        Implement a MyQueue class which implements a queue using two stacks.
        """
        self.inbox = []
        self.outbox = []

    def push(self, item):
        if not self.outbox:
            self.outbox.append(item)
        else:
            self.inbox.append(item)
        return item

    def pop(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()


def sort_stack(stack):
    sorted_stack = []
    while stack:
        temp = stack.pop()
        while sorted_stack and sorted_stack[-1] < temp:
            stack.append(sorted_stack.pop())
        sorted_stack.append(temp)
    return sorted_stack

stack = [5, 6, 3, 2, 9]
print(sort_stack(stack))




# newStack = myStack()
# newStack.push(5)
# newStack.push(6)
# newStack.push(3)
# newStack.push(2)
# newStack.push(9)
# print(newStack.stack, newStack.stack_min())
# newStack.pop()
# print(newStack.stack, newStack.stack_min())
# newStack.pop()
# print(newStack.stack, newStack.stack_min())
# newStack.pop()
# print(newStack.stack, newStack.stack_min())
# newStack.pop()
# print(newStack.stack, newStack.stack_min())

# print('\n\n')
# setofstacks = Set_Of_Stacks()
# for i in range(1000):
#     setofstacks.push(i)
# print(len(setofstacks))
# setofstacks.pop()
# setofstacks.pop_at(0)
# setofstacks.pop_at(0)
# print(len(setofstacks.stacks[0]))
# print(len(setofstacks.stacks[-1]))
# for j in range(3):
#     setofstacks.push(i)
# for k in range(550):
#     setofstacks.pop()
# print(len(setofstacks))

# print("\n\n")
# stupidqueue = StupidQueue()
# for i in range(100):
#     stupidqueue.push(i)

# for i in range(100):
#     print(stupidqueue.pop(), )