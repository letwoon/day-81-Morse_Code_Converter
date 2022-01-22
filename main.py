morse_code_rules = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}

run = True
while run:
    #input the text that want to convert
    alphabet = input("Type in the words you want to convert to Morse Code: (a-z,0-9)\n").lower()

    #add characters into list and check if the characters is correct to convert
    success_convert = []
    error_convert = []
    for char in alphabet:
        if char in morse_code_rules:
            success_convert.append(morse_code_rules[char] + " ")
        else:
            if char in error_convert:
                continue
            else:
                error_convert.append(char)

    #feedback
    if len(error_convert) >= 1:
        print(f"'{error_convert}' could not be converted.\n"
              f"Please try again.")
    else:
        print(f"Your Morse Code are:\n{''.join(success_convert)}")

    # ask user if they want to convert again
    next = input("convert another text? (y/n): ")
    if next == "n":
        run = False