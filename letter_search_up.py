word = input("Введите слово >> ")
letter = input('Какую букву нужно найти? >>')
positions = []
total = 0

for index, i in enumerate(word.lower()):
    if i.lower() == letter.lower():
        total += 1
        positions.append(index)

print(f"Кол-во букв {letter} cостовляет {total}")
if total > 0:
    print(f"{letter} Находится на позиции {positions}")
else:
    print("Буква не найдена")    
