from analyzer import categorizer, loader, analysis, visualizer

#
df = loader.load_data('data/transactions.csv')

#
df = categorizer.categ(df)

#
income = analysis.get_total_income(df)
expenses = analysis.get_total_expenses(df)
savings, rate = analysis.get_savings(df)
by_category = analysis.get_spending_by_category(df)
by_month = analysis.get_monthly_spending(df)

#
print("=" * 40)
print("     PERSONAL FINANCE DASHBOARD")
print("=" * 40)

print("\n── Income & Savings ──")
print(f"Total Income    : ₹{income}")
print(f"Total Expenses  : ₹{expenses}")
print(f"Total Savings   : ₹{savings}")
print(f"Savings Rate    : {rate:.2f}%")

print("\n── Spending by Category ──")
for category, amount in by_category.items():
    print(f"{category:<15} : ₹{amount}")

print("\n── Monthly Spending ──")
for month, amount in by_month.items():
    print(f"{month}      : ₹{amount}")

#
visualizer.plot_spending_by_category(by_category)
visualizer.plot_expense_distribution(by_category)
visualizer.plot_monthly_trend(by_month)

#
visualizer.generate_dashboard(income, expenses, savings, rate)

print("\n" + "=" * 40)
print("Charts saved to output/charts/")
print("Dashboard saved to output/dashboard.html")
print("=" * 40)