"""Create a function called shortcut to remove 
the lowercase vowels (a, e, i, o, u ) in a given string.

"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"

* don't worry about uppercase vowels
"""

def shortcut( param_string ):
    for vowel in "aeiou":
        param_string = param_string.replace(vowel, "")
    return param_string

print(shortcut("Python code challange"))
print(shortcut("This is vowel remover"))