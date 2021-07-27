import random

def main():
    country_capital = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Austria": "Vienna", "Hungary": "Budapest",
                        "Italy": "Rome", "Slovakia": "Bratislava", "Czech Republic": "Prague"}

    while True:
        random_num = random.randint(0, 6)
        selected_country = country_capital.keys()[random_num]

        guess = input("What is the capital city of %s?" % selected_country)

        check_guess (guess, selected_country, country_capital)

        new = input("Would you like to continue playing the game? (yes/no) ")
        if new == "no" or new == "n":
            break

    print ("Thank you for playing the game! BYE")

def check_guess (user_guess, country, country_capital):
    capital = country_capital.get(country)

    if user_guess == capital:
        print ("Correct! The capital of %s is %s!" % (country, capital))
        return True
    else:
        print ("Sorry! The capital of %s is %s." % (country, capital))
        return False

if __name__ == "__main__":
    main()