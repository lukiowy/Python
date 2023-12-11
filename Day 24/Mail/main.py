#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:/Python/Day 24/Mail/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("C:/Python/Day 24/Mail/Input/Names/invited_names.txt") as file:
    names = file.readlines()
        
for name in names:
    x = name.strip()
    final_letter = letter.replace("[name]", x)
    with open(f"C:/Python/Day 24/Mail/Output/ReadyToSend/letter_for_{x}.txt", "w") as file:
        file.write(final_letter)