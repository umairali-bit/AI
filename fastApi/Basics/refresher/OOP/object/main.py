from Enemy import *

enemy = Enemy()

enemy.type_of_enemy = 'Zombie'

# print(f'{enemy.type_of_enemy} has {enemy.health_points} '
     # f'health points and can do attack of {enemy.attack_damage}')

enemy.talk()
enemy.walk_forward()
enemy.attack()