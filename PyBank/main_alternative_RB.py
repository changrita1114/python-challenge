import csv

# create a holder list for each feature column
dates = []
assets = []


# handle file opening
with open('resources/budget_data.csv') as file:

    # use csvreader method to format and process file data
    reader = csv.reader(file)

    # remove the header row
    header = next(reader)

    # loop over remaining values in reader
    # note each row = [0: date, 1: asset]
    # for row in reader:
    #    date = row[0]
    #    asset = row[1]
    # since row = [date, asset] this is equivalent to
    # for date, asset in reader pattern seen below
    # this pattern is called unpacking and/or destructuring

    for date, asset in reader:
        # append row[0] (date) to dates
        # dont forget all data is of type str
        # - convert as necessary
        dates.append(date)
        assets.append(int(asset))


# all data has been stored in appropriate lists for use in analysis
# therefore the code from this point does not need the open file anymore


# Q1 - How many months of data were collected?
# - the length of the list of dates would equal the number of months collected

no_of_months = len(dates)


# Q2 - What is the total revenue for the list of assets?
# - the overall total of the assets is the sum of all the assets

total_revenue = sum(assets)


# Q3 - The average of the changes of assets over the time data was collected.

changes = []

# - use a for loop with enumerate to access index and items in list
for i, asset in enumerate(assets):
    try:
        change = assets[i+1] - asset
        changes.append(change)
    # - handle exception of last value + 1 being out of bounds
    except IndexError:
        print('End of list has been reached.')

# - compute average from sum and len of list of changes
avg_of_changes = sum(changes) / len(changes)

# Q4 - Greatest increase in the list of changes

# find max change
max_change = max(changes)

# get the index for max_change
max_index = changes.index(max_change)

# use max_index to get corresponding date
# and don't forget to adjust for len(changes) == len(dates)-1
max_date = dates[max_index+1]


# Q5 - Greatest decrease in the list of changes
# follow the same logic as above, just for the min
min_change = min(changes)

min_index = changes.index(min_change)

min_date = dates[min_index+1]

# quick check of values
# format values as requested once values are acceptable
print('Q1', no_of_months)
print('Q2', f'${total_revenue:.0f}')
print('Q3', f'${avg_of_changes:.2f}')
print('Q4', max_date, f'${max_change:.0f}')
print('Q5', min_date, f'${min_change:.0f}')
