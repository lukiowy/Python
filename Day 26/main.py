import pandas
#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("C:/Python/Day 26/nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Type your word: ").upper()
answer = [new_dict[letter] for letter in user]
print(answer)