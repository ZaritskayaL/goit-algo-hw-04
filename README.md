<!-- CONTACT BOT PYTHON: -->

A simple command‑line contact manager written in Python.
It allows you to add, update, search, and list saved contacts using text commands.

<!-- FEATURES: -->

Add a contact: add [name] [phone]

Update an existing contact: change [name] [new_phone]

Show a phone number: phone [name]

Show all contacts: all

Exit the program: exit or bye

<!-- PROJECT STRUCTURE FOR HOME WORK+BOT (main.py) -->

goit_algo_hw_03/
│── _pycache_
│── bot.py
|── colorama.py
│── path_module.py
│── README.md
│── cats_file.txt
│── salary_file.txt
│── .venv/

bot.py  
Contains the full logic of the bot:

command parsing

functions for adding, changing, and showing contacts

main loop for user interaction


<!-- HOW TO RUN: -->
Terminal: python bot.py 

Enter a command: hello
How can I help you?
Enter a command: add <name> <number>
Contact added.

Enter a command: change <name> <number>
Phone for <name> <number> changed

Enter a command: phone <name>
<name>: <number>

Enter a command: all
<name>: <number>

Enter a command: bye
bye

<!-- NOTES: -->
Commands must follow the expected format; otherwise, the bot returns "Invalid command."

Names are treated as keys in the dictionary, so they must match exactly.

<!-- AUTHOR -->
Valeriia
Course project for GOIT(Python) 
