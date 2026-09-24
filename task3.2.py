string = input("Give me an encrypted string: ")
number = int(input("Give me the key: "))

def decipher(string, number):
    result = ""

    for letter in string:
        if letter.isalpha():
            if letter.islower():
                result = result + chr((ord(letter) - ord('a') - number) % 26 + ord('a'))
            else:
                result = result + chr((ord(letter) - ord('A') - number) % 26 + ord('A'))
        else:
            result = result + letter

    return result

print("Your deciphered text is:")
print(decipher(string, number))
