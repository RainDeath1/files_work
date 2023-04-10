"""
Задание №3

Пользователь с клавиатуры вводит названия файлов,
до тех пор, пока он не введет слово quit.
После завершения ввода программа должна
объединить содержимое всех перечисленных пользователем файлов в один.
"""


def main():
    filenames = []
    output_filename = "merged.txt"
    default_extension = ".txt"

    while True:
        user_input = input("Введите название файла или 'quit' для завершения: ")
        if user_input.lower() == "quit":
            break
        else:
            if not user_input.endswith(default_extension):
                user_input += default_extension
            filenames.append(user_input)

    with open(output_filename, "w") as outfile:
        for filename in filenames:
            try:
                with open(filename, "r") as infile:
                    for line in infile:
                        outfile.write(line)
            except FileNotFoundError:
                print(f"Файл {filename} не найден. Пропускаем...")

    print(f"Содержимое файлов объединено в файле {output_filename}.")


if __name__ == "__main__":
    main()
