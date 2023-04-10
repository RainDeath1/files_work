"""
Задание №2

Написать программу транслитерации с русского на английский и наоборот.
Данные для транслитерации берутся из файла и записываются в другой файл.
Направление перевода определяется через меню пользователя.
"""

rus_to_eng = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '',
    'э': 'e', 'ю': 'yu', 'я': 'ya',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
    'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
    'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
}


eng_to_rus = {v: k for k, v in rus_to_eng.items()}


def transliterate(text, dictionary):
    result = []
    for char in text:
        result.append(dictionary.get(char, char))
    return ''.join(result)


def main():
    print("Выберите направление транслитерации:")
    print("1. Русский -> Английский")
    print("2. Английский -> Русский")
    choice = input("Введите номер опции: ")

    input_file = "input.txt"
    output_file = "output.txt"

    with open(input_file, "r", encoding="utf-8") as infile:
        text = infile.read()

    if choice == "1":
        translated_text = transliterate(text, rus_to_eng)
    elif choice == "2":
        translated_text = transliterate(text, eng_to_rus)
    else:
        print("Неверный выбор. Завершение программы.")
        return

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(translated_text)

    print(f"Транслитерация завершена. Результат сохранен в файле {output_file}")


content = 'Я видел как Коля выходил из двора, расположенного за домом, после чего он начал что-то топтать. \n' \
          'Я подшел к не му и спросил , что он делае, на что он толлько улыбулся ехидной улыбкой и \n' \
          'убежал, из-а чего я подумал что он бяка и задира, но не знал,что настоящим злюкой был его доносчик. '

with open("input.txt", "w", encoding='utf-8') as file:
    file.write(content)

if __name__ == "__main__":
    main()
