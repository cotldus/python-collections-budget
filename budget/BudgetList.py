# 8 Import the Expense module
from . import Expense

# 1 Create the BudgetList class
    # Class that extends list type
class BudgetList:
    # 2 Create the constructor
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
    
    # 3 Define the append method
        # implement append so that it only appends to self if total < budget
    def append(self, item):
    # 4 Add items to expenses that are under budget
        # TODO Check if item is a number
        if (self.sum_expenses+item < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item   
    #5 Add items to overages that are over budget    
        # Otherwise append to the overages list and add to the overage total
        else:
            self.overages.append(item)
            self.sum_overages+=item
    
    # 6 Define the __len__() method
    def __len__(self):
        return len(self.expenses) + len(self.overages)


#7 Define the main function
def main():
    # Using above class
    # Set starting budget to 500
    myBudgetList = BudgetList(1200)
    
    # 9 Read in the spending data file
        # Add expenses, the last expense is 100 and that goes in overages
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')

    # 10 Add the expenses to the BudgetList
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    #11 Print the Length of myBudgetList
        # Test len()
    print('The count of all expenses: ' + str(len(myBudgetList)))


if __name__ == "__main__":
    main()

