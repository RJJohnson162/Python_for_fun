# Initialize variables to keep track of the total commission and the number of transactions
total_commission = 0
num_transactions = int(input("Enter the number of transactions to process: "))

# Define commission rates based on the sales criteria
commission_rates = {
    (0, 100): 0.02,
    (100, 999): 0.04,
    (1000, 9999): 0.05,
}

# Function to calculate commission
def calculate_commission(sale_amount):
    for (min_amount, max_amount), rate in commission_rates.items():
        if min_amount <= sale_amount <= max_amount:
            return sale_amount * rate
    return sale_amount * 0.07  # Default commission rate

# Loop to record and process each transaction
for _ in range(num_transactions):
    # Get the sale amount from the user with input validation
    while True:
        try:
            sale_amount = float(input("Enter the sale amount in KES: "))
            if sale_amount >= 0:
                break
            else:
                print("Sale amount must be non-negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Calculate commission based on the provided criteria
    commission = calculate_commission(sale_amount)

    # Add the commission to the total commission
    total_commission += commission

    # Print the commission for the current transaction
    print(f"Commission for this transaction: {commission} KES")

# Print the total commission for all transactions
print(f"Total commission for all transactions: {total_commission} KES")
