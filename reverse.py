"""
Reverse each word of a string individually. 

For eg. if a string is "abc def", reversed string should be "cba fed".
"""

print(( lambdaa s: ' '.join([x[::-1] for x in s.split()]))(input()))
