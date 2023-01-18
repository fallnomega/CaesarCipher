from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(message,shifting,direction_to_go):
    if direction_to_go == "encode":
        testing_original = ""
        encrypted = ""
        for x in message:
            testing_original += x
            if x not in alphabet:
                encrypted+=x
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
            if alphabet.index(x) + int(shifting) < 25:
                reverse_index_pos = (alphabet.index(x) - int(shifting))

                # print(f"26 - temp position {alphabet.index(x)} - {shifting} shifting = {reverse_index_pos} reverse_index_pos")

                # print(reverse_index_pos)
                decoded += alphabet[reverse_index_pos]
            else:
                decoded += alphabet.index(x) - int(shifting)
        print(f"The encoded text is {testing_original}")
        print(f"The decoded text is {decoded}")
    else:
        print(f"{direction_to_go} is invalid")


#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).

# TODO-3: What happens if the user enters a number/symbol/space?
#  Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.


# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
direction="encode"
# text = input("Type your message:\n").lower()
# text = "ezqz".lower()
text = "hello zulu".lower()
# shift = int(input("Type the shift number:\n"))
shift = "5"


# print (logo)

caeser(message=text,shifting=shift,direction_to_go=direction)

  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"





