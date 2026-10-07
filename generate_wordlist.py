from itertools import product

name = input("Full name: ").strip()
dob = input("DOB (DDMMYYYY): ").strip()
nickname = input("Nickname: ").strip()

# User se additional digits/special characters
extra_digits = input("Extra digits (e.g. 123, 007): ").strip()
special_chars = input("Special characters (e.g. @#_!): ").strip()

parts = [
    name,
    name.lower(),
    name.upper(),
    nickname,
    nickname.lower(),
    nickname.upper(),
    dob,
    dob[-4:],       # year
    dob[:2],        # day
    dob[2:4],       # month
    extra_digits,
    special_chars
]

# Empty aur duplicate values remove
parts = list(dict.fromkeys(x for x in parts if x))

count = 0

with open("wordlist.txt", "w", encoding="utf-8") as f:
    for length in range(1, 3):
        for combo in product(parts, repeat=length):
            word = "".join(combo)

            if len(word) <= 20:
                f.write(word + "\n")
                count += 1

print(f"\nGenerated {count} entries.")
print("Wordlist saved as: wordlist.txt")