from . import Expense
import matplotlib.pyplot as plt
import timeit

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    # 5.6 Use categorize_set_comprehension
    divided_set_comp = expenses.categorize_set_comprehension() 

    #5.7 Check that the categorized sets are equal
    if divided_set_comp != divided_for_loop:
        print('Sets are NOT equal by == test')
    
    #5.8 Create for loop for subset test
    for a,b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print("Sets are NOT equal by subset test")
    
    #6.2-4
    print(timeit.timeit(stmt = "expenses.categorize_for_loop()",
                        setup=
                        '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
                        ''',
                        number=100000,
                        globals=globals()))
    
    #6.5 Duplicate the timeit.timeit() call for set comprehension
    print(timeit.timeit(stmt = "expenses.categorize_set_comprehension()",
                        setup=
                        '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
                        ''',
                        number=100000,
                        globals=globals()))

    # 6.6- 6.7
    fig, ax = plt.subplots()
    labels = ['Necessary', 'Food', 'Unnecessary']

    # 6.8-11 Sum the amounts in each set
    divided_expenses_sum = []
    for category_exps in divided_set_comp:
        divided_expenses_sum.append(sum(x.amount for x in category_exps))
    
    ax.pie(divided_expenses_sum, labels = labels, autopct = '%1.1f%%') # This will format the percentage
    
    plt.show()

if __name__ == "__main__":
    main()