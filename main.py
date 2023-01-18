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
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.



