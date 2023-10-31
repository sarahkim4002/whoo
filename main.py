def encode(password):
    new_pass = ''
    for number in password:
        number_new = str((int(number) + 3) % 10)
        new_pass += number_new
    return new_pass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")
        if option == "1":
            value = input("Please enter your password to encode: ")
            print("Encoded password is", encode(value))
        elif option == "2":
            value = input("Enter an already encoded 8-digit password: ")
            print("Decoded password is", decode(value))
        elif option == "3":
            break
        else:
            print("Invalid choice. Please try again.")
        print()

main()
