# The Data We Need to Retrieve.
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

#############START PyPoll#################

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and anlyze the data here: 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read and Print the header row.
    headers = next(file_reader)
    print(headers)

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")

# Close the file
outfile.close()



##########EXTRA CODE - TO DELETE IF NOT NEEEDED################

# Write some data to the file.
#outfile.write("Countries in the Election\n-------------------------")

# Write three counties to the file.
#outfile.write("Arapahoe, ")
#outfile.write("Denver, ")
#outfile.write("Jefferson ")

#outfile.write("\nArapahoe\nDenver\nJefferson")



    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)