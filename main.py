def encrypt(message, shifting):
    testing_original = ""
    encrypted = ""
    for x in message:
        testing_original+=x
        temp_position =  (alphabet.index(x))
        if temp_position + int(shifting) > 25:
            reverse_index_pos =  ((temp_position + int(shifting))-25)
            encrypted += alphabet[reverse_index_pos-1]
            # alphabet.reverse()
            # print(alphabet)


        else:
            encrypted+=alphabet[temp_position + int(shifting)]
    print (f"The original text is {testing_original}")
    print (f"The encoded text is {encrypted}")



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
text = "civilization".lower()
# shift = int(input("Type the shift number:\n"))
shift = "5"
encrypt(text,shift)




