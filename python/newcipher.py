
alphabet = 'abcdefghijklmnopqrstuvwxyz'

new_output = ''
user_input = input('Enter your message:').lower()
key = int(input('Enter your key:'))

for character in user_input:
    if character in alphabet:
        place = alphabet.find(character)
        new_place = (place + key)%26
        new_character = alphabet[new_place]
        new_output += new_character

    else:
        new_output += character

print('Your new message is: ' + new_output)

