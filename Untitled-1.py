        """
        How to do it?
        
        1 -> 5 -> 10
        
        2 -> 3 -> 7
        
        6 -> 7 -> 8
        
        
        Brute-force:
        - add all to array (o(n))
        - sort array        (nlog(n))
        - convert array to linked list o(n)
        o(n) + nlog(n) + o(n)
        => nlogn
        
        Option 2:
        - Create a heap
        - add elements to heap
        """
        
        # Create Heap
        h = []
        for l in lists:
            while l:
                heappush(h, l.val)
                l = l.next
        
        current = None
        head = None
        while h:
            val = heappop(h)
            
            if not current:
                head = ListNode(val, None)
                current = head
            
            else:
                current.next = ListNode(val, None)
                current = current.next
            
        return head
            
        """
        How to make a heap?
        
        """
        
        
        # Add Elements to Heap
        
        
        # Pop all elements from heap
        