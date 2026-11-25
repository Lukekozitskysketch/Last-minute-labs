import datetime

categories = ["Rent", "Groceries", "Gas", "Entertainment"]
expenses = []

budget = float(input("Enter your monthly budget: $"))

for category in categories:
    spent = float(input(f"How much did you spend on {category}? $"))
    expenses.append(spent)

total = sum(expenses)
difference = budget - total
today = datetime.datetime.now().strftime("%Y-%m-%d")

if difference >= 0:
    status = f"Under budget by ${difference:.2f}"
else:
    status = f"Over budget by ${abs(difference):.2f}"

print(f"\n--- Budget Report ({today}) ---")
print(f"Total Spent: ${total:.2f}")
print(status)

with open("budget_summary.txt", "w") as file:
    file.write(f"Budget Report ({today})\n")
    file.write(f"Total Spent: ${total:.2f}\n")
    file.write(status + "\n")
