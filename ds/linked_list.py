class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = Node()

    def __len__(self):
        count = 0
        curr = self.head

        while curr.next is not None:
            count += 1
            curr = curr.next

        return count

    def __repr__(self):
        elems = []

        curr = self.head
        while curr.next is not None:
            curr = curr.next
            elems.append(curr.data)

        return str(elems)

    def append(self, data):
        new_node = Node(data)

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def get(self, idx):
        if idx >= len(self):
            return None

        curr = self.head
        count = 0
        while True:
            curr = curr.next
            if count == idx:
                return curr.data
            count += 1

    def remove(self, idx):
        if idx >= len(self):
            return None

        else:
            cur = self.head
            count = 0

            while True:
                last_node = cur
                cur = cur.next
                if count == idx:
                    last_node.next = cur.next
                    return    
                count += 1


llist = LinkedList()
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

# print(llist.get(0))
print(llist)
llist.remove(1)
print(llist)
