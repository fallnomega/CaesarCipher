# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
def encrypt(message, shifting):
    testing_original = ""
    encrypted = ""
    for x in message:
        testing_original+=x
        temp_position =  (alphabet.index(x))
        encrypted+=alphabet[temp_position + int(shifting)]

    print (f"The original text is {testing_original}")
    print (f"The encoded text is {encrypted}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
text = "hello".lower()
# shift = int(input("Type the shift number:\n"))
shift = "5"
encrypt(text,shift)


    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

