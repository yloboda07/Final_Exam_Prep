def is_anagram(text_1, text_2):
    text_1 = text_1.lower()
    text_2 = text_2.lower()
    first = list(text_1)
    second = list(text_2)

    first_alpha = []
    second_alpha = []

    for char in first:
        if char.isalpha():
            first_alpha.append(char)

    for char in second:
        if char.isalpha():
            second_alpha.append(char)

    first_alpha.sort()
    second_alpha.sort()

    return first_alpha == second_alpha

print(is_anagram("O, Draconian devil!", "Leonardo da Vinci"))
print(is_anagram("Oh, lame saint!", "The Mona Lisa"))
print(is_anagram("ALGORITHMICALLY", "logarithmically"))
print(is_anagram("Doctor Who", "Torchwood"))