def calculate_income_tax(income):
    result_tax = 0
    if(income < 10000):
        return result_tax
    elif(income < 20000):
        result_tax = 0.1 * (income-10000)
        return result_tax
    else:
        result_tax += 0.2 * (income-20000) + 1000
        return result_tax
    
income = int(input("Enter the income: "))
print(calculate_income_tax(income))