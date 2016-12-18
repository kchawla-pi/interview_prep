#!/bin/python3

import random


class Node(object):
    def __init__(self, item):
        self.next = None
        self.data = item


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        linkedlist = []
        current_node = self.head
        while current_node:
            linkedlist.append(str(current_node.data))
            current_node = current_node.next
        return ' --> '.join(linkedlist)

    def __len__(self):
        if not self.head: return 0
        counter = 0
        current_node = self.head
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter

    def __iter__(self):
        self.iter_node = self.head
        return self

    def __next__(self):
        if self.iter_node is None: raise StopIteration
        current_node = self.iter_node
        self.iter_node = self.iter_node.next
        return current_node

    def appendToTail(self, item):
        new_node = Node(item) if not isinstance(item, Node) else item
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

        return new_node

    def appendToHead(self, item):
        new_head = Node(item) if not isinstance(item, Node) else item
        new_head.next = self.head
        self.head = new_head
        return new_head

    def remove(self, item):
        current_node = self.head
        if not current_node or (current_node and current_node.next is None):
            return False

        while current_node.next and current_node.next.data != item:
            current_node = current_node.next
        current_node.next = current_node.next.next

    def dedupe(self):
        current_node = self.head
        if current_node is None: return True
        memo = set()
        memo.add(current_node.data)
        while current_node.next:
            next_data = current_node.next.data
            if next_data in memo:
                current_node.next = current_node.next.next
            else:
                memo.add(next_data)
                current_node = current_node.next
        return self.head

    def kth_to_last(self, k):
        solution = self._kth_to_last(self.head, k)
        if isinstance(solution, Node):
            return solution.data
        else:
            return False

    def _kth_to_last(self, head, k):
        if head is None:
            return 1

        counter = self._kth_to_last(head.next, k)

        if isinstance(counter, Node):
            return counter
        elif counter == k:
            return head
        else:
            return counter + 1

    def partition(self, k):
        if self.head is None: return False
        current_node = self.head

        while current_node and current_node.next:
            data = current_node.next.data
            if data < k:
                temp_node = current_node.next
                current_node.next = current_node.next.next
                temp_node.next = self.head
                self.head = temp_node
            current_node = current_node.next
        return True

    def sumLinkedList(self, other):
        """
        Sum of linked lists with nodes as single digits. Number is stored in reverse order, such that the head is the 1s place.
        """
        if other is None:
            return self.head
        result = LinkedList()
        result.head = self._sumLinkedList(self.head, other.head)
        return result

    def _sumLinkedList(self, a, b, remainder=0):
        if not a and not b and remainder == 0: return None
        a_data = a.data if a else 0
        b_data = b.data if b else 0
        a_next = a.next if a else None
        b_next = b.next if b else None
        
        new_digit = Node((a_data + b_data + remainder) % 10)
        remainder = (a_data + b_data + remainder) // 10
        new_digit.next = self._sumLinkedList(a_next, b_next, remainder)
        return new_digit

    def sumLinkedList_fwd(self, other):
        if other is None: return self
        elif self.head is None: return other, 0

        # Make even length
        a_len = len(self)
        b_len = len(other)
        a_pointer = self.head
        b_pointer = other.head
        result = LinkedList()
        while a_len != b_len:
            if a_len > b_len:
                result.appendToTail(a_pointer.data)
                a_pointer = a_pointer.next
                a_len -= 1
            elif b_len > a_len:
                result.appendToTail(b_pointer.data)
                b_pointer = b_pointer.next
                b_len -= 1

        temp_head, remainder = self._sumLinkedList_fwd(a_pointer, b_pointer)

        # If you have a remainder, need to add it to the extra Nodes at beginning.
        if remainder > 0 and len(result) == 0:
            result.appendToHead(remainder)
            result.head.next = temp_head
        elif remainder > 0:
            temp = LinkedList()
            temp.appendToTail(remainder)
            result = result.sumLinkedList_fwd(temp)
            result.appendToTail(temp_head)
        return result

    def _sumLinkedList_fwd(self, a, b):
        if not a and not b: return None, 0

        next_node, remainder = self._sumLinkedList_fwd(a.next, b.next)
        digit = Node((a.data + b.data + remainder) % 10)
        digit.next = next_node
        remainder = (a.data + b.data + remainder) // 10
        return digit, remainder

    def isPalindrome(self):
        ll_as_list = [x.data for x in self]
        return ll_as_list == list(reversed(ll_as_list))

    def isIntersecting(self, other):
        if self.head is None or other is None: return False
        
        # tie tail to head
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        tail = current_node
        tail.next = other.head

        loop_exists = self.detectLoop()
        tail.next = None
        return loop_exists

    def deletefromMiddle(self, node):
        if not node.next: return None
        node.data = node.next.data
        node.next = self.deletefromMiddle(node.next)
        return node

    def detectLoop(self):
        # runner technique
        slow = self.head
        fast = self.head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow == fast:
                return True
        return False


