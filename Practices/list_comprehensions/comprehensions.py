# without list comprehension

nums = [4, -11, 69, 53, -65]

doubled =[]

for num in nums:
    doubled.append(num * 2)

# using list comprehnsion in one line
nums = [4, -11, 69, 53, -65]

doubled = [num * 2 for num in nums]

print(doubled)

# General syntax

# new_list = [<expression> for <element> in <collection>]

