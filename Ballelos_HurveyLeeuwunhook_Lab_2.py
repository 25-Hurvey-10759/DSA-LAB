class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traverseLinkedList():
    current = head
    while(current):
        print(current.data, end=" -> ")
        current = current.next

def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)
    
    if(head == None):
        head = newNode
    else:
        newNode.next = head
        head = newNode
        
def insertNodeAtTheEnd(data):
    global head
    newNode = Node(data)
    
    if(head == None):
        head = newNode
    else:
        current = head
        while(current.next != None):
            current = current.next
        current.next = newNode
        
def insertNodeAfterGivenNode(data, node):
    global head
    newNode = Node(data)

    if(head == None):
        head = newNode
        return

    current = head

    while(current != None and current.data != node):
        current = current.next

    if(current == None):
        print('The node does not exist')
        return

    newNode.next = current.next
    current.next = newNode
            
node1 = Node('SexyBack - Justin Timberlake')
head = node1

insertNodeAtTheBeginning('her - JVKE')
insertNodeAtTheBeginning('This is What Heart Break Feels Like - JVLE')
insertNodeAtTheEnd('Prom - John Micheal Howell')
insertNodeAtTheEnd('A Thousand Years - John Micheal Howell')
insertNodeAfterGivenNode('Smooth - Connor Price', 'A Thousand Years - John Micheal Howell')
insertNodeAfterGivenNode('Violet - Connor Price', 'Smooth - Connor Price')

traverseLinkedList()
