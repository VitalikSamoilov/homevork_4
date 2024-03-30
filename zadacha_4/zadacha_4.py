contacts = {}
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid format."
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."

def change_contacts(args, contacts):
    if len(args) != 2:
        return "Invalid format"
    name, phone = args
    if name.lower() in contacts:
        contacts[name.lower()] = phone
        return "Contacts apdated."
    else:
        return "Contacts not found"

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid format."
    name = args[0].lower()
    if name in contacts:
        return contacts[name]
    else:
        return "Contacts not found"

def show_all(contacts):
    return [f"{name}: {phone}" for name, phone in contacts.items()]  


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contacts(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()            

