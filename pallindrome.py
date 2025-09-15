def is_palindrome(text):
    # Remove spaces and convert to lowercase for uniformity
    text = str(text).replace(" ", "").lower()
    return text == text[::-1]

# Example with string
word = "Madam"
if is_palindrome(word):
    print(f'"{word}" is a Palindrome ')
else:
    print(f'"{word}" is NOT a Palindrome ')

# Example with number
num = 12321
if is_palindrome(num):
    print(f"{num} is a Palindrome ")
else:
    print(f"{num} is NOT a Palindrome ")
