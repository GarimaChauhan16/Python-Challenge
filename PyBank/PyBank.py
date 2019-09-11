import os
import csv

# csv File Read
csvpath = os.path.join('..','Resources', 'budget_data.csv')
with open (csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter =',')
    csv_header=next(csvreader)

# Total month and Total profit 
    Profits=[]
    Date=[]
    for row in csvreader:
        Date.append(row[0])
        Profits.append(float(row[1]))
    total_months= len(Date)
    print(f'Total Months = {total_months}')
    total_profit= 0
    for i in range(len(Profits)):
        total_profit=total_profit + Profits[i]
    print(f'Total: $ {float(total_profit)}')

# Average Change 
    change=[]
    for i in range(1, len(Profits)):
        monthly_change= Profits[i]- Profits[i-1]
        change.append(monthly_change)
    total_change=0
    for i in range(len(change)):
        total_change= total_change + change[i]
    Average_change= total_change/len(change)
    print(f'Average Change = $ {float(Average_change)}')

# Greatest Increase and Decrease in Profits 
    Greatest_Increase= 0
    Greatest_Decrease= 0
    for i in range(len(change)):
        if change[i]>= Greatest_Increase:
            Greatest_Increase = change[i]
        if change[i]<= Greatest_Decrease:
            Greatest_Decrease = change[i]
    print(f'Greatest Increase in Profits = $ {Greatest_Increase}')
    print(f'Greatest Decrease in Profits = $ {Greatest_Decrease}')

# Index of Greatest Increase and Greatest Decrease Values
    inc_indx = change.index(Greatest_Increase)
    dec_indx = change.index(Greatest_Decrease)
    Greatest_Increase_Date = Date[inc_indx+1]
    Greatest_Decrease_Date = Date[dec_indx+1]
    print(f'Greatest Increase in Profits = {Greatest_Increase_Date} ($ {Greatest_Increase})')
    print(f'Greatest Decrease in Profits = {Greatest_Decrease_Date} ($ {Greatest_Decrease})')

# Write a text file
output_path = 'PyBank_Output.txt'
with open(output_path, 'w') as text_file:
    text_file.write('Financial Analysis\n')
    text_file.write('----------------------------------\n')
    text_file.write(f'Total Months = {total_months}\n')
    text_file.write(f'Total: $ {float(total_profit)}\n')
    text_file.write(f'Average Change = $ {float(Average_change)}\n')
    text_file.write(f'Greatest Increase in Profits = {Greatest_Increase_Date} ($ {Greatest_Increase})\n')
    text_file.write(f'Greatest Decrease in Profits = {Greatest_Decrease_Date} ($ {Greatest_Decrease})\n')