# Sort the Gift Code
# Write a function called sortGiftCode/sort_gift_code/SortGiftCode 
# that accepts a string containing up to 
# 26 unique alphabetical characters, and returns a string 
# containing the same characters in alphabetical order.

# Examples (Input -- => Output):
# "abcdef"                      -- => "abcdef"
# "pqksuvy"                     -- => "kpqsuvy"
# "zyxwvutsrqponmlkjihgfedcba"  -- => "abcdefghijklmnopqrstuvwxyz"


def sortGiftCode(n):
    x = ''.join(sorted(n))
    return x

print(sortGiftCode("cabo"))



# def sortGiftCode(n):
#     x = ''.join(sorted(n))
#     return x

# print(sortGiftCode("cabo"))

# sorting algorithm manually. Here's a version of sortGiftCode that 
# uses the Bubble Sort algorithm
def sortGiftCode(n):
    # Convert the string to a list of characters
    chars = list(n)
    # Bubble sort algorithm
    for i in range(len(chars)):
        for j in range(0, len(chars) - i - 1):
            if chars[j] > chars[j + 1]:
                # Swap the characters
                chars[j], chars[j + 1] = chars[j + 1], chars[j]
    # Convert the list back to a string and return
    return ''.join(chars)

# Test cases
print(sortGiftCode("abcdef"))