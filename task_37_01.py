"""
Задание №1

Дан текстовый файл.
Необходимо создать новый файл убрав из него все неприемлемые слова.
Список неприемлемых слов находится в другом файле.
"""


bad_words = ["бяка", "задира", "доносчик", "злюка", "злюкой"]

with open("bad_words.txt", "w", encoding="utf-8") as file:
    for word in bad_words:
        file.write(f"{word}\n")

content = 'Я видел как Коля выходил из двора, расположенного за домом, после чего он начал что-то топтать. \n' \
          'Я подшел к не му и спросил , что он делае, на что он толлько улыбулся ехидной улыбкой и \n' \
          'убежал, из-а чего я подумал что он бяка и задира, но не знал,что настоящим злюкой был его доносчик. '

with open("source.txt", "w", encoding='utf-8') as file:
    file.write(content)

with open('source.txt', 'r', encoding='utf-8') as source_file, open('cleaned.txt', 'w', encoding='utf-8') as f:
    for line in source_file:
        words = line.split()
        cleaned_words = []

        for word in words:
            if word.lower().strip('.,') not in bad_words:
                cleaned_words.append(word)

        cleaned_line = ' '.join(cleaned_words)
        f.write(cleaned_line + '\n')

