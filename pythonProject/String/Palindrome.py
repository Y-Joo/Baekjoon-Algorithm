import re
def isPalindrome(s:str)->bool:
    s.lower()
    re.sub('[^a-z0-9]', '', s)
    return s==s[::-1]
str=input()
print(isPalindrome(str))