import os

import csv



# set var to identify location of file

filepath = os.path.join('py_bank_resources', 'budget_data.csv')

print (filepath)



# # opens my file and lets cpu know file type 

with open(filepath) as csvfile:



#     # reads and iterates through my file, recognizing the delimiters

    myreader = csv.reader(csvfile, delimiter=',')

    print (myreader)



#     # set var for my header so I can exclude from my output

    the_header = next(myreader)

    print (the_header)



    # sets my file as a list.  This helps me find the length of my file/list

    thelist = list(myreader)

    print(thelist)

#     # finds the length of my list.  each month = 1 row so all rows = total months

    total_months = len(thelist)

    # print (total_months)



    totalprofits = 0

    row_index = 1

    profit_changes = 0

    average_profit_change = 0

    greatest_profit_increase = ['',0]

    greatest_profit_decrease = ['',0]





    for row in thelist:

        totalprofits = totalprofits + int(row[1])
        

#         #Finding average changes...

        if row_index < 2:

#             # No calculations on first row except to save the value

            previous_row = int(row[1])

        if row_index > 1:

#             # For second row and beyond...

            this_row = int(row[1])

            absolute_value_difference = abs(this_row - previous_row)

            if this_row < previous_row: 

#                 # If value goes down, make the difference negative

                profit_or_loss = absolute_value_difference * -1

            else:

#                 # Else keep the default positive absolute value

                profit_or_loss = absolute_value_difference

#             # Save this row for next interation calculations

            previous_row = this_row

#             # Update running tally for use in calculating average

            profit_changes += profit_or_loss

#             # Finding greatest increase/decrease in profits...

            if profit_or_loss > greatest_profit_increase[1]:

                greatest_profit_increase = [row[0], profit_or_loss]

            if profit_or_loss < greatest_profit_decrease[1]:

                greatest_profit_decrease = [row[0], profit_or_loss]

        row_index += 1

    print (total_months)

    print(totalprofits)

    print(profit_changes) 

    print(greatest_profit_increase)

    print(greatest_profit_decrease)


#     # Summary Table

    output = (
    f" \n"
    f"Financial Analysis \n"
    f"---------------------------- \n"
    f"Total Months: {total_months} \n"
    f"Total Profits: ${totalprofits} \n"
    f"Average Change: ${profit_changes} \n"
    f"Greatest Increase in Profits: {greatest_profit_increase} \n"
    f"Greatest Decrease in Profits: {greatest_profit_decrease} \n"
    )
    print(output)







# # save output as a txt file

output_path = os.path.join(".", "py_bank_analysis", "financial_analysis.txt")

# # print(output_path)



with open(output_path, "w") as output_file:

    print(output_file)

    output_file.write(output)