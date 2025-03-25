def calculate_discount(price, discount_percent):
    """
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.
    
    Returns:
    float: The final price after applying the discount if applicable, otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Prompt user for input
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the result
    print(f"Final price: ${final_price:.2f}")

