def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it is 20% or higher.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    
    Returns:
    float: The price after applying the discount if discount_percent >= 20,
           otherwise the original price.
    """
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount amount from the original price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

        # Prompt the user for input values
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Determine if a discount was applied and print the appropriate message
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. Price remains: {final_price}")

