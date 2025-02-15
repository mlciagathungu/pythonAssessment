word=str(input("Enter a word:"))
def is_palindrome(word):
    if word==word[::-1]:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"
print(is_palindrome(word))
