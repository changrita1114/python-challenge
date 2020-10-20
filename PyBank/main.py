# Credit: Ryan Boris 

# import modules
import os
import csv

# file reading location
csvpath = os.path.join("Resources", "budget_data.csv")

dates = []
profits_losses = []

# reading file using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Read the header row first
    csv_header = next(csvreader)
    
    # Making data into the dates and profits_losses lists
    for row in (csvreader):
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# # Count total mounths
# print(len(dates))
# # Count total amounts
# print(sum(profits_losses))
# Count average change
cumulatives =[]
for index, item in enumerate(profits_losses):
    try:
        price =  profits_losses[index]
        next_price = profits_losses[index + 1]
        cumulatives.append(next_price - price)
    except IndexError:
        pass

average_change = round(sum(cumulatives)/len(cumulatives),2)

# look uo the greatest increase and decrease in profits
max_increase = max(cumulatives)
min_decrease = min(cumulatives)

max_index = cumulatives.index(max_increase)
min_index = cumulatives.index(min_decrease)

# print in terminal
print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(len(dates)))
print("Total: $" + str(sum(profits_losses)))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + dates[max_index +1] + " $" + str(max_increase))
print("Greatest Decrease in Profits: " + dates[min_index +1] + " $" + str(min_decrease))