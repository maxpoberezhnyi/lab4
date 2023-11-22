class Smartphone:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def years_since_release(self, current_year):
        return current_year - self.release_year


class Store:
    def __init__(self):
        self.smartphones = []

    def add_smartphone(self, smartphone):
        self.smartphones.append(smartphone)

    def remove_smartphones_before_year(self, year):
        self.smartphones = [smartphone for smartphone in self.smartphones if smartphone.release_year >= year]

    def display_smartphones(self):
        print("Наявні смартфони:")
        for smartphone in self.smartphones:
            print(f"{smartphone.name} ({smartphone.release_year}), {smartphone.years_since_release(2023)} роки з моменту виходу")

if __name__ == "__main__":
    iphone = Smartphone("iPhone 12", 2020)
    samsung = Smartphone("Samsung Galaxy S21", 2021)
    xiaomi = Smartphone("Xiaomi Mi 11", 2021)

    phone_store = Store()

    phone_store.add_smartphone(iphone)
    phone_store.add_smartphone(samsung)
    phone_store.add_smartphone(xiaomi)

    phone_store.display_smartphones()

    while True:
        try:
            year_to_filter = int(input("Введіть рік: "))
            break  
        except ValueError:
            print("Некоректний ввід. Будь ласка, введіть ціле число.")

    phone_store.remove_smartphones_before_year(year_to_filter)

    phone_store.display_smartphones()