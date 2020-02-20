# Наследование и полиморфизм
# Определить иерархию и/или композицию классов/объектов (в соответствии с вариантом). Реализовать классы.
# Написать демонстрационную программу, в которой создаются объекты различных классов.
# Определение классов, их реализацию.
# Каждый класс должен иметь отражающее смысл название и информативный состав.
# Наследование должно применяться только тогда, когда это имеет смысл.

# Классы – Цветок, Стебель, Роза, Хризантема, Букет.
from abc import ABC, abstractmethod


class Bouquet:
    """Class for bouquet."""

    def __init__(self, name, *flowers):
        self.name = name
        self.flowers = []
        for flower in flowers:
            self.flowers.append(flower)

    @property
    def bouquet_info(self):
        return '{0}: {1}'.format(self.name, self.flowers)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Stem(ABC):
    """Class stem with height and color."""

    def __init__(self, height, color):
        self.height = height
        self.color = color


class Flower(ABC):
    """Base ABSTRACT class for flower."""

    def __init__(self, shape_of_petal, petal_color, height_stem, color_stem):
        self.stem = Stem(height_stem, color_stem)
        self.shape_of_petal = shape_of_petal
        self.petal_color = petal_color

    @abstractmethod
    def make_smell(self):
        pass


class Rose(Flower):
    """Rose class."""

    def __init__(self, shape_of_petal, petal_color, height_stem, color_stem, number_of_spikes):
        super().__init__(shape_of_petal, petal_color, height_stem, color_stem)
        self.number_of_spikes = number_of_spikes

    def make_smell(self) -> str:
        """Make rose smell."""
        return 'smell as rose'

    def __str__(self):
        return 'rose'

    def __repr__(self):
        return 'rose'


class Chrysanthemum(Flower):
    """Chrysanthemum class."""

    def make_smell(self) -> str:
        """Make chrysanthemum smell."""
        return 'smell as chrysanthemum.'

    def __str__(self):
        return 'chrysanthemum'

    def __repr__(self):
        return 'chrysanthemum'


r1 = Rose('round', 'red', 1, 'green', 10)
print(r1.make_smell())
ch1 = Chrysanthemum('ellipse', 'white', 0.75, 'green')
print(ch1.stem.height)
print(ch1.shape_of_petal)
print(ch1.make_smell())
bouquet1 = Bouquet('bouquet_iz_togo_chto_bilo', r1, ch1)
print(bouquet1.bouquet_info)