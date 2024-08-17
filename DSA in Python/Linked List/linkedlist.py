class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        node = Node(data)
        temp = self.head
        while index > 1:
            if temp.next:
                temp = temp.next
            else:
                print("Cannot link a node at the given index")
                return
            index -= 1
        node.next = temp.next
        temp.next = node

    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head
        print("head", end="")
        while temp:
            print(" ->", temp.data, end="")
            temp = temp.next
        print()

    def delete_first_element(self):
        if self.head is None:
            print("Linked List is already Empty")
            return
        temp = self.head
        self.head = temp.next
        del temp

    def delete_last_element(self):
        if self.head is None:
            print("List is already empty")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        del temp.next
        temp.next = None

    def delete_element_at_index(self, index):
        if self.head is None:
            print("Linked List is already emplty")
            return
        temp = self.head
        while index > 1:
            temp = temp.next
            index -= 1
        temp_node = temp.next
        temp.next = temp_node.next
        del temp_node

    def is_present(self, key):  # Search the element
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


if __name__ == "__main__":
    LL = LinkedList()
    LL.insert_at_beginning(24)
    LL.insert_at_beginning(12)
    LL.insert_at_end(48)
    LL.insert_at_end(60)
    LL.insert_at_index(2, 36)
    LL.print_linked_list()
    LL.delete_first_element()
    LL.delete_element_at_index(3)
    LL.print_linked_list()
    print(LL.is_present(24))
