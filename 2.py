def is_palindrome(s: str) -> bool:
    s = ''.join(c for c in s.lower() if c.isalpha())
    return s == s[::-1]

assert is_palindrome("Лёша на полке клопа нашёл") == True    
assert is_palindrome("racecar") == True                      
assert is_palindrome("12321") == False                      
assert is_palindrome("Hello") == False                     
assert is_palindrome("A man a plan a canal Panama") == True  
