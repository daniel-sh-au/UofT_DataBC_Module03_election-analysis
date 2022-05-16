# The data we need to retrieve.
# 1. The total num of votes cast
# 2. A compelte list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# The winner of the elction basec on popular vote

# dependencies
import os
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)