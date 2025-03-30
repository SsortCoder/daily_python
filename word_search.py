def count_words(text, target_word):
    
    text_lower = text.lower()
    
    words = text_lower.split()
    
    target_word_lower = target_word.lower()

    count = 0

    for word in words:

        word_clean = word.strip(".,!?;:-()\"'")
        
        if word_clean == target_word_lower:
            count += 1
    
    return count


def position_word(text, target_word):
    if not text or not target_word:
        return -1

    text_lower = text.lower()
    words = text_lower.split()
    target_word_lower = target_word.lower()

    for index, word in enumerate(words):
        word_clean = word.strip(".,!?;:-()\"'")
        if word_clean == target_word_lower:
            return index
    return -1        



text = input("Введите предложение: >> ")
target = input("Введите слово для поиска: >> ")

if not text or not target:
    print("Ошибка: пустой ввод!")
else:
    result = count_words(text, target)
    position = position_word(text, target)

    print(f"Слово '{target}' встречается {result} раз.")
    if position != -1:
        print(f"Первая позиция в тексте: {position}")
    else:
        print("Слово не найдено.")
