text = input("Enter encrypted text: ").lower()
key_length = int(input("Enter key length: "))

english_freq = [
    8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0,
    6.1, 7.0, 0.15, 0.77, 4.0, 2.4,
    6.7, 7.5, 1.9, 0.095, 6.0, 6.3,
    9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074
]

letters = ""

for letter in text:
    if letter.isalpha():
        letters += letter


key = ""

for position in range(key_length):

    group = ""

    for i in range(position, len(letters), key_length):
        group += letters[i]

    best_shift = 0
    best_score = 999999

    for shift in range(26):

        counts = [0] * 26

        for letter in group:
            new_position = (ord(letter) - ord('a') - shift) % 26
            counts[new_position] += 1

        score = 0

        for i in range(26):
            expected = english_freq[i] * len(group) / 100

            if expected > 0:
                score += (counts[i] - expected) ** 2 / expected

        if score < best_score:
            best_score = score
            best_shift = shift

    key += chr(best_shift + ord('a'))


print("Key:", key)


result = ""
key_index = 0

for letter in text:

    if letter.isalpha():

        shift = ord(key[key_index % key_length]) - ord('a')

        new_letter = chr(
            (ord(letter) - ord('a') - shift) % 26 + ord('a')
        )

        result += new_letter
        key_index += 1

    else:
        result += letter


print("Decrypted text:")
print(result)
