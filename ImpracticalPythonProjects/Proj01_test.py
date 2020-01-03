""" Testing a while True loop, particularly for closing it. """

print("cheese")
while True:
    some_text = input("Write something.  > ")
    print("You wrote " + some_text)
    try_again = input("\nTry again? (Press Enter else n to quit this loop.)\n")
    if try_again.lower() == "n":
        break
input("\nPress Enter to exit.") # <= Enter won't give any input, so the file closes.