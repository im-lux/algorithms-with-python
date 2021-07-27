import random

def lottery_numbers(quantity):
    list_of_numbers = []

    while True:
        if len(list_of_numbers) == quantity:
            break

        random_num = random.randint (1, 1000)

        if random_num not in list_of_numbers:
            list_of_numbers.append(random_num)

    return list_of_numbers

def main():
    print ("Welcome to the Lottery number generator game!")

    quantitiy_quetion = input("Type in how many numbers you would like to generate: ")

    try:
        quantity_num = int(quantitiy_quetion)
        print (lottery_numbers(quantity_num))
    except ValueError:
        print ("Please enter a number.")

    print ("END")

if __name__ == "__main__":
    main()