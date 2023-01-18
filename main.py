def encrypt(message, shifting):
    testing_original = ""
    encrypted = ""
    for x in message:
        testing_original += x
        temp_position = (alphabet.index(x))
        if temp_position + int(shifting) > 25:
            reverse_index_pos = ((temp_position + int(shifting)) - 25)
            encrypted += alphabet[reverse_index_pos - 1]
            # alphabet.reverse()
            # print(alphabet)
        else:
            encrypted+=alphabet[temp_position + int(shifting)]
    print (f"The original text is {testing_original}")
    print (f"The encoded text is {encrypted}")

def decrypt(message, shifting):
    testing_original = ""
    decoded = ""
    # print (f"message: {message}")
    for x in message:
        testing_original+=x
        temp_position =  (alphabet.index(x))
        if temp_position + int(shifting) < 25:
            reverse_index_pos = (temp_position - int(shifting))
            # print(f"26 - temp position {temp_position} - {shifting} shifting = {reverse_index_pos} reverse_index_pos")

            # print(reverse_index_pos)
            decoded += alphabet[reverse_index_pos]
        else:
            decoded+=alphabet[temp_position - int(shifting)]
    print (f"The encoded text is {testing_original}")
    print (f"The decoded text is {decoded}")
    return


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
direction="decode"
# text = input("Type your message:\n").lower()
# text = "ezqz".lower()
text = "ezqz".lower()
# shift = int(input("Type the shift number:\n"))
shift = "5"
if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt (text,shift)
else:
    print(f"{direction} is invalid")

  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"





