#Use doubly linked list and hash map to create LRU cache
import time

start_time = time.time()

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None
    
class doublyLinkedList:
    def __init__(self):
        self.start_node = None
        
    def InsertToEmptyList(self, value):
        if self.start_node is None:
            new_node = Node(value)
            self.start_node = new_node
        else:
            print("Empty list")
            
    
    
    def InsertToBeginning(self,value):
        if self.start_node is None:
            new_node = Node(value)
            self.start_node = new_node
        
        else:
            self.start_node = self.start_node.next
            new_node = Node(value)
            self.start_node = new_node
    
    
    def InsertToEnd(self, value):
        if self.start_node is None:
            new_node = Node(value)
            self.start_node = new_node
            return
            
        n = self.start_node
        
        while n.next is not None:
            new_node = Node(value)
            n.next = new_node
            new_node.prev = n
            
    def DeleteAtStart(self):
        if self.start_node is None:
            print("Linked List empty; nothing to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None
            
    def DeleteAtEnd(self):
        if self.start_node is None:
            print("Linked List empty; nothing to delete")
            return 
         
        if self.start_node.next is None:
            self.start_node = None
            return
            
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None 
            
            
            
    def Display(self):
        if self.start_node is None:
            print("List empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Value of element is: ", n.item)
                n = n.next
        print("\n")
            
    def Size(self):
        n = self.start_node
        count = 0
        while n is not None:
            count +=1
            n = n.next
        return count
    


class LRU_Cache(object):

    def __init__(self, size):
        self.dictionary = dict()
        self.dll = doublyLinkedList()
        self.size = size
        
    def get(self,key):
        
        if self.size == 0:
            return -1
        
        if key in self.dictionary.keys():
            return self.dictionary[key]
            if key not in self.dictionary.keys():
                return -1
            
    #Not complete yet
    
    
    def put(self,key, value):
        if key not in self.dictionary.keys():
            self.dictionary[key] = value
            self.dll.InsertToBeginning(value) #put most recent item to heat of dll\
            
        
        if self.dll.Size() > self.size:
            self.dll.DeleteAtEnd()
            
            
            
            
''' Edge test cases go here. Commented edge cases cause NameErrors '''
        
test_cache = LRU_Cache(5)

test_cache.put(0.5,2)
#We expect floats  to work as a data type and display 2 int 
print(test_cache.get(0.5))


#test_cache.put(_,_)
#We expect empty underscores not to work because of NameError
#print(test_cache.get(_))

test_cache.put("string", "abc")
#We expect strings to work as a data type and display "abc"
print(test_cache.get("string"))

#test_cache.put(not_string, probably_key)
#We ecpect a NameError 
#print(test_cache.get(not_string))


print("%s seconds" % (time.time() - start_time))


    