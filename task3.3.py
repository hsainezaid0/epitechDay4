text = input("Enter text: ").lower()
key = input("Enter key: ").lower()

result = ""
key_index = 0

for letter in text:

    shift = ord(key[key_index]) - ord('a')

    new_letter = chr(
        (ord(letter) - ord('a') + shift) % 26 + ord('a')
    )

    result += new_letter

    key_index += 1

    if key_index == len(key):
        key_index = 0

print(result)
