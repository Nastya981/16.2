from src.product_classes import Product, Category


def main() -> None:
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССОВ Product И Category")
    print("=" * 50)

    product1 = Product("Смартфон", "Мощный смартфон", 50000.0, 15)
    product2 = Product("Ноутбук", "Игровой ноутбук", 89999.99, 8)
    product3 = Product("Наушники", "Беспроводные наушники", 5000.0, 30)

    print("\n📦 Товары:")
    print(f"  - {product1.name}: {product1.price} руб. (в наличии: {product1.quantity} шт.)")
    print(f"  - {product2.name}: {product2.price} руб. (в наличии: {product2.quantity} шт.)")
    print(f"  - {product3.name}: {product3.price} руб. (в наличии: {product3.quantity} шт.)")

    electronics = Category("Электроника", "Электронные товары", [product1, product2])
    audio = Category("Аудио", "Аудио-товары", [product3])

    print("\n📂 Категории:")
    print(f"  - {electronics.name}: товаров: {len(electronics.products)}")
    print(f"  - {audio.name}: товаров: {len(audio.products)}")

    print("\n📊 Статистика:")
    print(f"  - Всего категорий: {Category.category_count}")
    print(f"  - Всего товаров: {Category.product_count}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
