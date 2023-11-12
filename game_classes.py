from dataclasses import dataclass


@dataclass
class Thing:
    """Создает объект инвентаря."""
    title: str
    defense_percentage: float
    attack: int
    health_point: int


@dataclass
class Person:
    """Создает базовый объект персонажа."""
    name: str
    health: int
    default_attack: int
    defense_percentage: float
    
    def set_things(self, things):
        """Принимает список вещей."""
        for thing in things:
            self._count_buff(**asdict(thing))
        pass

    def attack_damage(self):
        """Вычитает жизни на основе атаки."""
        pass


@dataclass
class Paladin(Person):
    """Создает персонажа типа: Plaldin"""
    def __init__(self, name: str, health: int, default_attack: int, default_defend: int):
        super().__init__(name, health, default_attack, default_defend)

    def __post_init__(self):
        self.health *= 2
        self.defense_percentage *= 2


@dataclass
class Warrior(Person):
    """Создает персонажа типа: Warrior"""
    def __init__(self, name: str, health: int, default_attack: int, default_defend: int):
        super().__init__(name, health, default_attack, default_defend)

    def __post_init__(self):
        self.default_attack *= 2
