alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text,shift_amount,encode_or_decode):
    shifted_text = ""
    shifted_pos = 0

    for char in original_text:
        if char != ' ' and char in alphabet:
            if encode_or_decode == "encode":
                shifted_pos = int(alphabet.index(char) + shift_amount)
            else:
                shifted_pos = int(alphabet.index(char) - shift_amount)

        if char in alphabet and shifted_pos < len(alphabet):
            shifted_text += str(alphabet[shifted_pos])

        elif char in alphabet and shifted_pos > len(alphabet)-1:
            shifted_text += str(alphabet[shifted_pos % len(alphabet)])
        else:
            shifted_text += char

    print(f"here's the {encode_or_decode}d result: {shifted_text}")