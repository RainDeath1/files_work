"""
Задание №4

Пользователь с клавиатуры вводит названия файлов,
до тех пор, пока он не введет слово quit.
После завершения ввода программа должна
записать в итоговый файл символы,
которые есть во всех перечисленных файлах
(символы должны быть в каждом файле).
"""


def main():
    filenames = []

    while True:
        user_input = input("Введите название файла или 'quit' для завершения: ")
        if user_input.lower() == "quit":
            break
        else:
            filenames.append(user_input)

    if not filenames:
        print("Не было введено ни одного файла.")
        return

    common_chars = None

    for filename in filenames:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                file_chars = set(content)

                if common_chars is None:
                    common_chars = file_chars
                else:
                    common_chars.intersection_update(file_chars)
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Пропускаем...")

    if common_chars:
        output_filename = "common_chars.txt"
        with open(output_filename, "w", encoding="utf-8") as out_file:
            for char in common_chars:
                out_file.write(char)

        print(f"Общие символы записаны в файл {output_filename}.")
    else:
        print("Общих символов не найдено.")


concordance = 'Я видел как Коля выходил из двора, расположенного за домом, после чего он начал что-то топтать. \n' \
          'Я подшел к не му и спросил , что он делае, на что он толлько улыбулся ехидной улыбкой и \n' \
          'убежал, из-а чего я подумал что он бяка и задира, но не знал,что настоящим злюкой был его доносчик. '

with open("content.txt", "w", encoding='utf-8') as document:
    document.write(concordance)

content_1 = 'Hi, world '

with open("cont.txt", "w", encoding='utf-8') as f:
    f.write(content_1)

poem = """Жлоб даёт советы снобу,
            Как набить свою утробу,
            Как украсть зимой метель.
            Крокодиловая куртка.
            Крокодиловый портфель."""

with open("poem.txt", "w", encoding='utf-8') as new_file:
    new_file.write(poem)

eng_poem = """Sun of the sleepless! Melancholy star!
              Whose tearful beam glows tremulously far,
              That show’st the darkness thou canst not dispel,
              How like art thou to joy remember’d well!
              """
with open("eng_poem.txt", "w", encoding="utf-8") as new_f:
    new_f.write(eng_poem)

if __name__ == "__main__":
    main()
