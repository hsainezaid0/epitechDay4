#x = int(input("entrer un nbr : "))

#if x % 2 !=0:
#    print("This integer is odd")
#else:
#    print("This integer is even")


"""string = input("Entrer une phrase :")

if string == "open sesame":
    print("acces granted")
elif string == "will you open ":
    print("acces fucking granted")
else : 
    print("permission denied")"""


"""x = int(input("entrer un nbr : "))

if x == 42 : 
    print("a")
elif x <= 21 :
    print("b")
else :
    print("c")"""

"""a = 42
b = 41
if a == b :
    print("A and B is the sames")

if b <= a :
    print("B is equal or lower as A")

if b != a :
    print("B his different from A")"""

"""for i in range(1,1001,1) :
    print(i)"""



"""string = input("Entrer une phrase :")

for char in string :
    print(char * 2, end="") #empêche print() de revenir à la ligne à chaque fois."""


"""for i in range(10000,0,-1) :
    if(i % 7 == 0) : 
        print(i)"""

"""for i in range(-30, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)"""


"""number, text = input("Enter an integer and a string: ").split(maxsplit=1)
number = int(number)
vowels = ["a", "e", "i", "o", "u"]
found = False

if number == 0:
    quit()
for vowel in vowels:
    if vowel in text:
        found = True

if found:
    print(number)
elif number >= 42:
    print(number)
else:
    print(text)


number, text = input("Enter an integer and a string: ").split(maxsplit=1)
number = int(number)

if number == 0:
    quit()

if any(v in text.lower() for v in "aeiou") or number >= 42:
    print(number)
else:
    print(text)"""



"""text = input("Enter text: ")
shift = 3
result = ""

for letter in text:
    new_letter = chr((ord(letter) - ord('a') + shift) % 26 + ord('a')) #ord = ascii code % 26 bcs there is 26 alphabet and chr() opposite of ord()
    result += new_letter

print(result)"""




"""string = input("Give me a string: ")
number = int(input("Give me an integer: "))
 
def cipher(string, number):
    result = ""
 
    for letter in string:
        if letter.isalpha():
            if letter.islower():
                result = result + chr((ord(letter) - ord('a') + number) % 26 + ord('a'))
            else:
                result = result + chr((ord(letter) - ord('A') + number) % 26 + ord('A'))
        else:
            result = result + letter
 
    return result
 
 
print("Your deciphered text is the following:\n", cipher(string, number))"""


""""
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

print(result)"""



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
