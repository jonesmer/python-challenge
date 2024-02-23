# import the modules needed to work with CSVs and to find files regardless of OS used
import csv
import os

#create path strings
csvpath = os.path.join("Resources", "budget_data.csv")
outputPath = os.path.join("Analysis", "budget_analysis.txt")

#initialize variables for comparisons
monthCount = 0
totalProfit = 0
prevMonth = 0
initProfit = 0
totalChange = 0
maxMonth = ""
maxChange = 0
minMonth = ""
minChange = 0

#open csv
with open(csvpath, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    # loop through the rows of data
    for row in csvreader:

        # we don't want the headers in the calcs, store them
        if row[0] == "Date":
            header1 = row[0]
            header2 = row[1]
        else:
            # add to month tally and total profit
            monthCount = monthCount + 1            
            monthlyChange = int(row[1]) - prevMonth
            prevMonth = int(row[1])

            # only want to record the initial profit once, totalProfit is same number
            if monthCount == 1: 
                initProfit = prevMonth
                totalProfit = prevMonth
                changeMonth = 0
            # for the rest of the rows, total profit and month count will accumulate
            else:
                totalProfit = totalProfit + int(row[1])
                changeMonth = changeMonth + 1
            
            # compare current change to max and min; overwrite if either case is true
            if monthlyChange > maxChange:
                maxMonth = row[0]
                maxChange = monthlyChange
            elif monthlyChange < minChange:
                minMonth = row[0]
                minChange = monthlyChange

    # calc avg, based on changeMonths (months - 1 because we didn't calc change in month 1)
    avgChange = round((prevMonth - initProfit) / changeMonth, 2)

    # adjust any negative numbers so that we can put '-' before the '$' in results string
    minChange = minChange * (-1)
    if avgChange < 0:
        avgString = "-$" + str(avgChange*(-1))
    else: avgString = "$" + str(avgChange)
    
    
results = f"Financial Analysis\n\n----------------------------\n\nTotal Months: {monthCount}\n\nTotal: ${totalProfit}\n\nAverage Change: {avgString}\n\nGreatest Increase in Profits: {maxMonth} (${maxChange})\n\nGreatest Decrease in Profits: {minMonth} (-${minChange})"

# print results
print("\n"+results +"\n")

# save results into txt file
with open(outputPath,'w') as output_file:
    output_file.write(results)