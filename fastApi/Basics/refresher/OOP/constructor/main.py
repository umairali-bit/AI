from Enemy import *


enemy = Enemy('Zombie', 15, 3)

print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do attack of '
      f'{enemy.attack_damage}')