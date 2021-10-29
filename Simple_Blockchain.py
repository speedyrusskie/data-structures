''' Create a blockchain implementation using linked lists and hashing '''

import hashlib
import datetime    
    
    
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
    
    
    def calc_hash(self):
        sha = hashlib.sha256()
        
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        
        sha.update(hash_str) #This needs to be adjusted
        
        return sha.hexdigest()


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        if data is None or data == "":
            return
        elif self.head is None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            self.tail = self.head 
        else:
            self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.hash)
            self.tail = self.tail.next
        
        return
    
    def toList(self):
        output = []
        node = self.head
        while node:
            output.append(node)
            node = node.next
        return output
    
'''Test Cases'''

'''Test Case #1'''
blockchain = LinkedList()
txt1 = "1st block"
txt2 = "2nd block"
txt3 = "3rd block"

blockchain.append(txt1)
blockchain.append(txt2)
blockchain.append(txt3)

print(blockchain.toList())


'''Test Case #2'''
blockchain_2 = LinkedList()

blockchain_2.append(5)
blockchain_2.append("str")
blockchain_2.append(3.14)
blockchain_2.append(-2)
blockchain_2.append(5 % 2)
blockchain_2.append(None) #We expenct this blockchain node not to be created

print(blockchain_2.toList())



'''Test Case #3'''
blockchain_3 = LinkedList()

blockchain_3.append(None) 

print(blockchain_3.toList()) #We expect an empty list