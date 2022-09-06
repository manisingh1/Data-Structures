# Lists
from dataclasses import dataclass
from unicodedata import numeric


fruits = ['orange', 'apple', 'pear', 'banana', 'banana']
fruits.append('pineapple')
fruits.insert(0, "apple pie")
favorite_pie = fruits.pop(0)
print("My favorite pie is {pie}".format(pie=favorite_pie))
print("Index of pear is {}".format(fruits.index("pear", 1)))
print("There are {} bananas".format(fruits.count("banana")))
fruits.sort()
print("Here's a sorted fruit cart: \n{}".format(fruits))
fruits.reverse()
print("Here's a sorted fruit cart: \n{}".format(fruits))
print(fruits[len(fruits):])

class myList:
    def __init__(self, data=[]):
        self.data = data

    def append(self, data):
        pass

# List Comprehension
class Fruits:
    def __init__(self):
        self.fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
        self.num_a = 0
    
    def num_contain_a_loop(self):
        a_fruits = []
        for each_fruit in self.fruits:
            if 'a' in each_fruit:
                self.num_a+=1
                a_fruits.append(each_fruit)
        print('There are {} fruits containing "a"'.format(self.num_a))
        print('They are: {}'.format(a_fruits))
        self.num_a = 0

    def num_contain_a_list_comp(self):
        a_fruits = [x for x in self.fruits if 'a' in x]
        print('There are {} fruits containing "a"'.format(len(a_fruits)))
        print('They are: {}'.format(a_fruits))


class JamSession:
    def __init__(self, foo: str) -> None:
        self.foo = foo

class TestDicts:
    def __init__(self, dict = {"hello": "world"}):
        self.dict = dict
    
    def print_dict(self):
        print("The dict is {}".format(self.dict))

    



# Stack
    # Stacks are first in, last out
    # implement a stack using a list
class Stack:
    def __init__(self, data=[]):
        assert type(data) is list
        self.data = data

    def push(self, new_data):
        self.data.append(new_data)

    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[len(self.data)]

    # def __str__(self):
    #     # print("Stack is:\n")
    #     for index, value in reversed(list(enumerate(self.data))):
    #         print("{} , {}".format(index, value))
        

# Queue
# Using a deque as an implementation for a queue, the complexity is
# o(1) for all operations, but random access by index is O(n)



# LinkedList 


# BST

# Heap

# Graph

if __name__ == '__main__':
    print("------ Main -------")
    # print(fruits)

    pez = Stack([1, 2, 3])
    pez.push(4)
    # print(pez)

    fruit_cart = Fruits()
    fruit_cart.num_contain_a_loop()
    fruit_cart_franchise = Fruits()
    fruit_cart_franchise.num_contain_a_list_comp()


# Map
xs = map(lambda x : x + 2, [1, 2, 3])
other_xs = (x + 2 for x in [1, 2, 3])
other_xs[0]
print(xs)
print(list(xs))
print(other_xs)

