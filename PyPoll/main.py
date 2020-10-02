# Homework Python Challenge by Jose Luis Duarte Alcantara
# PyPoll

import os
import csv

# Read the csv file
election_data_csv = os.path.join("Resources","election_data.csv")

# Then store the contents of candidates, votes, percent & totals into Python Lists.
candidates =["Khan","Correy","Li","O'Tooley"]
votes=[]
cand_vote=[]
cand_tot_votes=[]
cand_perc_votes=[]

# Open and read the csv file to append data into the lists
with open(election_data_csv, "r", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile)

    # Because my file had a header, I should use:
    header = next(csvreader)
    khan=0
    correy=0
    li=0
    otooley=0
    
    # Create two list for votes & candidates votes
    for row in csvreader:
        votes.append(row[0])
        cand_vote.append(row[2])
        
    # Calculate and create a list for all the diferences between day(t+1) - day(t)
    for x in cand_vote:
        if x == candidates[0]:
            khan = khan + 1
        elif x == candidates[1]:
            correy = correy + 1
        elif x == candidates[2]:
            li = li +1
        elif x == candidates[3]:
            otooley = otooley + 1


# Set the final values
total_votes = len(votes)
cand_tot_votes = (khan,correy,li,otooley)
cand_perc_prev=((khan/total_votes)*100,(correy/total_votes)*100,(li/total_votes)*100,(otooley/total_votes)*100)
cand_perc_votes=(round(cand_perc_prev[0],4),round(cand_perc_prev[1],4),round(cand_perc_prev[2],4),round(cand_perc_prev[3],4))
winner = max(cand_tot_votes)
index_win = cand_tot_votes.index(winner)

# Print the Financial Analysis
print("")
print("Election Results")
print("-------------------------------")
print(f" Total Votes:", str(total_votes))
print("-------------------------------")
index_z = 0
for z in candidates:
    index_z = candidates.index(z)
    print(f" {candidates[index_z]}: {cand_perc_votes[index_z]:.3f}% ({cand_tot_votes[index_z]})")
print("-------------------------------")
print(f" Winner:", candidates[index_win])
print("-------------------------------")

# Create output file Financial_Analysis.txt
f = open('analysis/Election_Results.txt','w')
f.write("\n")
f.write("Election Results")
f.write("\n")
f.write("-------------------------------")
f.write("\n")
f.write("Total Votes:")
f.write(str(total_votes))
f.write("\n")
f.write("-------------------------------")
f.write("\n")
for w in candidates:
    index_w = candidates.index(w)
    f.write(str(candidates[index_w]))
    f.write(":")
    f.write(f'{cand_perc_votes[index_w]:.3f}')
    f.write("% (")
    f.write(str(cand_tot_votes[index_w]))
    f.write(")")
    f.write("\n")
f.close()