

# Hi. I'm testing a new commit! 
message = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_length = len(alphabet)
offset = 14


def caesar_encode(message, offset):
    new_message = ' '
    for letter in message:
     
        if letter in alphabet:
            original_index = alphabet.find(letter)
            new_index = original_index - offset

            if new_index >= alphabet_length:
                new_index = new_index - alphabet_length
            elif new_index < 0:
                new_index = new_index + alphabet_length

            new_message += alphabet[new_index]
        else:
            new_message += letter

    return new_message
##############################################################
def caesar_decode(message, offset):
    new_message = ' '
    for letter in message:
     
        if letter in alphabet:
            original_index = alphabet.find(letter)
            new_index = original_index + offset

            if new_index >= alphabet_length:
                new_index = new_index - alphabet_length
            elif new_index < 0:
                new_index = new_index + alphabet_length

            new_message = new_message + alphabet[new_index]
        else:
            new_message = new_message + letter

    return new_message

#print(translated)

print('Do you want to encrypt or decrypt?')
user_input = input('e/d:   ').lower()
print()

if user_input == 'e':
    text = input('Enter the text to encode:   ')
    new_message = caesar_encode(text, offset)
    print(f'NEW_MESSAGE: {new_message}')

elif user_input == 'd':
    text = input('Enter the text to decode:   ')
    new_message = caesar_decode(text, offset)
    print(f'NEW_MESSAGE: {new_message}')