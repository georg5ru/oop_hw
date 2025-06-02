# ООП 1st hw


## Созданы 2 класса Category и Product 

## Product: класс продукта. Содержит название, описание, цену и количество 
### Product: name(str), description(str), price(float), quantity(int)



## Category: класс категории. Содержит название, описание, список товаров, количество категорий, количество товаров
### Category: name(str), description(str), products(list), all_category(int), all_product(int)

### Созданы новые классы Smartphone и LawnGrass

### Новые возможности
- Добавлен абстрактный базовый класс `BaseProduct`
- Реализован миксин `LogCreationMixin` для логирования создания объектов
- Все классы продуктов теперь наследуются от `BaseProduct`