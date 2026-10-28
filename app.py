def calculate_total(price, quantity, discount_rate=0):
    if price < 0 or quantity < 0 or discount_rate < 0:
        raise ValueError("Inputs must remain strictly non-negative parameters.")
    if discount_rate > 100:
        raise ValueError("Discount rate cannot exceed 100%.")
        
    subtotal = price * quantity
    savings = subtotal * (discount_rate / 100)
    return round(subtotal - savings, 2)

def main():
    print("=== Shopping Bill Calculator (v2.0 - With Discounts) ===")
    try:
        price = float(input("Enter unit price: "))
        quantity = int(input("Enter quantity amount: "))
        discount = float(input("Enter discount percentage rate (0 for none): "))
        
        total = calculate_total(price, quantity, discount)
        print(f"Grand Total Bill (After Savings applied): ${total}")
    except ValueError as e:
        print(f"Error Input Verification: {e}")

if __name__ == "__main__":
    main()
