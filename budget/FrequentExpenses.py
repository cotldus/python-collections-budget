import collections
from . import Expense
import matplotlib.pyplot as plt

#Read in the Spending Data
expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

#Create a List of the Spending Categories
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

#Count Categories with a Counter Collection
spending_counter = collections.Counter(spending_categories)

#Get the Top 5 Categories
top5 = spending_counter.most_common(5)

categories, count = zip(*top5)

#Plot the Top 5 Most Common Categories
fig, ax = plt.subplots()

#Create the bar chart
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

#Display the graph
plt.show()