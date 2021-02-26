#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

# Modules
import os
import csv

# Variables
total_months = 0
total_revenue = 0
monthly_change = []
month_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0

# Set path for file
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    row = next(csvreader)
# Calculating total number of months and total revenue
    prev_profit = int(row[1])
    total_months += 1
    total_revenue += int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])
        revenue_change = int(row[1]) - prev_profit
        monthly_change.append(revenue_change)
        prev_profit = int(row[1])
        month_count.append(row[0])
        
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]

        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]
    
    avg_change = sum(monthly_change)/ len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

#Print statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:{total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: {avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${highest})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${lowest})")

#Exporting to text file.

analysis_file = os.path.join('analysis', 'analysis.text')
with open(analysis_file, 'w') as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"----------------------------\n")
    textfile.write(f"Total Months:{total_months}\n")
    textfile.write(f"Total: ${total_revenue}\n")
    textfile.write(f"Average Change: {avg_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_inc_month} (${highest})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${lowest})\n")


