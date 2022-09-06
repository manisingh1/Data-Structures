def minMutation(start, end, bank) -> int:
    
    bank_set = set()
    visited = set()
    for mutation in bank:
        bank_set.add(mutation)
        
    mutations_count = 0
        
    q = []
    
    q.append((start,0))
    
    while len(q) > 0:
        
        for i in range(len(q)):
        
            current, step = q.pop(0)

            # check if matches end. If does, return mutations_count
            if current == end:
                return step

            # otherwise check if exists in bank. if does, increment count


            else:

            # lastly, BFS all possible children (change each char to one of other options)
                other_options = generate_options(current)
                # print(other_options)
            
                for each in other_options:
                    if each in bank_set:
                        q.append((each, step+1))
                        
    return -1

def toString(l):
    return "".join(l)

def generate_options(current):
    output = []
    l = current
    options = ['A', 'C', 'G', 'T']

    for i in range(len(l)):

        for c in "AGCT":
            temp = l
            temp = temp[:i] + c + temp[i+1:]
            output.append(toString(temp))
    return output
            

start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
print(minMutation(start=start, end=end, bank=bank))