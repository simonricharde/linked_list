class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, key):
        current = self.head

        while current:
            if current.value == key:
                return True
            
            current = current.next

        return False

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += "{ " +current.value +" } -> "
            current = current.next
        result += 'None'
        return result   

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next