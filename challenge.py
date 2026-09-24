number, text = input("Enter an integer and a string: ").split(maxsplit=1)
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
