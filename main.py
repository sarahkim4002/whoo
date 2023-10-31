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
        option = input("\nPlease enter an option: ")
        if option == "1":
            value = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            print()
        elif option == "2":
            print("The encoded password is {password}, and the original password is {decode(password)}")
        elif option == "3":
            break
        else:
            print("Invalid choice. Please try again.")
        print()

main()
