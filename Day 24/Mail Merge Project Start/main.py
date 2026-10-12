#TODO: Create a letter using starting_letter.txt 
PLACEHOLDER = '[name]'
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letters = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letters.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_{stripped_name}.txt", 'w') as letter_file:
            letter_file.write(new_letter)

