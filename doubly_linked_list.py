class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, letter):
        node = Node(letter)
        node.prev = self.tail
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self):
        removed = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return removed

    def show(self):
        parts = []
        current = self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        return "none <-> " + " <-> ".join(parts) + " <-> none" if parts else "(empty)"


def main():
    name = input("Enter a word or name: ").strip().upper()
    if not name:
        print("Nothing entered.")
        return

    dll = DoublyLinkedList()

    for letter in name:
        dll.add(letter)
        print(f"Added {letter}: {dll.show()}")

    print()

    while dll.head is not None:
        letter = dll.remove()
        print(f"Removed {letter}: {dll.show()}")

    print("\nThe list is empty.")


if __name__ == "__main__":
    main()
