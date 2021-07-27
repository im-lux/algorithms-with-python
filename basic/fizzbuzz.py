print ("Welcome to FIZZBUZZ game!!!")

guess = int(input("Select a number between 1-100: "))

for num in range(1, guess+1):
    if num % 3 == 0 and num % 5 == 0:
        print ("FIZZBUZZ")
    elif num % 5 == 0:
        print ("buzz")
    elif num % 3 == 0:
        print ("fizz")
    else:
        print (num)