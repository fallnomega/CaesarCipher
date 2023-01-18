from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caeser(message, shifting, direction_to_go):
    if int(shifting) > 26:
        shifting = int(shifting) % 26

    if direction_to_go == "encode":
        testing_original = ""
        encrypted = ""
        for x in message:
            testing_original += x
            if x not in alphabet:
                encrypted += x
            elif alphabet.index(x) + int(shifting) > 25:
                reverse_index_pos = ((alphabet.index(x) + int(shifting)) - 25)
                encrypted += alphabet[reverse_index_pos - 1]
                # alphabet.reverse()
                # print(alphabet)
            else:
                encrypted += alphabet[alphabet.index(x) + int(shifting)]
        print(f"The original text is {testing_original}")
        print(f"The encoded text is {encrypted}")
    elif direction_to_go == "decode":
        testing_original = ""
        decoded = ""
        # print (f"message: {message}")
        for x in message:
            testing_original += x
            if x not in alphabet:
                decoded += x
            elif alphabet.index(x) + int(shifting) < 25:
                reverse_index_pos = (alphabet.index(x) - int(shifting))
                decoded += alphabet[reverse_index_pos]
            else:
                decoded += alphabet[alphabet.index(x) - int(shifting)]
        print(f"The encoded text is {testing_original}")
        print(f"The decoded text is {decoded}")
    else:
        print(f"{direction_to_go} is invalid")




print (logo)
restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(message=text, shifting=shift, direction_to_go=direction)
    redo = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if redo == 'no':
        print("Goodbye!")
        restart = False

# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"
