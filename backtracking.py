from typing import List

def toString(List):
    return ''.join(List)

def stringPermutation(s, left, right):
    print(s)
    print(type(s))
    # s = list(s)
    if left == right:
        print(s)
        
    else:
        for i in range(left, right):
            s[left], s[i] = s[i], s[left]
            stringPermutation(str, left+1, right)
            s[left], s[i] = s[i], s[left] # backtrack
        

List = ['A', 'B', 'C']

stringPermutation(List, 0, len(List))

