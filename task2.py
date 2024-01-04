from collections import deque

def is_palindrome(string: str) -> bool:
    # Remove spaces and convert to lowercase
    string = string.replace(' ', '').lower()

    # Create a deque from the string
    d = deque(string)

    # Check if it's a palindrome
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    
    return True

def process_example(example: str):
    result = is_palindrome(example)
    print('The string "{}" is {}a palindrome'.format(example, '' if result else 'not '))

def main():
    process_example("abba") # True
    process_example("abca") # False
    process_example("abcba") # True
    process_example("abDba") # True
    process_example("a Da ") # True
    process_example("a Da 1") # False

if __name__ == '__main__':
    main()
