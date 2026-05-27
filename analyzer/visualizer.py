import matplotlib.pyplot as plt
import seaborn as sns
from jinja2 import Environment, FileSystemLoader

def generate_dashboard(income, expenses, savings, rate):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('dashboard.html')

    html_content = template.render(
        income = round(income,2),
        expenses = round(expenses,2),
        savings = round(savings,2),
        rate=round(rate, 2),
    )
    with open('output/dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

def plot_spending_by_category(by_category):
    plt.figure(figsize=(10,6)) # means 10 inches wide and 6 inches tall. Think of this as deciding your paper size before drawing.
    sns.barplot(x=by_category.index, y= by_category.values)
    plt.title('Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount(INR)')
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.savefig('output/charts/category_spending.png')
    plt.close()


def plot_expense_distribution(by_category):
    plt.figure(figsize=(8,8))
    plt.pie(by_category.values, labels = by_category.index, autopct='%1.1f%%')
    plt.title('Expense Distribution')
    plt.tight_layout()
    plt.savefig('output/charts/expense_distribution.png')

def plot_monthly_trend(by_month):
    months = by_month.index.astype(str) # This converts 2024-01 to plain string "2024-01". Safe to plot now.
    plt.figure(figsize=(10,6))
    plt.plot(months, by_month, marker = 'o')
    plt.title('Monthly Spending Trend')
    plt.xlabel('Month')
    plt.ylabel('Amount(INR)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/charts/monthly_trend.png')
    plt.close()
