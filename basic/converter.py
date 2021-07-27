print ("HELLO! Welcome to a converter that converts kilometers to miles!")

print ("Please enter a number of kilometers that you would like to convert into miles.")

while True:
    try:
        km = input("Kilometers: ")
        miles = float(km) * 0.621371192

        print (str(km) + " kilometers is " + str(miles) + " miles.")
    except:
        print ("Enter a number please!")

    choice = input("Would you like another conversion? (Type yes/no): ")

    if choice == "n" or choice == "no":
        print ("Thank you for using our converter!")
        break