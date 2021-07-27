import random

def main():
    secret = random.randint(1, 50)

    while True:
        guess = int(input("Search for a secret number! (Between 1 and 50) :"))

        if guess == secret:
            print ("Congratulations! Secret number is %s!" % secret)
            break
        elif guess > secret:
            print ("Try something smaller!")
        elif guess < secret:
            print ("Try something bigger!")
        else:
            print ("Please type in a number.")

if __name__ == "__main__":
    main ()