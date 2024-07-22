
from command_check_decorator import command_check_decorator
from parse_input_validator import parse_input_validator

@parse_input_validator
def parse_input(cmd_string):
    cmd, *args = cmd_string.split()
    cmd = cmd.strip().lower()
    return (cmd, args)


@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: add [name] [phone number]"
        ) 
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: change [name] [new phone number]"
        ) 
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact not found."


@command_check_decorator(
        index_error_message="Error: Not enough arguments. Usage: delete [name]",
        key_error_message= "Error: Contact not found"
        ) 
def delete_contact(args, contacts):
    name = args[0]
    contacts.pop(name)
    return "Contact removed."


@command_check_decorator(
        index_error_message="Error: Not enough arguments. Usage: phone [name]",
        key_error_message= "Error: Contact not found"
        )
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


def show_all(contacts):
    if len(contacts) == 0:
        return "No contacts found."

    contact_strings = [f"{name}: {phone}" for (name, phone) in contacts.items()]
    result = "\n".join(contact_strings)
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        cmd_string = input("Enter a command: ")
        cmd, args = parse_input(cmd_string)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args, contacts))
        elif cmd == "change":
            print(change_contact(args, contacts))
        elif cmd == "delete":
            print(delete_contact(args, contacts))
        elif cmd == "phone":
            print(show_phone(args, contacts))
        elif cmd == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

main()