class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
                
        q = []
        origin = (0,0)
        dest = (x,y)
        visited = set()
        q.append(origin)
        num_steps = 0
        
        while len(q) > 0:

            for i in range(len(q)):
                # get top of queue
                current = q.pop(0)
                if current == dest:
                    return num_steps

                # visit
                visited.add(current)

                # get child nodes
                moves = self.get_possible_moves(current)

                # iterate through all children, visit, and add to queue
                for curr_move in moves:
                    # if self.is_dest(curr_move, dest):
                    #     return num_steps
                    # else:
                    if curr_move not in visited:
                        visited.add(curr_move)
                        q.append(curr_move)
                        
            num_steps += 1
            
            
                    
            
    def get_possible_moves(self, node):
        possible_moves = [(1,2), (2,1), (-1,2), (-2,1), (-2,-1),(-1,-2), (1,-2), (2,-1)]
        
        updated_moves = []
        for each_move in possible_moves:
            new_x = each_move[0] + node[0]
            new_y = each_move[1] + node[1]
            updated_moves.append((new_x, new_y))
        return updated_moves
    
    def is_dest(self, curr, dest):
        return curr == dest
    
            
            
            
sol = Solution
print(sol.minKnightMoves(1,1,1))






class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        bank_set = set()
        visited = set()
        for mutation in bank:
            bank_set.add(mutation)
            
        mutations_count
            
        q = []
        
        q.append(start)
        
        while len(q) > 0:
            
            for 
            
            current = q.pop(0)
            
            # check if matches end. If does, return mutations_count
            if current == end:
                return mutations_count
            
            # otherwise check if exists in bank. if does, increment count
            elif current in bank_set:
                mutations_count += 1
            
            else:
            
            # lastly, BFS all possible children (change each char to one of other options)
            other_options = generate_options(current)
            
            # else, check if visited. if visited, don't add
