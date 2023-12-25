# Общий класс
class Flower:
    def __init__(self, color, stem_length, freshness, cost, lifespan):
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.cost = cost
        self.lifespan = lifespan

    def __str__(self):
        return f"{self.color} цветок, {self.stem_length} см, свежесть {self.freshness}/10"

    def __repr__(self):
        return f"Flower('{self.color}', {self.stem_length}, {self.freshness}, {self.cost}, {self.lifespan})"


# Классы нескольких видов
class Rose(Flower):
    pass


class Tulip(Flower):
    pass


class Lily(Flower):
    pass


# экземпляры (объекты) цветов разных видов.
rose = Rose("красный", 40, 8, 100, 7)
tulip = Tulip("желтый", 30, 9, 60, 5)
lily = Lily("белый", 50, 7, 120, 10)


# Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть хранятся в списке.
# Это будет список объектов.

# Класс букет
class Bouquet:
    def __init__(self):
        self.flowers = []  # список для хранения цветов

    # считаем стоимость букета
    def calculate_cost(self):
        return sum(flower.cost for flower in self.flowers)

    # Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
    def average_lifespan(self):
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return total_lifespan / len(self.flowers) if self.flowers else 0

    # Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
    # (это тоже методы)
    def sort_flowers(self, attribute):
        supported_attributes = ['color', 'stem_length', 'freshness', 'cost', 'lifespan']
        if attribute in supported_attributes:
            self.flowers.sort(key=lambda flower: getattr(flower, attribute))

    # Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни)
    # (и это тоже метод).
    def find_flowers(self, lifespan=None):
        return [flower for flower in self.flowers if
                flower.lifespan == lifespan] if lifespan is not None else []

    # добавление цветка в букет
    def add_flower(self, flower):
        self.flowers.append(flower)

    def __str__(self):
        return f"Букет содержит: {[str(flower) for flower in self.flowers]}"


# Ничего не сказано про вывод, поэтому чисто для себя:)
my_bouquet = Bouquet()
my_bouquet.add_flower(rose)
my_bouquet.add_flower(tulip)
my_bouquet.add_flower(lily)

print(my_bouquet)
