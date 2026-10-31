# CodeAlpha Task 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

number = int(input("How many different stocks do you want to buy? "))

for i in range(number):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices and quantity > 0:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print("Investment in", stock_name, "=", investment)
    else:
        print("Invalid stock name or quantity. This entry is skipped.")

print("\nTotal Investment =", total_investment)

with open("stock_report.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("Total Investment = " + str(total_investment))

print("Report saved as stock_report.txt")