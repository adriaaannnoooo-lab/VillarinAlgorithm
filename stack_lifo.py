def main():
    name = input("Enter a word or name: ").strip().upper()
    if not name:
        print("Nothing entered.")
        return

    S = []

    step = 1
    for letter in name:
        S.append(letter)
        print(f"{step:>2}. append({letter})  Stack (bottom -> top): {' '.join(S)}")
        step += 1

    print()

    while S:
        letter = S.pop()
        remaining = ' '.join(S) if S else "(empty)"
        print(f"{step:>2}. pop() -> {letter}  Stack (bottom -> top): {remaining}")
        step += 1

    print("\nThe stack is empty.")


if __name__ == "__main__":
    main()
