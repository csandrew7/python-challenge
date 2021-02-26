#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#As an example, your analysis should look similar to the one below:
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.


#Modules
import os
import csv

#Variables
total_votes = 0
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

#path for file

csvpath = os.path.join( "Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

#calculate votes
    for row in csvreader:
        total_votes += 1

        if (row[2] == "Khan"):
            khan_total += 1
        elif (row[2] == "Correy"):
            correy_total += 1
        elif (row[2] == "Li"):
            li_total += 1
        else:
            otooley_total += 1

#calculate percentages
khan_percent = khan_total/total_votes
correy_percent = correy_total/total_votes
li_percent = li_total/total_votes
otooley_percent  = otooley_total/total_votes

#calculate winner
winner = max(khan_total,correy_total,li_total,otooley_total)

if winner == khan_total:
    winners_name = "Khan"
elif winner == correy_total:
    winners_name = "Correy"
elif winner == li_total:
    winners_name = "Li"
else:
    winner_name = "O Tooley"

#Print
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Khan: {khan_percent:.3%} ({khan_total})")
print(f"Correy: {correy_percent:.3%} ({correy_total})")
print(f"Li:{li_percent:.3%} ({li_total})")
print(f"O Tooley:{otooley_percent:.3%} ({otooley_total})")
print(f"-------------------------")
print(f"Winner:{winners_name}")
print(f"-------------------------")


#Export Text File
analysis_file = os.path.join("analysis", "analysis.text")
with open(analysis_file, "w") as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Khan: {khan_percent:.3%}({khan_total})\n")
    textfile.write(f"Correy: {correy_percent:.3%}({correy_total})\n")
    textfile.write(f"Li: {li_percent:.3%}({li_total})\n")
    textfile.write(f"O Tooley: {otooley_percent:.3%}({otooley_total})\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Winner: {winners_name}\n")
    textfile.write(f"-------------------------\n")