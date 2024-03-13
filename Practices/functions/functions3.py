# lambda functions

# lambda keyword - define anonymous functions

# Example 1

snack = lambda: print("Nyama Choma")

#calling the function

snack()


# lambda function with arguements

#example 2

def num_square(num):
    return num ** 2

print("square of num is:", num_square(8))

#example 3 - using a lambda function

num_square = lambda num: num ** 2

print("The square of num is:", num_square(100))

# use lambda function in simple expressions

#normal function

def isPalindrome(string):
    if (string == string[::-1]): # checks if the original string is equal to its reverse
                            # string[::-1] - creates a new string in the reverse order
        return "A palindrome"
    
    else:
        return "Not a palindrome"

string = input("Enter a string:")

print (isPalindrome(string))


# using a lambda function

is_palindrome = lambda string : "palindrome" if string == string[::-1] else "not a palindrome"

string = input("Enter string:")

print(is_palindrome(string))


