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
