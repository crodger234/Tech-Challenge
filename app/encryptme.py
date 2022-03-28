
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main(action, text, shift):
  action = action.lower()
  if action == "encode":
    shift_amount = shift
  elif action == "decode":
    shift_amount = shift * -1
  else:
    #raise Exception("Invalid action. Select either encode or decode.")
    print("Invalid action. Select either encode or decode.")
    main(action, text,shift)
  return caeser(direction_text=action, plain_text=text,shift_amount = shift_amount)

def caeser(direction_text, plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  return (f"Your text is {cipher_text}")
    