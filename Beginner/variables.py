#1.create a variable named pi and store the value 22/7 in it. check the data type of this variable

pi = 22/7
print(type(pi))

#2. create a variable called for and assign it a value 4. See what happens and find out the reason behind the  behaviour that you see
#for = 4
#print(for)
# invalid syntax 


# 3. Store the principal amount, rate of interest, and time in
# different variables and then calculate the Simple Interest for 3
# years. Formula: Simple Interest = P x R x T / 100

principal_amount = 500.99
interest_rate = 10.09
time = 3

simpleInterest = principal_amount * interest_rate * time / 100

print('Simple Interest for 3years: ', format(simpleInterest, '.2f'))
