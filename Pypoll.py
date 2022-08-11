# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users/gmulat/Desktop/Classwork/Homework Repositories/projects/Election_Analysis-/election_result.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users/gmulat/Desktop/Classwork/Homework Repositories/projects/Election_Analysis-/analysis/election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# declare empty dictionary 
candidate_votes = {}

# winning candidates and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
        
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0

        # Add votes to the candidate count
        candidate_votes[candidate_name] += 1
         # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
     election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
print(election_results, end="")
    # Save the final vote count to the text file.
txt_file.write(election_results)
    #Print the candidate list
print(candidate_options)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
for candidate_name in candidate_votes:

    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    #3 calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100 
        
    #print out each candidate's name, vote count, and percentage of votes to the terminal.
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidates
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

         winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")

     # If true then set winning_count = votes and winning_percent = vote_percentage.
    winning_count = votes
    winning_percentage = vote_percentage

    # And, set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name

        # Print the candidate name and percentage of votes
    with open(file_to_save) as txtfile:

        print(winning_candidate_summary)
        election_analysis = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_analysis, end="")
        txtfile.write(election_analysis)
    print(winning_candidate_summary)
candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Print each candidate, their voter count, and percentage to the terminal.
print(candidate_results)
#  Save the candidate results to our text file.
txt_file.write(candidate_results)