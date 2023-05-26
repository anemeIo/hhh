import os

# Открываем файл синонимов для чтения
synonyms_file = open("synonyms.txt", "r")

# Создаем словарь для хранения синонимов
synonyms_dict = {}

# Читаем файл построчно и заполняем словарь
for line in synonyms_file:
    if " - " in line:
        words = line.strip().split(" - ")
        word = words[0]
        synonyms = words[1].split("; ")
        synonyms_dict[word] = synonyms

# Закрываем файл синонимов
synonyms_file.close()

# Запрашиваем слово у пользователя
word = input("Введите слово: ")

# Если слово есть в словаре, выбираем случайный синоним
if word in synonyms_dict:
    synonyms = synonyms_dict[word]
    if len(synonyms) > 1:
        print(f"Слово \"{word}\" имеет несколько синонимов: {', '.join(synonyms)}.")
        answer = input("Вы хотите заменить это слово на один из них? Введите \"да\" или \"нет\": ")
        if answer.lower() == "да":
            for idx, synonym in enumerate(synonyms):
                print(f"{idx + 1}. \"{synonym}\"")
            answer = input("Введите номер синонима, который вы хотите использовать: ")
            try:
                synonym_idx = int(answer) - 1
                if synonym_idx >= 0 and synonym_idx < len(synonyms):
                    synonym = synonyms[synonym_idx]
                    with open("synonyms.txt", 'r') as file:
                        lines = file.readlines()
                    found_line = None
                    for i, line in enumerate(lines):
                        if word in line:
                            found_line = i
                            break
                    if found_line is not None:
                        z = synonym
                        v = word
                        lines[found_line] = lines[found_line].replace(word, synonym).capitalize()
                        words = lines[found_line].split()
                        index = -1
                        for i, syn in enumerate(words):
                            if syn == z and i != index:
                                del words[i]
                                break
                            elif syn == z:
                                index = i
                                break
                        if index >= 0:
                            words[index] = z
                        lines[found_line] = " ".join(words) + ';' + f" {v.lower()}\n"
                    with open("synonyms.txt", 'w') as file:
                        file.writelines(lines)
                    print(f"Заменяем слово \"{word}\" на его синоним \"{synonym}\".")
            except ValueError:
                print("Некорректный ввод.")
    elif len(synonyms) == 1:
        synonym = synonyms[0]
        print(f"Хотите заменить слово \"{word}\" на его синоним \"{synonym}\"?")
        answer = input("Введите \"да\" или \"нет\": ")
        if answer.lower() == "да":
            with open("synonyms.txt", 'r') as file:
                lines = file.readlines()
            found_line = None
            for i, line in enumerate(lines):
                if word in line:
                    found_line = i
                    break
            if found_line is not None:
                z = synonym
                v = word
                lines[found_line] = lines[found_line].replace(word, synonym).replace("-", "").replace(" ", "").capitalize()
                words = lines[found_line].split()
                index = -1
                for i, syn in enumerate(words):
                    if syn == z and i != index:
                        del words[i]
                        break
                    elif syn == z:
                        index = i
                        break
                if index >= 0:
                    words[index] = z
                lines[found_line] = " ".join(words) + ' - ' + f"{v.lower()}\n"
            with open("synonyms.txt", 'w') as file:
                file.writelines(lines)
            print(f"Заменяем слово \"{word}\" на его синоним \"{synonym}\".")
else:
    print(f"Слово \"{word}\" не найдено в словаре синонимов.")
    new_synonym = input("Введите свой вариант синонима: ")
    synonyms_dict[word] = [new_synonym]
    # Открываем файл синонимов для записи и перезаписываем его с обновленными данными
    with open("synonyms.txt", "a") as synonyms_file:
        line = word + " - " + new_synonym