USERS = {}


def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user"
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner


def hello_user():
    return "How can I help you?"


def unknown_command():
    return "unknown_command"


@error_handler
def add_user(name, phone):
    USERS[name] = phone
    return f'User {name} added!'


@error_handler
def change_phone(name, phone):
    old_phone = USERS[name]
    USERS[name] = phone
    return f'У {name} тепер телефон: {phone} Старий номер: {old_phone}'


def show_all():
    result = ''
    for name, phone in USERS.items():
        result += f'Name: {name} phone: {phone}\n'
    return result


@error_handler
def show_phone(name):
    phone = USERS[name]
    result = f'Phone: {phone} for user: {name}\n'
    return result


HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'change': change_phone,
    'show': show_all,
    'phone': show_phone,
}


def main():
    while True:
        command, *data = input('Please enter command: ').strip().split(' ', 1)
        
        if command in ["goodbye", "close", "exit"]:
            print("Good bye!")
            break
        
        if HANDLERS.get(command):
            handler = HANDLERS.get(command)
            if data:
                data = data[0].split(' ')
                
            result = handler(*data)

        else:
            result = unknown_command()

        print(result)


if __name__ == "__main__":
    main()
