def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter in "aeiou":
                translation = translation + "g"
            else:
                translation = translation + "G"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))