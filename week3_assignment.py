# create a function that has two arguements
# arguements will be in float
def calculate_discount(price, discount_percent):

    discount_threshhold = 0.2 # min discount applicable
    if discount_percent >= discount_threshhold:
        discount_amount = price * discount_percent
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
input_price = float(input("What is the price of the item? "))
input_discount = float(input("What is the discount percentage (e.g, 20 for 20%):")) / 100   # convert to decimal

final_price = calculate_discount(input_price,input_discount)

print (f"The final price after discount is:  ${final_price: .2f}") # use the fstring format for standard practice and convert the final price to 2decimal places





    
