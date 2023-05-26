import os

synonyms_file = open("synonyms.txt", "r")
synonyms_dict = {}

for line in synonyms_file:
    if " - " in line:
        words = line.strip().split(" - ")
        word = words[0]
        synonyms = words[1].split("; ")
        synonyms_dict[word] = synonyms

synonyms_file.close()

word = input("Введите слово: ")

if word in synonyms_dict:
    synonyms = synonyms_dict[word]
    if len(synonyms) > 1:
        for idx, synonym in enumerate(synonyms):
            print(f"{idx + 1}. \"{synonym}\"")
        answer = input("Вас устраивает эти варианты? Введите \"да\" или \"нет\": ")
        if answer.lower() == "нет":
            new_synonym = input("Введите свой вариант синонима: ")
            if word in synonyms_dict:
                synonyms_dict[word].append(new_synonym)
            else:
                synonyms_dict[word] = [new_synonym]

            # Записываем обновленные данные в файл
            with open("synonyms.txt", "w") as f:
                for w, syns in sorted(synonyms_dict.items(), key=lambda x: x[0]):
                    line = w.capitalize() + " - " + "; ".join([s.capitalize() for s in syns]) + "\n"
                    f.write(line)

    elif len(synonyms) == 1:
        synonym = synonyms[0]
        print(f"\"{synonym}\"")
        answer = input("Вас устраивает слово? \"да\" или \"нет\": ")
        if answer.lower() == "нет":
            new_synonym = input("Введите свой вариант синонима: ")
            if word in synonyms_dict:
                synonyms_dict[word].append(new_synonym)
            else:
                synonyms_dict[word] = [new_synonym]

            # Записываем обновленные данные в файл
            with open("synonyms.txt", "w") as f:
                for w, syns in sorted(synonyms_dict.items(), key=lambda x: x[0]):
                    line = w.capitalize() + " - " + "; ".join([s.capitalize() for s in syns]) + "\n"
                    f.write(line)

else:
    print(f"Слово \"{word}\" не найдено в словаре синонимов.")
    new_synonym = input("Введите свой вариант синонима: ")
    synonyms_dict[word] = [new_synonym]

    # Добавляем новую пару слово-синоним в файл
    with open("synonyms.txt", "a") as synonyms_file:
        line = word.capitalize() + " - " + new_synonym.capitalize() + "\n"
        synonyms_file.write(line)

    # Считываем данные из файла и перезаписываем их отсортированными по первым словам строк
    synonyms_file = open("synonyms.txt", "r")
    data = [line.capitalize() for line in synonyms_file.readlines()]
    synonyms_file.close()

    with open("synonyms.txt", "w") as synonyms_file:
        data.sort()
        for line in data:
            synonyms_file.write(line)

# Закрываем файл
synonyms_file.close()
