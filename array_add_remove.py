def main():
    name = input("Enter a word or name: ").strip().upper()
    if not name:
        print("Nothing entered.")
        return

    A = [None] * len(name)
    i = 0

    for letter in name:
        A[i] = letter
        i += 1
        print(f"Added {letter} at index {i - 1} -> {A}")

    print(f"\nThe array now holds: {A}\n")

    while i > 0:
        i -= 1
        print(f"Removed {A[i]} from index {i}")
        A[i] = None
        print(f"   Array: {A}")

    if i == 0:
        print("\nThe array is empty.")


if __name__ == "__main__":
    main()
