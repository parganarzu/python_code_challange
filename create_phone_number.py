# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    result = "("
    for i in range(0,3):
        result += str(n[i])

    result += ") "

    for i in range(3,6):
        result += str(n[i])

    result += "-"

    for i in range(6,10):
        result += str(n[i])

    return result

print("Created phone num:", create_phone_number([7, 3, 2, 5, 6, 8, 9, 3, 0, 4]))