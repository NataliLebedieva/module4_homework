def total_salary(path):
    total_sum_salary = 0
    count_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file_salary:
            for line in file_salary:
                parts = line.strip().split(',')
                
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        total_sum_salary += salary
                        count_developers += 1
                        print(f'developer {parts[0]}, salary {parts[1]}')
                    except ValueError:
                        print(f"Неправильний формат зарплати у рядку: {line}")
                else:
                    print(f"Неправильний формат рядка: {line}")
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return (0, 0)
    except IOError:
        print(f"Помилка читання файлу {path}.")
        return (0, 0)

    if count_developers == 0:
        return (0, 0)
    
    average_salary = total_sum_salary / count_developers
    return (total_sum_salary, average_salary)


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
