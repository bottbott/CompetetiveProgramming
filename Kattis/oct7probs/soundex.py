word = input()

values = {
    'BFPV': 1,
    'CGJKQSXZ': 2,
    'DT': 3,
    'L': 4,
    'MN': 5, 
    'R': 6
}

letters = list(values.keys())
letters = [item for sublist in letters for item in sublist]

# word_dict = dict.fromkeys(letters)

soundex = ''
i = 0
while i < len(word):
    if word[i] == word[i+1]:
        continue
    # can i do some sort of partial match from the letter in the word to the key? 
    soundex += values[any(key.find(word[i]) for key in values)]

print(soundex)
