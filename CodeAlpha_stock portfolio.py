# Stock prices dictionary (hardcoded)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}


portfolio = {}


print("Enter your stock portfolio:")
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in the database. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")

total_value = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print(f"\nTotal Investment Value: ₹{total_value}")

save_option = input("Do you want to save this summary to a file? (yes/no): ").lower()

if save_option == "yes":
    file_type = input("Enter file type to save (txt/csv): ").lower()
    file_name = f"portfolio_summary.{file_type}"
    
    with open(file_name, "w") as file:
        file.write("Stock,Quantity,Price,Value\n" if file_type == "csv" else "")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            if file_type == "csv":
                file.write(f"{stock},{qty},{price},{value}\n")
            else:
                file.write(f"{stock}: {qty} shares × ₹{price} = ₹{value}\n")
        file.write(f"\nTotal Investment Value: ₹{total_value}")

    print(f"Summary saved to {file_name}")
else:
    print("Summary not saved.")
