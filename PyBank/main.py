# Homework Python Challenge by Jose Luis Duarte Alcantara
# Pybank

import os
import csv

# Read the csv file
budget_csv = os.path.join("Resources","budget_data.csv")

# Then store the contents of the Date, Profit/Losses into Python Lists.
month =[]
profit_losses=[]
diference_pl=[]
diference_month=[]

# Open and read the csv file to append data into the lists
with open(budget_csv, "r", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile)

    # Because my file had a header, I should use:
    header = next(csvreader)
    total_PL = 0
    pl_prev = 0
    for row in csvreader:
        month.append(row[0])
        profit_losses.append(int(row[1]))
        # To calculate and create a list for all the diferences between day(t+1) - day(t)
        if pl_prev != 0:
            diference = int(row[1]) - pl_prev
            diference_pl.append(diference)
            diference_month.append(row[0])
        pl_prev = int(row[1])
        
    total_month = len(month)
    total_PL = sum(profit_losses)    
 
    

# Set the final values
maximo = max(diference_pl)
minimo = min(diference_pl)
row_month_max = diference_pl.index(maximo) + 1
row_month_min = diference_pl.index(minimo) + 1
month_max = month[row_month_max]
month_min = month[row_month_min] 
average_chg = (sum(diference_pl)/len(diference_pl))

# Print the Financial Analysis
print ("")
print("Financial Analysis")
print("-------------------------------")
print(f" Total Months:", str(total_month))
print(f" Total: $", total_PL)
print(f" Average Change: $", round(average_chg,2))
print(f" Greatest Increase in Profits: {month_max} (${str(max(diference_pl))})")
print(f" Greatest Decrease in Profits: {month_min} (${str(min(diference_pl))})")

# Create output file Financial_Analysis.txt
f = open('analysis/Financial_Analysis.txt','w')
f.write("Financial Analysis\n")
f.write("-------------------------------\n")
f.write(" Total Months:")
f.write(str(total_month))
f.write("\n")
f.write(" Total: $")
f.write(str(total_PL))
f.write("\n")
f.write(" Average Change: $")
f.write(str(round(average_chg,2)))
f.write("\n")
f.write(" Greatest Increase in Profits: ")
f.write(str(month_max))
f.write(" ($")
f.write(str(max(diference_pl)))
f.write(")")
f.write("\n")
f.write(" Greatest Decrease in Profits: ")
f.write(str(month_min))
f.write(" ($")
f.write(str(min(diference_pl)))
f.write(")")
f.write("\n")
f.close()
