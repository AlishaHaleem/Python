alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))



# TODO:
def ceaser(plain_text,shift_amount , encode_or_decode):
    output_text = ""
    for letter in plain_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        position = alphabet.index(letter) + shift_amount
        position %= len(alphabet)
        output_text += alphabet[position]
    print(f"The decoded text is {output_text}")


should_continue = True

# directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
while should_continue:
    directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(plain_text=text, shift_amount=shift, encode_or_decode=directions)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")







#TODO: Inside the 'encrypt' function, shift each letter of the 'text'
# forwards in the alphabet by the shift amount and print the encrypted text.

