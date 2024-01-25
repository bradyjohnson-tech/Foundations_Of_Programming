def divisible_by_zero_check():
    while True:
        try:
            num_1, num_2 = map(int, input("Please enter two two positive integers separated by a comma: ").split(','))
        except ValueError:
            print("You did not format your input correctly please make sure you comma separate TWO positive integers.")
            continue
        except UnboundLocalError:
            print("You did not format your input correctly please make sure you comma separate TWO positive integers.")
            continue
        except:
            print("I am not sure what you did wrong but try again with a little more effort please.")
            continue

        if num_1 <= 0 or num_2 <= 0:
            print("One or more of the numbers you entered are not greater than 0.")
        if num_1 % num_2 == 0 or num_2 % num_1 == 0:
            return True
        else:
            print("The positive integers you entered are not divisible by one another.")


if divisible_by_zero_check():
    print("The numbers you entered are divisible by each other: True")
