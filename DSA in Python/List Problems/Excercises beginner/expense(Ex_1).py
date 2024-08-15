expenses = [2200, 2350, 2600, 2130, 2190]

print("In february you spent ", expenses[1] - expenses[0], " more than january.")

print("In the first quarter you spent ", expenses[0] + expenses[1] + expenses[2])

if 2000 in expenses:
    print("2000 spent in a month.")
else:
    print("No such expense found.")

expenses.append(1980)

expenses[3] -= 200
print(expenses)
