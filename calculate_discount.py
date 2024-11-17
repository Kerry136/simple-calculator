def calculate_discount(price, discount_percent):
    # Checking if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculating the discount amount and subtract it from the original price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Returning the original price if no discount is applied
        return price

# Prompting the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating the final price using the function
final_price = calculate_discount(price, discount_percent)

# Printing the final price or the original price if no discount was applied
print(f"The final price is: {final_price}")
