def calculate_total_cost(file_path):
    total = 0

    try:
        with open(file_path, 'r', encoding='windows-1251') as file:
            lines = file.readlines()

            for line in lines:
                separation = line.split('--')

                if len(separation) == 2:
                    product_name = separation[0].strip()
                    product_cost = float(separation[1].strip())  

                    total += product_cost

    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайден")
    except Exception as e:
        print(f"Виникла помилка: {e}")

    return total

file_path = r'D:\lab4\lab.txt'

total = calculate_total_cost(file_path)
print("Загальна вартість товарів:", int(total))