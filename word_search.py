def clean_and_split(text):
    """Приводит текст к нижнему регистру и разбивает на очищенные слова."""
    if not text:
        return []
    text_lower = text.lower()
    words = text_lower.split()
    return [word.strip(".,!?;:-()\"'") for word in words]

# Улучшенные функции:
def count_words(text, target_word):
    words = clean_and_split(text)
    target = target_word.lower().strip(".,!?;:-()\"'")
    return words.count(target)  # Встроенный метод count упрощает подсчёт

def position_word(text, target_word):
    words = clean_and_split(text)
    target = target_word.lower().strip(".,!?;:-()\"'")
    return words.index(target) if target in words else -1



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
