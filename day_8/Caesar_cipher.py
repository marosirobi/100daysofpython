from caesar import caesar



go_again = "yes"
while go_again == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    go_again = input("Do you want to continue? (yes/no)\n").lower()