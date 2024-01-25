#
# income = float(input("Please enter your income: "))
#
# if income <= 10000:
#     print("You are broke and do not have to pay tax!!")
# elif  income <= 10000:
#     tax = income * .10
#     print("Tax rate is 10%. You will pay {}".format(tax))
# elif income <= 50000:
#     tax = income * .20
#     print("Tax rate is 20%. You will pay {}".format(tax))
# else:
#     tax = income * .30
#     print("Tax rate is 30%. You will pay {}".format(tax))
#
#
#
#
# WHILE
# Write a program that repeatedly asks the user to enter a positive number until they enter a negative number.
# Then, print the sum of all positive numbers entered.


# total = 0
# while True:
#     number = int(input("Please enter a positive number:"))
#     if number >= 0:
#         total += number
#     else:
#         break
# print(total)


userInput = ""
while True:
    userInput = input("Please enter a string: ")
    if userInput.lower() == "exit":
        break
    else:
        print(userInput)








# start = 50
# while True:
#     print(start)
#     if start > 25:
#         start = start - 5
#     else:
#         break


# for x in reversed(range(51)):
#     if (x % 5) == 0 and x >= 25:
#         print(x)



