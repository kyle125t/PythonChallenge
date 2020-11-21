import os
import csv

# The total number of votes cast
vote_count = 0
# A complete list of candidates who received votes
candidate_list = []
# The percentage of votes each candidate won
votes = []
# The total number of votes each candidate won
# The winner of the election based on popular vote.

file_path = os.path.join("Resources", "election_data.csv")

with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    row = next(csv_reader)
# three columns = Voter ID, County, Candidate
    for row in csv_reader:
        vote_count += 1
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            votes.append(1)
        else:
            candidate_votes = candidate_list.index(candidate)
            votes[candidate_votes] += 1
    
    # individual_votes = zip(candidate_list, votes)
    # print(list(individual_votes))
    # print(vote_count)
    # print(candidate_list)
    # print(votes)
   
percentage = []
c_votes = votes[0]
c_index = 0
for count in range(len(candidate_list)):
    vote_percentage = (votes[count]/vote_count)*100
    percentage.append(vote_percentage)
    
    if votes[count] > c_votes:
        c_votes = votes[count]
        print(c_votes)
        c_index = count
winner = candidate_list[c_index]
# formatted_percentage = ["%.3f" % elem for elem in percentage]


print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
for count in range(len(candidate_list)):
    # print(f"{candidate_list[count]}: {formatted_percentage[count]}% ({votes[count]})")
    print(f"{candidate_list[count]}: {percentage[count]}% ({votes[count]})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

election_analysis = os.path.join("Analysis", "election_results.txt")
with open(election_analysis, "w") as text:
    text.write("-------------------------" + "\n")
    text.write("Election Results" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Total Votes: {vote_count}" + "\n")
    text.write("-------------------------" + "\n")
    for count in range(len(candidate_list)):
        # text.write(f"{candidate_list[count]}: {formatted_percentage[count]}% ({votes[count]})")
        text.write(f"{candidate_list[count]}: {percentage[count]}% ({votes[count]})" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write("-------------------------" + "\n")