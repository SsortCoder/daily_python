import string

def find_letters(text, target_letter):
    text_clean = text.lower().translate(str.maketrans('', '', string.punctuation))
    positions = []
    
    for index, char in enumerate(text_clean):
        if char == target_letter.lower():
            positions.append(index)
    
    return len(positions), positions

text = input("Введите текст: ")
letter = input("Какую букву ищем? ")

count, positions = find_letters(text, letter)

if count > 1: 
    povtor = "раза"
else:
    povtor = "раз"    

print(f"Буква '{letter}' найдена {count} {povtor} на позициях: {positions}")
