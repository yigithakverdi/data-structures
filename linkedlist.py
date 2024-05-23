class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current))
            current = current.next
        return ' -> '.join(result)

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def deleteGracefully(self, value):
        pass

    
def main():

    values = [4,5,1,9]
    
    ll = LinkedList()
    for value in values:
        ll.append(value)
    
    print(ll)

if __name__ == '__main__':
    main()    
        