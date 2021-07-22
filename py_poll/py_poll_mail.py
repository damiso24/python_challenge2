import os

import csv



# sets up my variable election data and tells computer where to find this file

csv_file_path = os.path.join("py_poll_resources", "election_data.csv")

print(csv_file_path)

# define and initialize variables

total_votes = 0


# Opens the file as a csv type

with open(csv_file_path) as csv_file:



#     # Sets a variable that Reads the file and recognizes the commas as delimeters

    csv_reader_damiso = csv.reader(csv_file, delimiter=",")



#     # read the header

    csv_header = next(csv_file)

    print(csv_header)



    # Inititialize Candidate Vote Tallies

    votes_for_Khan = 0

    votes_for_Correy = 0

    votes_for_Li = 0

    votes_for_OTooley = 0

    winner = {'name': '', 'votes': 0}



    # read through each row in the csv file

    for row in csv_reader_damiso:

        # Set To Variables for Readability

        voter_id = row[0]

        voter_county = row[1]

        candidate = row[2]



        # increase total votes by 1

        total_votes += 1



        # Increase Vote Count for Appropriate Candidate

        if candidate == 'Khan':

            votes_for_Khan += 1

        if candidate == 'Correy':

            votes_for_Correy += 1

        if candidate == 'Li':

            votes_for_Li += 1

        if candidate == "O'Tooley":

            votes_for_OTooley += 1



# Calculate Percentage of Votes

percentage_for_Khan = format((votes_for_Khan / total_votes) * 100, '.3f')

percentage_for_Correy = format((votes_for_Correy / total_votes) * 100, '.3f')

percentage_for_Li = format((votes_for_Li / total_votes) * 100, '.3f')

percentage_for_OTooley = format((votes_for_OTooley / total_votes) * 100, '.3f')

results = {

    'Khan': votes_for_Khan,

    'Correy': votes_for_Correy,

    'Li': votes_for_Li,

    "O'Tooley": votes_for_OTooley

}

for key, value in results.items():

    # print(key)

    # print(value)

    if value > winner['votes']:

        winner = {'name': key, 'votes': value}

    print(winner)


# Set up our summary table



output = (

    f" \n"

    f"Election Results \n"

    f"-------------------- \n"

    f"Total Votes: {total_votes} \n"

    f"-------------------- \n"

    f"Khan: {percentage_for_Khan}% ({votes_for_Khan}) \n"

    f"Correy: {percentage_for_Correy}% ({votes_for_Correy}) \n"

    f"Li: {percentage_for_Li}% ({votes_for_Li}) \n"

    f"O'Tooley: {percentage_for_OTooley}% ({votes_for_OTooley}) \n"

    f"-------------------- \n"

    f"Winner: {winner['name']}\n"

    f"-------------------- \n"

)



# Output our summary results to terminal

print(output)



# save output as a txt file

output_path = os.path.join(".", "py_poll_analysis", "election_analysis.txt")

#print(output_path)



with open(output_path, "w") as output_file:

    print(output_file)

    output_file.write(output)