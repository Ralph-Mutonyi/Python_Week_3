# functions - piece of code that can be used repeatedly


# function without parameters

#def <function name> :
#    <task to complete>

# function with paramaters

#def <function_name (a, b)>:
#   <task to be completed>

#1. 

def add_nums():
    print(2 + 13)

# calling a function
add_nums()

# function with parameters and arguements

def add_nums1 (a, b):
    answer = a + b
    return answer

# call the function by assigning to a variable called total

total = add_nums1(15, 15)
print("Total: ", total)

# Arbitrary keywords = *args

def add_nums2(*nums):
    sum = 0
    for num in nums:
        sum += num # sum variable will be equal to addition of each 
                    # item inside the tuple which is your arguement. 
    return sum

# call the function

print("Total:", add_nums2(2, 5, 6, 7, 8, 13))


# **kwargs
# keyward arguement to be passed in a function isnt known

def add_ages(**ages):
    sum = 0
    for k,v in ages.items():
        sum += v
    return sum

#calling the function

print("Total: ",add_ages(mutemi = 23, skinny = 22, ahmed = 21))
    


