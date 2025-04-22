def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting user for input
try:
    original_price = float(input("2000:"))
    discount = float(input("20%:"))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${original_price:.2f}")
except ValueError:
    print("final_price.")
   