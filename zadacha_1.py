from pathlib import Path
filename = Path("zarplata.txt")

def total_salary(filename):
    try:
        total_salary = 0
        developer_count = 0
        with open (filename, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    name, salary = line.strip().split(",")
                    total_salary += float(salary)
                    developer_count += 1
                except ValueError as e:
                    print(f"Невірний формат запису зарплати {e}")
        average_salary = total_salary / developer_count
        return total_salary, average_salary
    except FileNotFoundError:
        print("Список зарплат не знайдено")
    except Exception as e:
        print(f"Виникла {e} помилка")      

total, average = total_salary(filename)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


                     