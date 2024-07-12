# 1. Create a list of your friends' names. The list should have at least 5 names.
# Create a list of tuples. Each tuple should contain a friend's name and the length
# of the name.
# For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)

def createNameLengthTuples(names):
    nameLengthTuples = []  # empty list for storing tuples

    for name in names:  # looping through each name in the name list
        name_length = len(name) # length name calculation

        # getting tuple with it name and length
        name_tuple = (name, name_length)

        #add tuple name to the empty tuple list
        nameLengthTuples.append(name_tuple)

    # return the tuple length
    return nameLengthTuples

# list of friend name
friend_names = ['Mosh Hamidani', 'Dave Gray', 'Brad Traversy', 'Bro Code', 'Code Harry']

# tuples with friend names and it length
tuple_length = createNameLengthTuples(friend_names)
print(tuple_length)
print()


# 2.You and your partner are planning a trip, and you want to track expenses.
# Create two dictionaries, one for your expenses and one for your partner's
# expenses. Each dictionary should contain at least 5 expense categories and their
# corresponding amounts.
# For example:
# Your expenses
# your_expenses = {
# "Hotel": 1200,
# "Food": 800,
# "Transportation": 500,
# "Attractions": 300,
# "Miscellaneous": 200
# }
# Your partner's expenses
# partner_expenses = {
# "Hotel": 1000,
# "Food": 900,
# "Transportation": 600,
# "Attractions": 400,
# "Miscellaneous": 150
# }
# Calculate the total expenses for each of you and print the results.
# Determine who spent more money overall and print the result.
# Find out the expense category where there is a significant difference in spending
# between you and your partner.
# Print the category and the difference.

# function for the total expenses calculation
def calc_totalExpenses(expenses):
    total = 0.0     # getting the running total

    # looping through expenses
    for amount in expenses.values():
        # add amount to the total variable
        total += float(amount)

    return total

# function for significance difference in spending
def findSignificantDifference(myExpenses, partnerExpenses):
    # variables to track categories expenses and the largest difference
    maxDifference = 0
    significantCategory = ''

    # looping through in my Expenses
    for category in myExpenses:
        # Calculate the difference if the category exists in both dictionaries
        if category in partnerExpenses:
            # calculate the difference between the two expenses
           difference = abs(myExpenses[category] - partnerExpenses[category])

           # Check if this difference is larger than the current max difference
           if difference > maxDifference:
               maxDifference = difference
               significantCategory = category
    
    return (significantCategory, maxDifference)

# main function
def main():
    # dictionaries for both my partner and me expenses 
    myExpenses = {
        "Food": 500.99,
        "Transportation": 300.89,
        "Accommodation": 1200.74,
        "Entertainment": 600.08,
        "Miscellaneous": 200.89
    }

    partnerExpenses = {
        "Food": 700.99,
        "Transportation": 500.89,
        "Accommodation": 1000.74,
        "Entertainment": 800.08,
        "Miscellaneous": 150.89
    }

    # each person expenses calculation
    myTotal = calc_totalExpenses(myExpenses)
    partnerTotal = calc_totalExpenses(partnerExpenses)

    # results of the total expenses
    print(f"My total expenses: ${format(myTotal, '.2f')}")
    print(f"Partner's total expenses: ${format(partnerTotal, '.2f')}")

    # comparing who spent more money overall
    if myTotal > partnerTotal:
        print("I spent more money for this trip")
    
    elif partnerTotal > myTotal:
        print("My partner spent more money overall for this trip")
    
    else:
        print("We spent the same amount of money on this trip overall")

    # finding the expense category with most significant difference
    (significantCategory, maxDifference) = findSignificantDifference(myExpenses, partnerExpenses)

    # output of significant and max difference
    print("Category with significant difference:", significantCategory)
    print("Difference in spending:", maxDifference)

# calling the main
main()