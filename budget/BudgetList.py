# 3.8 Import the Expense module
from . import Expense
import matplotlib.pyplot as plt # 4.6

# 3.1 Create the BudgetList class
    # Class that extends list type
class BudgetList:
    # 3.2 Create the constructor
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
    
    # 3.3 Define the append method
        # implement append so that it only appends to self if total < budget
    def append(self, item):
    # 3.4 Add items to expenses that are under budget
        # TODO Check if item is a number
        if (self.sum_expenses+item < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item   
    #3.5 Add items to overages that are over budget    
        # Otherwise append to the overages list and add to the overage total
        else:
            self.overages.append(item)
            self.sum_overages+=item
    
    # 3.6 Define the __len__() method
    def __len__(self):
        return len(self.expenses) + len(self.overages)
    
    # 4.1 Create the __iter__() method
        # Create an iterable that combines self.expenses and self.overages
        # Create two local iterators for our internal lists using the default list iterator.
    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

    # 4.3/4 Create __next__()
        # Iterate first over the expenses iterator until it runs out, then switch to
        # the overages iterator. When it fails, it will return StopIteration to the caller.
    def __next__(self):
        try:
          return self.iter_e.__next__()
        except StopIteration as stop:
          return self.iter_o.__next__()


#3.7 Define the main function
def main():
    # Using above class
    # Set starting budget to 500
    myBudgetList = BudgetList(1200)
    
    # 3.9 Read in the spending data file
        # Add expenses, the last expense is 100 and that goes in overages
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')

    # 3.10 Add the expenses to the BudgetList
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    #3.11 Print the Length of myBudgetList
        # Test len()
    print('The count of all expenses: ' + str(len(myBudgetList)))

    #4.5 Test the iterable
    for entry in myBudgetList:
        print(entry)
    
    #4.7-12
        # Simple bar chart with Expenses total compared to Budget
    fig, ax = plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget] 
    ax.bar(labels, values, color=['green','red','blue'])
    ax.set_title('Your total expenses vs. total budget')
    plt.show()

# 3.12 Tell Python to run the main function
if __name__ == "__main__":
    main()

