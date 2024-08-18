class DNode:
    def __init__(self, data=None, next=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        node = DNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_start(data)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        node = DNode(data)
        node.prev = temp
        temp.next = node
        self.tail = node

    def insert_at_index(self, index, data):
        if self.head is None:
            print("Index does not exist")
            return
        if index == 0:
            self.insert_at_start(data)
            return
        temp = self.head
        while index > 1:
            if temp.next:
                temp = temp.next
            else:
                print("Cannot link node at given index.")
                return
            index -= 1
        node = DNode(data)
        temp.next.prev = node
        node.next = temp.next
        node.prev = temp
        temp.next = node

    def insert_after_value(self, value, data):
        if self.is_present(value):
            temp = self.head
            while temp.data != value:
                temp = temp.next
            node = DNode(data)
            temp.next.prev = node
            node.next = temp.next
            temp.next = node
            node.prev = temp
            return
        print("Given value is not present in the Linked List.")

    def is_present(self, value):
        if self.head is None:
            return False
        temp = self.head
        while temp is not None:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def print_forward(self):
        if self.head is None:
            print("Empty Linked List")
            return
        temp = self.head
        print("Head", end="")
        while temp is not None:
            print("->", temp.data, end="")
            temp = temp.next
        print("-> Tail")

    def print_reverse(self):
        if self.head is None:
            print("Empty Linked List")
            return
        temp = self.tail
        print("Tail", end="")
        while temp is not None:
            print("->", temp.data, end="")
            temp = temp.prev
        print("-> Head")

    def insert_values(self, values):
        for value in values:
            self.insert_at_end(value)

    def remove_value(self, value):
        if self.is_present(value):
            temp = self.head
            while temp.next.data != value:
                temp = temp.next
            node_to_delete = temp.next
            temp.next = temp.next.next
            temp.next.next.prev = temp
            del node_to_delete
            return
        print("Value does not exist in Linked List.")

    def delete_first_element(self):
        if self.head is None:
            print("Linked List is alreadt empty.")
            return
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        del temp

    def delete_last_element(self):
        if self.head is None:
            print("Linked List is alreadt empty.")
            return
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        del temp

    def delete_ele_at_index(self, index):
        if self.head is None:
            print("Linked List is alreadt empty.")
            return
        if index == 0:
            self.delete_first_element()
            return
        temp = self.head
        while index > 1:
            if temp.next:
                temp = temp.next
            else:
                print("Index out of available range.")
                return
            index -= 1
        node_to_delete = temp.next
        temp.next = temp.next.next
        if temp.next:
            temp.next.next.prev = temp
        else:
            self.tail = temp
        del node_to_delete


if __name__ == "__main__":
    DLL = DoublyLinkedList()
    DLL.insert_at_start(24)
    DLL.insert_at_start(12)
    DLL.insert_at_end(36)
    DLL.insert_at_end(60)
    DLL.insert_values([72, 84, 96, 108, 120])
    DLL.insert_after_value(36, 48)
    DLL.delete_first_element()
    DLL.delete_last_element()
    DLL.delete_ele_at_index(4)
    DLL.print_forward()
    DLL.print_reverse()
