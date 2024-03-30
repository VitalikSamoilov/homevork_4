from pathlib import Path
filename = Path("cats_raw.txt")

def get_cats_info(filename):
    cats_info = []
    try:
        with open (filename, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    cat_id, cat_name, cat_age = line.strip().split(",")
                    cats_info.append({"id": cat_id, "name": cat_name, "age": cat_age})
                except ValueError as e:
                    print(f"Невірний формат запису текстового файлу: {e}")
    except FileNotFoundError:
        print("Текстовий файл котів не знайдений")            
    except Exception as e:
        print(f"Виникла {e} помилка")    
    return cats_info
print(get_cats_info(filename))

         

