class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, letter):
        node = Node(letter)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self):
        removed = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed

    def show(self):
        parts = []
        current = self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        parts.append("none")
        return " -> ".join(parts)


def main():
    name = input("Enter a word or name: ").strip().upper()
    if not name:
        print("Nothing entered.")
        return

    sll = SinglyLinkedList()

    for letter in name:
        sll.add(letter)
        print(f"Added {letter}: {sll.show()}")

    print()

    while sll.head is not None:
        letter = sll.remove()
        print(f"Removed {letter}: {sll.show()}")

    print("\nThe list is empty.")


if __name__ == "__main__":
    main()
