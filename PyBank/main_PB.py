import os
import csv


profits = []
p2p_change = []
period_data = []

# The total number of months included in the dataset
total_months = 0
# The net total amount of "Profit/Losses" over the entire period
total_profit = 0
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
change_profit = 0
previous_profit = 0


budget_data_path = os.path.join("Resources", "budget_data.csv")

with open(budget_data_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    # goes through each row in file: adds months, totals P/L, tracks changes by period
    for row in csv_reader:
        # month count
        total_months += 1
        # takes date
        period_data.append(row[0])
        # ascribes profit for each date
        profits.append(row[0])
        total_profit = total_profit + int(row[1])
        end_profit = int(row[1])
        monthly_PL = end_profit - previous_profit
        # adds P/L from each month --- current and previous --- to the changes list
        p2p_change.append(monthly_PL)
        # counts changes in P/L then resets the previous month value
        change_profit = change_profit + monthly_PL
        previous_profit = end_profit
        
        avg_profit = (change_profit / total_months)

        greatest_increase = max(p2p_change)
        greatest_decrease = min(p2p_change)
        increase_period = period_data[p2p_change.index(greatest_increase)]
        decrease_period = period_data[p2p_change.index(greatest_decrease)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_profit}")
print(f"Average Change: {avg_profit}")
print(f"Greatest Increase in Profits: {increase_period} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {decrease_period} ${greatest_decrease}")

financial_file = os.path.join("Analysis", "financial_analysis.txt")
with open(financial_file, "w") as text:
    text.write("Financial Analysis"+ "\n")
    text.write("----------------------------" + "\n")
    text.write("Total Months: " + str(total_months) + "\n")
    text.write("Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("Average Change: " + '$' + str(int(avg_profit)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_period) + " ($" + str(greatest_increase) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_period) + " ($" + str(greatest_decrease) + ")\n")