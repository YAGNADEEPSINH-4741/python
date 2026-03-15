from database import create_table
from contact_service import add_contact, view_contacts, update_contact, delete_contact

def menu():

    while True:

        print("\n===== Contact Book System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            name = input("Enter name: ")
            phone = input("Enter phone number: ")

            add_contact(name, phone)

            print("Contact added successfully!")

        elif choice == "2":

            contacts = view_contacts()

            print("\nContact List:")
            for contact in contacts:
                print(contact)

        elif choice == "3":

            contact_id = int(input("Enter contact ID to update: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")

            update_contact(contact_id, name, phone)

            print("Contact updated successfully!")

        elif choice == "4":

            contact_id = int(input("Enter contact ID to delete: "))

            delete_contact(contact_id)

            print("Contact deleted successfully!")

        elif choice == "5":

            print("Exiting program...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":

    create_table()

    menu()