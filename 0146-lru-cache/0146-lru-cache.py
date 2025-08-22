class Node:
    # define a doubly linked list node
    def __init__(self, key, val, prev: Optional["Node"] =None, nextt=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=nextt

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        # Clue that we can use linked list is there is frequent movement of elements based on usage
        # doubly linked list to hold key, value
        # keep least recently used element at the head so that it can deleted in O(1)
        self.head,self.tail = None,None
        # map of key to linked list node that holds the value
        self.map={}
        

    def _move_to_tail(self, node: Node):
        if node==self.tail:
            return
        
        if node==self.head:
            self.head=self.head.next
            self.head.prev=None
        else:
            # disconnect the given node from list
            p=node.prev
            n=node.next
            p.next=n
            n.prev=p

        # move to end
        self.tail.next=node
        node.prev=self.tail
        node.next=None
        self.tail=node
    

    def _insert_at_tail(self, key, val):
        newNode=Node(key, val)
        if not self.head:
            self.head,self.tail = newNode,newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
    
    def _remove_from_head(self):
        if not self.head:
            return
        
        if self.head==self.tail:
            del self.head
            self.head,self.tail = None,None
        else:
            t=self.head
            self.head=self.head.next
            self.head.prev=None
            del t


    def get(self, key: int) -> int:
        v=-1
        if key in self.map:
            v=self.map[key].val
            # move node to end as it is recently used
            self._move_to_tail(self.map[key])
        return v
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            n=self.map[key]
            n.val=value
            # move to end as it is recently used
            self._move_to_tail(n)
        else:
            # insert at end and update map
            self._insert_at_tail(key, value)
            self.map[key]=self.tail

            # if capacity is reached, delete least used element
            if len(self.map)>self.cap:
                del self.map[self.head.key]
                self._remove_from_head()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Time complexity: O(1) for put() and get()
# Space complexity: O(n)