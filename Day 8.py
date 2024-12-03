alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter) + shift_amount
        position %= len(alphabet)
        cipher_text += alphabet[position]
    print(f"The encoded text is {cipher_text}")


#TODO: Inside the 'encrypt' function, shift each letter of the 'text'
# forwards in the alphabet by the shift amount and print the encrypted text.
encrypt(plain_text=text,shift_amount=shift)