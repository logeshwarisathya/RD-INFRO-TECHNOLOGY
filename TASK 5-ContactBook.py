class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name}: {contact.phone_number}")

    def search_contact(self, query):
        search_results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                search_results.append(contact)
        return search_results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def get_contact_info():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone_number, email, address)

def main():
    contact_book = ContactBook()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_contact = get_contact_info()
            contact_book.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            search_results = contact_book.search_contact(query)
            if search_results:
                print("Search Results:")
                for contact in search_results:
                    print(f"{contact.name}: {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                new_contact = get_contact_info()
                contact_book.update_contact(index, new_contact)
                print("Contact updated successfully.")
            else:
                print("Invalid index.")

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
                print("Contact deleted successfully.")
            else:
                print("Invalid index.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()




