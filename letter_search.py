word = input("Введите слово  ")
qi = input("какую букву найти? >>  ")
found = False

for i in word:
    if i == qi:
        found = True
        break
if found:
    print("буква есть")

else:
    print("нет")
