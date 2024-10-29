class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров и их цен

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в ассортимент магазина {self.name} с ценой {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён из ассортимента магазина {self.name}.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина {self.name}.")

    def get_price(self, item_name):
        """Возвращает цену товара по названию, если он есть в ассортименте."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара, если он есть в ассортименте."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' в магазине {self.name} обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина {self.name}.")

    def __str__(self):
        """Отображает информацию о магазине и его ассортименте."""
        items_list = "\n".join(f"{item}: {price}" for item, price in self.items.items())
        return f"Магазин '{self.name}', Адрес: {self.address}\nАссортимент:\n{items_list}"


# Создание объектов магазинов
store1 = Store("Fresh Market", "123 Main St")
store2 = Store("Grocery Land", "456 High St")
store3 = Store("Eco Shop", "789 Oak Ave")

# Добавление товаров
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("milk", 1.5)
store2.add_item("bread", 2.0)

store3.add_item("cheese", 3.5)
store3.add_item("yogurt", 1.2)

# Тестирование методов для магазина store1
print(store1)  # Вывод информации о магазине

# Обновление цены товара
store1.update_price("apples", 0.6)

# Получение цены товара
price = store1.get_price("bananas")
print(f"Цена на bananas в магазине {store1.name}: {price}")

# Удаление товара
store1.remove_item("apples")

# Вывод финальной информации о магазине после изменений
print(store1)

print(store2.__str__())