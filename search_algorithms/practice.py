def alpha_sort(lst):
    for i in range(len(lst)):
        sorted = True
        for k in range(len(lst)-i-1):
            if lst[k] > lst[k+1]:
                x = lst[k]
                lst[k] = lst[k+1]
                lst[k+1] = x
                sorted = False
        if sorted:
            break
    return lst

def alpha_search(lst,term):
    flag = False
    for i in lst:
        if i == term:
            flag = True
    return flag 

def subtract_string(str1,str2):
    return str1.replace(str2,'')
    
def best_match(lst,term):
    min = len(subtract_string(lst[0],term))
    index = 0
    for i in range(len(lst)):
        k = len(subtract_string(lst[i],term))
        if k < min:
            min = k
            index = i
    return lst[index]

def find_words_from_letters(letters):
    with open('algorithms/words.txt') as f:
        words = f.readlines()
    out = []
    for word in words:
        temp = word.lower()
        for letter in letters:
            temp = subtract_string(temp,letter)
        if temp == '\n':
            out.append(subtract_string(word,'\n').lower())
    return out
 
def best_scrabble_word(letters):
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    potential_words = find_words_from_letters(letters)
    max = 0
    index = 0
    for i in range(len(potential_words)):
        score = 0
        for c in potential_words[i]:
            score += scores[c]
        if len(potential_words[i]) <= 7 and score > max:
            max = score
            index = i
    return potential_words[index]

