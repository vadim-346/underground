from random import *
from time import sleep
import random as rnd
VERSION = 0.5
PUPLE = 95
YELLOW = 93
GREEN = 92
BLUE = 94

class Unit():

    def __init__(self, name='', health=100, damage=10):
        self.health = health
        self.damage = damage
        self.name = name 
    
    def kick(self):
        return rnd.randrange(0, self.damage)
    
    def wound(self, damage):
        self.health = self.health - damage
        return self.health <= 0
        



class Gun():
    def __init__(self, damage=30):
        self.damage = damage
    
    def shot(self):
        return rnd.randrange(self.damage // 3, self.damage)

def help():
    print('move - w')
    print('backpack - i')
    print('shot - e')


def monster_spawn():\

    monster = None
    monster_tipe = randint(1, 4)
    if monster_tipe == 1:
        monster = Unit('bugmole', 20, 30)
    elif monster_tipe == 2:
        monster = Unit('bigbag', 50, 10)
    elif monster_tipe == 3:
        monster = Unit('molemut', 80, 15)
    else:
        monster = Unit('chicken', 10, 1)
    return monster
    

def color_text(text, color):
    
    print(f'\033[{color}m{text}\033[0m')


if __name__ == '__main__':

    i_am = Unit('Vadim', 100)
    gun = Gun(20)

    print('hello')
    print(f'underground {VERSION}')
    print('Before I begin, I tell you a story.')
    print('')

    with open('history.txt', 'r') as file:
        text = file.read()
        color_text(text, YELLOW)
    health = 100
    ammo = 30
    distance = 0
    win_distance = 20
    while True:
        sleep(1)
        action = input('>> ')
        
        if action == 'i':
            print('|| = ', ammo, '   + =', i_am.health)
        elif action == 'w':
            distance = distance + 1
            monster_chance = randint(0, 1)
            if monster_chance:
                monster = monster_spawn()
                print(f'you met a creature {monster.name}')
                
                # Fight with a monster
                while True:
                    action = input()
                    if action == 'e' and ammo > 0:
                        print('pow!')
                        ammo = ammo - 1
                        monster_is_dead = monster.wound(gun.shot())
                        if monster_is_dead:
                            color_text('You win!', GREEN)
                            break

                        i_am_dead = i_am.wound(monster.kick())
                        if i_am_dead:
                            color_text('You die!', PUPLE)
                            exit(0)
                            break
                    if action == 'i':
                        print('|| = ', ammo, '   + =', i_am.health)

                    
        
        else:
            help()
        