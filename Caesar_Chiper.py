alpahabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  encrypted_text = ""
  for letter in text:
    if letter in alpahabet:
      letter_index = alpahabet.index(letter)
      new_index = letter_index + shift

      if new_index > 25:
        index2 = 25 - letter_index
        index3 = shift - index2
        encrypted_text += alpahabet[index3-1]

      else:
        encrypted_text += alpahabet[new_index]

    else:
      encrypted_text += letter

  print(encrypted_text)

def decrypt(text, shift):
  decrypted_text = ""
  for letter in text:
    if letter in alpahabet:
      letter_index = alpahabet.index(letter)
      new_index = letter_index - shift

      if new_index < 0:
        index2 = letter_index - shift
        index3 = shift - index2
        decrypted_text += alpahabet[index3-1]

      else:
        decrypted_text += alpahabet[new_index]

    else:
      decrypted_text += letter

  print(decrypted_text)

decrypt(text,shift)