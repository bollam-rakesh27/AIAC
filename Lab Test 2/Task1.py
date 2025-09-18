def seed_discount(price):
    return price - price * 0.1

def fert_discount(price):
    return price - price * 0.15

def tool_discount(price):
    return price - price * 0.05
# Calculates the discounted price based on the product category.

# Parameters:
#     price (float): The original price of the product. Must be a non-negative number.
#     category (str): The category of the product. Must be one of 'seeds', 'fertilizers', or 'tools'.

# Returns:
#     float: The price after applying the category-specific discount, rounded to two decimal places.

# Raises:
#     TypeError: If price is not a number.
#     ValueError: If price is negative or category is invalid.

def apply_discount(price, category):
    # Check if price is a number
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number.")
    # Check if price is non-negative
    if price < 0:
        raise ValueError("Price cannot be negative.")
    # Define discount rates for each category
    discounts = {
        "seeds": 0.10,
        "fertilizers": 0.15,
        "tools": 0.05
    }
    # Convert category to lowercase for case-insensitive matching
    category = category.lower()
    # Validate category
    if category not in discounts:
        raise ValueError("Invalid category. Must be 'seeds', 'fertilizers', or 'tools'.")
    # Get the discount rate for the category
    discount = discounts[category]
    # Calculate and return the discounted price, rounded to two decimal places
    return round(price * (1 - discount), 2)

# Main program entry point
if __name__ == "__main__":
    try:
        # Prompt user for price input
        price = float(input("Enter the price: "))
        # Prompt user for category input
        category = input("Enter the category (seeds, fertilizers, tools): ")
        # Calculate the final discounted price
        final_price = apply_discount(price, category)
        # Display the discounted price
        print(f"Discounted price: {final_price}")
    except Exception as e:
        # Handle and display any errors
        print(f"Error: {e}")