while True:
    word = input("Enter a character: ")
    if word.isdigit():
        print("You entered a digit.")
    else:
        print("You entered a letter.")