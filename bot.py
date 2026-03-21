from dis import show_code


def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return '', []
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args, contacts):
    if len(args) !=2:
        return 'Invalid command format. Use: add [name] [phone]'
    name, phone = args 
    contacts[name] = phone
    return 'Contact added'


def change_contact(args, contacts):
    if len(args) != 2:
        return 'Invalid command format. Use: add [name] [phone]'
    name, new_phone = args
    if name not in contacts:
        return 'Contact not found.'
    if name not in contacts:
        return 'Contact not found'
    old_phone = contacts[name]
    contacts[name] = new_phone
    return f'Phone for {name} changed'

    
def show_phone(args, contacts):
    name = args[0] if args else None
    if not name:
        return 'Enter name'
    if name in contacts:
        return f'{contacts}'
    else:
        return 'Contact not fouund'
    
    
def show_all(contacts):
    if not contacts:
        return 'No contacts saved.'
    result = []
    for name, phone in contacts.items():
        result.append(f'{name} {phone}')
    return '\n'.join(result)


def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    
    while True:
        user_input = input('Enter a command: ').strip().lower()
        command, args = parse_input(user_input)
        
        if command in ['close', 'exit', 'bye']:
            print('bye')
            break
        
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            if len(args) != 1:
                print("Please provide exactly name.")
            else:
                print(show_phone(args[0], contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command.')
            
if __name__ == '__main__':
    main()
    

