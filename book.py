class Contact:
    def __init__(self, first_name, last_name, birth_year, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.phone_number = phone_number
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

def main():
    print ("Welcome to your Contact List!")
    john = Contact(first_name="John", last_name="Clark", phone_number="89348239429", birth_year="1979",
                   email="john@clark.com")
    marissa = Contact(first_name="Marissa", last_name="Mayer", phone_number="83483204032", birth_year="1978",
                      email="marissa@yahoo.com")
    bruce = Contact(first_name="Bruce", last_name="Wayne", phone_number="902432309443", birth_year="1939",
                    email="bruce@batman.com")

    contacts = [john, marissa, bruce]

    while True:
        print ("") 
        print ("Please choose one of these options:")
        print ("a) See all your contacts")
        print ("b) Add a new contact")
        print ("c) Edit a contact")
        print ("d) Delete a contact")
        print ("e) Quit the program.")
        print ("")  

        option = input("Please select one of your options (a, b, c, d, e): ")

        if option.lower() == "a":
            list_all_contacts(contacts)
        elif option.lower() == "b":
            add_new_contact(contacts)
        elif option.lower() == "c":
            edit_contact(contacts)
        elif option.lower() == "d":
            delete_contact(contacts)
        elif option.lower() == "e":
            print ("Thank you for using Contact List. Goodbye!")
            break
        else:
            print ("Sorry, I didn't understand your selection. Please try again.")
            continue

def list_all_contacts(contacts):
    for index, person in enumerate(contacts):
        print ("ID: " + str(index))
        print (person.get_full_name())
        print (person.birth_year)
        print (person.phone_number)
        print (person.email)
        print ("")

    if not contacts:
        print ("You don't have any contacts in your Contact list.")

def add_new_contact(contacts):
    first_name = input("Please enter contact's first name: ")
    last_name = input("Please enter contact's last name: ")
    email = input("Please enter contact's email address: ")
    phone = input("Please enter contact's phone number: ")
    birth_year = input("Please enter contact's birth year: ")

    new = Contact(first_name=first_name, last_name=last_name, phone_number=phone, birth_year=birth_year, email=email)
    contacts.append(new)

    print ("")
    print (new.get_full_name() + " was successfully added to your list!")

def edit_contact(contacts):
    print ("Select the number of the contact you'd like to edit:")

    for index, person in enumerate(contacts):
        print (str(index) + ") " + person.get_full_name())

    print ("")
    selected_id = input("What contact would you like to edit? (enter ID number): ")
    selected_contact = contacts[int(selected_id)]

    new_email = input("Please enter a new email address for %s: " % selected_contact.get_full_name())
    selected_contact.email = new_email

    print ("")
    print ("Email updated.")
    #...

def delete_contact(contacts):
    print ("Select the number of the contact you'd like to delete:")

    for index, person in enumerate(contacts):
        print (str(index) + ") " + person.get_full_name())

    print ("") 
    selected_id = input("What contact would you like to delete? (enter ID number): ")
    selected_contact = contacts[int(selected_id)]

    contacts.remove(selected_contact)
    print ("")
    print ("Contact was successfully removed from your contact list.")

if __name__ == "__main__":
    main()