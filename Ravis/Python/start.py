new_command = input("I don'tunderstand would you like for me to make that a new command? ")
user_input = input("What can I do for you? ")

greetings = open("text/greetings.txt", "r+")
greetings_stuff = greetings.read()

if user_input in greetings_stuff:
    print("Hello")
new_command