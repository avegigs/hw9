def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input format."
        except IndexError:
            return "Invalid command."
    return wrapper


def hello_command():
    return "How can I help you?"


@input_error
def add_command(user_input, contacts):
    _, contact_name, phone_number = user_input.split()
    contacts[contact_name] = phone_number
    return "Contact added successfully."


@input_error
def change_command(user_input, contacts):
    _, contact_name, phone_number = user_input.split()
    contacts[contact_name] = phone_number
    return "Phone number updated successfully."


@input_error
def phone_command(user_input, contacts):
    _, contact_name = user_input.split()
    return contacts[contact_name]


def show_all_command(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{contact}: {phone}" for contact, phone in contacts.items())


def main():
    contacts = {}
    while True:
        user_input = input("Enter a command: ").lower()
        if user_input == "hello":
            print(hello_command())
        elif user_input.startswith("add"):
            print(add_command(user_input, contacts))
        elif user_input.startswith("change"):
            print(change_command(user_input, contacts))
        elif user_input.startswith("phone"):
            print(phone_command(user_input, contacts))
        elif user_input == "show all":
            print(show_all_command(contacts))
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
