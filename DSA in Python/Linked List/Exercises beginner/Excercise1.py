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

    def insert_after_value(self, key, data):  ## This function is added
        if self.head is None:
            print("No such value exists in the linked list.")
            return
        temp = self.head
        if self.is_present(key):
            while temp.data != key:
                temp = temp.next
            node = Node(data)
            node.next = temp.next
            temp.next = node
            return
        print("No such value exists in the linked list.")

    def remove_value(self, data):
        if self.head is None:
            print("Linked list is already empty")
            return
        if self.head.data == data:
            self.delete_first_element()
            return
        if self.is_present(data):
            temp = self.head
            while temp.next.data != data:
                temp = temp.next
            temp_node = temp.next
            temp.next = temp.next.next
            del temp_node
            return
        print("No such element exists in the Linked List.")

    def insert_values(self, values):
        for value in values:
            self.insert_at_end(value)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_linked_list()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print_linked_list()
    ll.remove_value("orange")  # remove orange from linked list
    ll.print_linked_list()
    ll.remove_value("figs")
    ll.print_linked_list()
    ll.remove_value("banana")
    # ll.print_linked_list()
    ll.remove_value("mango")
    # ll.print_linked_list()
    ll.remove_value("apple")
    # ll.print_linked_list()
    ll.remove_value("grapes")
    ll.print_linked_list()
