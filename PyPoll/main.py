# import modules
import os
import csv

# file reading location
csvpath = os.path.join("Resources", "election_data.csv")
# reading file using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Read the header row first
    csv_header = next(csvreader)
    # Define varibles
    total_votes = 0
    khan_count =0
    correy_count = 0
    li_count = 0
    otooley_count = 0
    for row in csvreader:
        total_votes += 1
        if row[2] == 'Khan':
           khan_count += 1
        if row[2] == 'Correy':
           correy_count +=1
        if row[2] == 'Li':
           li_count +=1
        if row[2] == "O'Tooley":
           otooley_count +=1

    percent_khan = (khan_count / total_votes)*100
    percent_correy = (correy_count / total_votes)*100
    percent_li = (li_count / total_votes)*100
    percent_otooley = (otooley_count / total_votes)*100
    
    print("Election Results")
    print("-----------------------")
    print("Total Votes: " +str(total_votes))
    print("-----------------------")
    print("Khan: " + str(round(percent_khan, 2)) + "% (" + str(khan_count)+ ")")
    print("Correy: " + str(round(percent_correy, 2)) + "% (" + str(correy_count)+ ")")
    print("Li: " + str(round(percent_li, 2)) + "% (" + str(li_count)+ ")")
    print("O'Tooley: " + str(round(percent_otooley, 2)) + "% (" + str(otooley_count)+ ")")
    print("-----------------------")
    print("Winner: Khan")