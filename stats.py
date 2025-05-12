def get_num_words(file):
    words = file.split()
    return len(words)

def get_char_count(file):
    characterDict = {}
    lower_file = file.lower()
    for character in lower_file:
        if character in characterDict:
            characterDict[character] += 1
        else:
            characterDict[character] = 1

    return characterDict

def create_sorted_list(characterDict):
    result = []
    for char in characterDict:
        char_dict = {"char": char, "num": characterDict[char]}
        result.append(char_dict)
    result.sort(reverse=True, key=lambda dict:dict["num"])
    return result