


class Enemy:
    #
    # type_of_enemy: str
    # health_points: int = 10
    # attack_damage: int = 1
    #
    # # empty constructor
    # def __init__(self):
    #     pass

    # # No argument constructor
    # def __init__(self):
    #     print("New enemy created with no starting values")

    # Parameter constructor
    def __init__(self, type_of_enemy, health_points = 10, attack_damage = 1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage



