from email.quoprimime import header_check
from tkinter.messagebox import NO

class QueueTwoStacks:
    pass



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __str__(self):
        return f"{self.val}->{self.next}"

class LinkedList:
    
    def __init__(self, arr=[]):
        self.head = None
        self.tail = None
        self.length = 0
        
        for val in arr:
            self.append(val)
        
    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
            return

        temp = self.tail

        node = ListNode(val)
        temp.next = node
        self.tail = node

    def create_list_from_Arr(self,arr):
        if len(arr) == 0:
            return None
        
        current_node = ListNode(arr[0])
        for i in range(0, len(arr)):
            node = ListNode(arr[i])
            if i == len(arr-1):
                self.tail = node
            if i == 0:
                self.head = node

    def print(self):
        print("Print Linked List")
        print(f'{self.head}')


# append, delete item, insert, reverse, pop_front, pop_end, at

    def delete(self, val):
        """
        - iterate through list, find node where == val
        - keep track of prev
        - make prev->next == current->next
        """
        if self.head.val == val:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            return

        node = self.head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                return
            
            node = node.next
    
    def delete_recursive(self, node, val):
        if node.val == val:
            node.next = None
            return
        if node.next.val == val:
            node.next = node.next.next
            return
        
        self.delete_recursive(node.next, val)

    def at(self, index):
        node = self.head
        for i in range(index):
            if node == None:
                break
            node = node.next
            if i == index:
                break
        return node
    
    def insert_after(self, val, index):
        node = self.at(index)
        after = node.next
        node.next = ListNode(val)
        node.next.next = after




                
    
lst = LinkedList([1])

lst.append(55)
lst.append(77)
lst.append(88)

print(lst.at(0))
print(lst.at(1))
print(lst.at(2))
print(lst.at(3))
print(lst.at(0))

lst.insert_after(2, 0)
lst.print()

# lst.delete(1)
# lst.print()
# lst.delete(55)
# lst.print()



"""




"""