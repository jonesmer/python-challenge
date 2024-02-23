import csv
import os

#create path strings
csvpath = os.path.join("Resources", "election_data.csv")
outputPath=os.path.join("Analysis", "election_analysis.txt")

# blank library
votesDict = {}

totalVotes = 0
voteStr = ""
winName = ""
winVotes = 0

#open csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # loop through the rows of data
    for row in csvreader:

        # we don't want the headers in the calcs, store them
        if row[0] == "Ballot ID":
            header1 = row[0]
            header2 = row[1]
            header3 = row[2]
        else:
            candName = row[2]

            # if name is already in the dictionary, add 1 to their tally, also tally total vote
            if candName in votesDict:
                votesDict[candName] = votesDict[candName] + 1
                totalVotes = totalVotes + 1

            # if it's a new name, start a new tally in dictionary, add to total votes
            else:
                votesDict[candName] = 1
                totalVotes = totalVotes + 1

# go through completed dictionary to calculate percentages, determine a winner
for x in votesDict:
    cName = x
    cVotes = votesDict[x]
    cPct = round((cVotes/totalVotes)*100,3)

    # string to add into printed results
    voteStr = voteStr + f"\n{cName}: {cPct}% ({cVotes})\n"
    if cVotes > winVotes:
        winVotes = cVotes
        winName = cName

results = f"Election Results\n\n----------------------------\n\nTotal Votes: {totalVotes}\n\n----------------------------\n" + voteStr + f"\n----------------------------\n\n Winner: {winName}\n\n----------------------------"

# print results
print("\n"+results+"\n")

# save results into txt file
with open(outputPath,'w') as output_file:
    output_file.write(results)
        