print('#######################')
print('Begin Tests:')
myList = LinkedList()
myList.appendToTail(5)
myList.appendToTail(6)
myList.appendToTail(7)
myList.appendToTail(8)
myList.appendToTail(9)
myList.appendToTail(5)
myList.appendToTail(100)
myList.appendToTail(5)
myList.appendToTail(100)
print('myList: %s' % myList)
myList.dedupe()
print('running dedupe()')
print('myList: %s' % myList)
print('\n')
print('running kth_to_last(3)')
print(myList.kth_to_last(3))
print('running kth_to_last(0)')
print(myList.kth_to_last(0))
print('running kth_to_last(100)')
print(myList.kth_to_last(100))
print('\n')
partList = LinkedList()
partList.appendToTail(random.randint(0,100))
partList.appendToTail(random.randint(0,100))
partList.appendToTail(random.randint(0,100))
partList.appendToTail(random.randint(0,100))
partList.appendToTail(random.randint(0,100))
partList.appendToTail(random.randint(0,100))
partList.appendToTail(random.randint(0,100))
partList.appendToTail(random.randint(0,100))
partList.appendToTail(random.randint(0,100))
print('partList(50): %s' % partList)
partList.partition(50)
print('partList(50): %s' % partList)
print('\n')
a = LinkedList()
b = LinkedList()
a.appendToTail(9)
a.appendToTail(8)
a.appendToTail(7)
a.appendToTail(6)
a.appendToTail(5)
b.appendToTail(9)
b.appendToTail(9)
b.appendToTail(9)
b.appendToTail(9)
print('Summing the following:')
print(a)
print(b)
print('---------------------------------')
print(a.sumLinkedList(b))
print(a.sumLinkedList_fwd(b))
print('\n')

f = LinkedList()
f.appendToTail('a')
f.appendToTail('b')
a_node = Node('c')
f.appendToTail(a_node)
f.appendToTail('d')
f.appendToTail('e')
print('f_list: %s' % f)
print('deleting %s' % a_node.data)
f.deletefromMiddle(a_node)
print('f_list: %s' % f)
print('\n')

c = LinkedList()
c.appendToTail('t')
c.appendToTail('a')
c.appendToTail('c')
some_node = Node('o')
c.appendToTail(some_node)
c.appendToTail('c')
c.appendToTail('a')
c.appendToTail('t')
print('%s is a Palindrome? %s' % (c, c.isPalindrome()))
print('%s is a Palindrome? %s' % (a, a.isPalindrome()))
c.appendToTail('t')
print('%s is a Palindrome? %s' % (c, c.isPalindrome()))
print('\n')
d = LinkedList()
d.appendToTail('c')
d.appendToTail(some_node)
print('%s is intersecting %s? %s' % (c, b, c.isIntersecting(b)))
print('%s is intersecting %s? %s' % (c, d, c.isIntersecting(d)))

c.appendToTail(some_node)
print('Loop Present? %s (should be True)' % c.detectLoop())