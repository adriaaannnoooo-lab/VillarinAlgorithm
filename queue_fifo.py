from collections import deque


def main():
    name = input("Enter a word or name: ").strip().upper()
    if not name:
        print("Nothing entered.")
        return

    Q = deque()

    step = 1
    for letter in name:
        Q.append(letter)
        print(f"{step:>2}. append({letter})  Queue (front -> back): {' '.join(Q)}")
        step += 1

    print()

    while Q:
        letter = Q.popleft()
        remaining = ' '.join(Q) if Q else "(empty)"
        print(f"{step:>2}. popleft() -> {letter}  Queue (front -> back): {remaining}")
        step += 1

    print("\nThe queue is empty.")


if __name__ == "__main__":
    main()
