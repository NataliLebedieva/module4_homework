def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file_cats:
            for line in file_cats:
                parts = line.strip().split(',')
                
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                else:
                    print(f"Неправильний формат рядка: {line}")
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    except IOError:
        print(f"Помилка читання файлу {path}.")

    return cats_info

cats_info = get_cats_info("cats_file.txt")
print(cats_info)