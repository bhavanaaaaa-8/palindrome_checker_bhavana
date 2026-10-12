text = input("Enter a word or sentence: ")
# Normalize capitalization and spacing
normalized_text = text.lower().replace(" ", "")
# Reverse using string slicing
reversed_text = normalized_text[::-1]
if normalized_text == reversed_text:
    print("It is a palindrome!")
else:
    print("It is not a palindrome!")
