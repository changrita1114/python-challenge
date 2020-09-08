## import modules
import os
import csv

## file reading location
csvpath = os.path.join("Resources", "election_data.csv")

## Define the fuction and have it accept the 'election_data' as its sole parameter
## I followed "wrestling_functions.py." Dunno why the problem shows here for the Candidate.
def print_percentages(election_data):
    Candidate = str(election_data[2])

## store variables
# votes for Khan
# votes_1 =[]
# votes for Correy
# votes_1 =[]
# votes for Li
# votes_1 =[]
# votes for O'Tooley
# votes_1 =[]

## reading file using CSV module
with open(csvpath) as csvfile:
    
    ## CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    ## Read the header row first
    csv_header = next(csvreader)
    
    ## I was think to do a for loop to read through all the lines and classify cadidates,
    ## and just got stuck. Dunno how to classify
    ## for candidate in csvreader:

    ## Count total votes
    ## It worked, but I don't even know why. What does "1" mean ?)
    total_votes = sum( 1 for row in csvreader)

    ## I was thinking to count every candidate's vote, but there is something wrong here.
    ##percent_Khan
    ##votes_1
    #for row in csvreader:
     #   Khan = 0
      #  if row[2] == Khan:
       # Khan += row
    #pritn(row)

    # percent_1 = votes_1 / total_votes
    
    ## percent_Correy
    # percent_2 = votes_2 / total_votes
    
    ## percent_Li
    # percent_3 = votes_3 / total_votes
    
    ## percent_O'Tooley
    # percent_4 = votes_4 / total_votes
    
    ## decide winner
    # winner = max(percent_1,percent_2,percent_3,percent_4)

    print("Election Results")
    print("-----------------------")
    print("Total Votes: " +str(total_votes))
    print("-----------------------")
    #print("Khan: " + str(percent_1) + " %")
    #print("Correy: " + str(percent_2) + " %")
    #print("Li: " + str(percent_3) + " %")
    #print("O'Tooley: " + str(percent_4) + " %")
    print("-----------------------")
    #print("Winner: " + str(winner))

#Zip lists together
#cleaned_csv = zip(total_votes, percent_1, percent_2, percent_3, percent 4, winner)

# File output location
# output_file = os.path.join("analysis", "results.txt")

# Open the output file
# with open(output_file, "w") as datafile:
       #writer = csv.writer(datafile)

# Write the header row
    #writer.writerow(["total_votes", "percent_1", "percent_2", "percent_3",
                     # "percent_4", "winner"])

 # Write in zipped rows
    # writer.writerows(cleaned_csv)