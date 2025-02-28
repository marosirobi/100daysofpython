alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(original_text,shift_amount):
    shifted_text = ""
    shifted_pos = 0
    for char in original_text:
        if char != ' ':
            shifted_pos = int(alphabet.index(char) + shift_amount)

        if char in alphabet and shifted_pos < len(alphabet):
            shifted_text += str(alphabet[shifted_pos])

        elif char in alphabet and shifted_pos > len(alphabet)-1:
            shifted_text += str(alphabet[shifted_pos % len(alphabet)])
        else:
            shifted_text += " "

        print(f"here's the result: {shifted_text}")

def decrypt(original_text,shift_amount):
    shifted_text = ""
    shifted_pos = 0
    for char in original_text:
        if char != ' ':
            shifted_pos = int(alphabet.index(char) - shift_amount)

        if char in alphabet and shifted_pos < len(alphabet):
            shifted_text += str(alphabet[shifted_pos])

        elif char in alphabet and shifted_pos > len(alphabet) - 1:
            shifted_text += str(alphabet[shifted_pos % len(alphabet)])
        else:
            shifted_text += " "

        print(f"here's the result: {shifted_text}")