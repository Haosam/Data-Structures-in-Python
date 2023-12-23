class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def addFirst(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
    
    def printList(self):
        temp = self.head
        while(temp):
            print("Current data is ", temp.data)
            temp = temp.next
            print("The next reference address is ", temp)
        
    def print(self):
        temp = self.head
        print("The Linked List Elements are:")
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
            
if __name__ == "__main__":
    llist = LinkedList()
    
    print("Inserting the Element 300 into the first node at the beginning")
    llist.addFirst(300)
    
    print("Inserting the Element 200 into the first node at the beginning, and 300 becomes the 2nd node")
    llist.addFirst(200)
    
    print("Inserting the Element 100 into the first node at the beginning, and 300 becomes the 2nd node")
    llist.addFirst(100)
    
    print("")
    print("The Data Representation is ")
    llist.printList()
    print("")
    llist.print()