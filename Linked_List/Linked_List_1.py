class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print("Current data is ", temp.data)
            temp = temp.next
            print("The next reference address is ", temp)
            
    def print(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
            
if __name__ == '__main__':
    linkedlist = LinkedList()
    
    linkedlist.head = Node(10)
    middle1 = Node(20)
    middle2 = Node(30)
    middle3 = Node(40)
    middle4 = Node(50)
    last = Node(60)

    linkedlist.head.next = middle1
    middle1.next = middle2
    middle2.next = middle3
    middle3.next = middle4
    middle4.next = last
    
    print("Data Representation:")
    linkedlist.printList()
    print("")
    print("The LinkedList Elements Are:")
    linkedlist.print()