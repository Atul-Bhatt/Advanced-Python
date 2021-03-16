# Demonstrate the working of deque object

from collections import deque
import string


def main():
    # TODO: create a deque object using a string
    alphabets = string.ascii_lowercase
    deque_alphabets = deque(alphabets)
    print(*deque_alphabets)

    # TODO: pop items from left and right
    print(deque_alphabets.pop())
    print(deque_alphabets.popleft())
    print(*deque_alphabets)

    # TODO: append and appendleft
    deque_alphabets.append(26)
    deque_alphabets.appendleft(1)
    print(*deque_alphabets)

    # TODO: rotate the deque
    deque_alphabets.rotate(10)
    print(*deque_alphabets)


if __name__ == "__main__":
    main()
