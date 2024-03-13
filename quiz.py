def outer_fun(a,b):
    def inner_fun(c,d):
        return c + d
    return inner_fun(a,b)
res = outer_fun(5,10)
print(res)

for num in range(1,5):
    print(num)



x = 0
for i in range(3):
    x = x + i

print(x)

for i in range(0,5,1):
    print(i)

list1 = [3, 2, 5, 6, 0, 7, 9]

sum_even = 0
sum_divisible_by_three = 0

for elem in list1:
    if elem % 2 == 0:
        sum_even += elem  # Use += for concise addition
        continue

    if elem % 3 == 0:
        sum_divisible_by_three += elem  # Use += for concise addition

print(f"Sum of even numbers: {sum_even}")
print(f"Sum of numbers divisible by 3: {sum_divisible_by_three}")

