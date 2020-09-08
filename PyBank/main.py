# import modules
import os
import csv

# file reading location
csvpath = os.path.join("Resources", "budget_data.csv")

# reading file using CSV module
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Count total months
    # It worked, but I don't even know why. What does "1" mean ?)
    total_month = sum(1 for row in csvreader)
    
    # Count profit total
    # I was thinking to insert a for loop from this line but failed. Something like
    #total_profit=[]
    #for row in csvreader:
    #total_profit.append(int(row(1)))
    
    # Count average change
    # Dunno how to do

    # look uo the greatest increase in profits
    # Dunno how to do
    
    # look up the greatest decrease in profits
    # Dunno how to do

    # print in terminal
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: " + str(total_month))
    #print("Total: $" + str(sum(total_profit))
    #print("Average Change: $" + str(average_change))
    #print("Greatest Increase in Profits: ")
    #print("Greatest Decrease in Profits: ")

#Zip lists together
#cleaned_csv = zip(total_month, total_profit, average_change, Greatest Increase in Profits,
#             Greatest Decrease in Profits)

# File output location
# output_file = os.path.join("analysis", "results.txt")

# Open the output file
# with open(output_file, "w") as datafile:
       #writer = csv.writer(datafile)

# Write the header row
    #writer.writerow(["total_month", "total_profit", "average_change", "Greatest Increase in Profits",
                     # "Greatest Decrease in Profits"])

 # Write in zipped rows
    # writer.writerows(cleaned_csv)