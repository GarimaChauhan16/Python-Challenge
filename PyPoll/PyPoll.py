import os
import csv

# csv File Read
csvpath = os.path.join('..','Resources', 'election_data.csv')
with open (csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter =',')
    csv_header=next(csvreader)

# Create Indivisual Lists
    Voter_ids = []
    Counties = []
    Candidates= []
    for row in csvreader:
        Voter_ids.append(row[0])
        Counties.append(row[1])
        Candidates.append(row[2])

# The total number of votes cast
    total_votes = len(Voter_ids)
    print("----------------------------")
    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {total_votes}')
    print("----------------------------")
    
# A complete list of candidates who received votes
    unique_list =[]
    for Candidate in Candidates:
        if Candidate not in unique_list:
            unique_list.append(Candidate)
    print(f'List of Candidates: {unique_list}')
    print("------------------------------")

# The total number of votes each candidate won and Winner
    max_votes=0
    for i in range(len(unique_list)):
        vote_count= Candidates.count(unique_list[i])
        percent_votes = float((vote_count/total_votes)*100)
        print(f'{unique_list[i]}: {round(percent_votes)}% ({vote_count})')
        if vote_count >= max_votes:
            winner = unique_list[i]
            max_votes = vote_count
    print("----------------------------")
    print (f'Winner: {winner}')
    print("----------------------------")

# Write a text file    
output_path = 'PyPoll_Output.txt'
with open(output_path, 'w') as text_file:
    text_file.write('Election Results\n')
    text_file.write('------------------------------\n')
    text_file.write(f'Total Votes: {total_votes}\n')
    text_file.write('------------------------------\n')
    text_file.write(f'List of Candidates: {unique_list}\n')
    text_file.write('------------------------------\n')
    for i in range(len(unique_list)):
        vote_count= Candidates.count(unique_list[i])
        percent_votes = float((vote_count/total_votes)*100)
        text_file.write(f'{unique_list[i]}: {round(percent_votes),2}% ({vote_count})\n')
    text_file.write("----------------------------\n")
    text_file.write(f'Winner: {winner}\n')
    text_file.write("----------------------------\n")