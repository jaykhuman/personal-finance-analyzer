
def get_total_income(df):
# First filter rows where Amount is positive, then pick Amount column, then sum it, then return it.
     total = df[df['Amount'] > 0]['Amount'].sum()
     return total

def get_total_expenses(df):
     total = df[df['Amount'] < 0]['Amount'].sum()
     return total * -1

def get_savings(df):
     income = get_total_income(df)
     expenses = get_total_expenses(df)
     savings = income - expenses
     rate = (savings / income) * 100
     return savings, rate

def get_spending_by_category(df):

     expense = df[df['Amount']<0]
     summary = expense.groupby('Category')['Amount'].sum()
     summary = summary * -1
     summary = summary.sort_values(ascending=False)
     return summary

def get_monthly_spending(df):
     expenses = df[df['Amount'] < 0].copy()
     expenses['Month'] = expenses['Date'].dt.to_period('M')
     monthly_totals = expenses.groupby('Month')['Amount'].sum()
     monthly_totals = monthly_totals * -1
     return monthly_totals