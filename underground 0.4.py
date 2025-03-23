from random import randint
score = 0
buck = 30
health = 100
kills = 0
bandage = 2
food = 10
hunger = 100
a = True
def found_chest():
    
                        lucky = randint(1, 2)
                        print('You found the chest, youre going to open it?, y/n ')
                        choose4 = input()
                        if choose4 == 'y':
                            if lucky == 1:
                                print('Youre a lucky guy!')
                                buck = buck + 5
                                bandage = bandage + 1
                            if lucky == 2:
                                print('You shouldnt have inspired him')
                                buck = buck - 5
                        if choose4 == 'n':
                            score = score + 1
                            print('')
                            print('health-',health, 'buck-',buck, 'hunger-',hunger)
                            
def fight():
            
            
            
            
                miss = randint(1, 2)
                if miss == 1:
                    buck = buck - 1
                    kills = kills + 1
                    print('you killed him')
                    if chest == door_num:
                        found_chest
                if miss == 2:
                    buck = buck - 1
                    print('you missed! shoot away!')
                    choose2 = input()
                    if choose2 == 'shoot' and buck > 0:
                        buck = buck - 1
                        kills = kills + 1
                        print('you killed him')
                        print('')
                        if choose2 != 'shoot' and choose2 != 'run':
                            print('ERROR')
                            # TODO: fix error!
                score = score + 1
                print('')
                
                if choose == 'shoot' and buck < 0:
                
                   print('the buck is over')
                   print('health-',health, 'buck-',buck, 'hunger-',hunger)
                   choose3 = input('will you run?, y/n')
                   if choose3 != 'y' and 'n':
                     # TODO: fix error!
                    if choose3 == 'y':
                      if health > 10:
                        print('')    
                        score = score + 1
                        print('health-',health, 'buck-',buck, 'hunger-',hunger)
                    else:
                        print('monster kill you')
                        
                   if choose3 == 'n':
                    print('He smeared you to the wall')
                    pass     
def run():
          
          if choose == 'run':
                health = health - 10
                print('')
                score = score + 1
          if choose == 'run' and health < 0:
                a = False
def safe_movement():
            if door_num == chest:
                found_chest
            score = score + 1
            print('')
            print('health-',health, 'buck-',buck, 'hunger-',hunger)
print('underground 0.3')
print('The goal: to score as many points as possible by making your way through the dungeons')
print('actions: forward, heal, eat')
print('health-',health, 'buck-',buck, 'hunger-', hunger)
while a:
    if buck < 0:
        buck = 0
    if hunger > 100:
        hunger = 100
    action = input()
    if action =='i':
        print('food-', food, 'bandage-', bandage, 'buck-', buck)
        print('health-', health, 'hunger', hunger)

    hunger = hunger - 2
    if action == 'forward':    
        monster = randint(1, 2)
        chest = randint(1, 2)
        print('1, 2')
        door = input()
        door_num = int(door)
        if door_num == monster:
            miss = randint(1, 2)
            print('MONSTER!')
            print('shoot or run?')
            print('health-',health, 'buck-',buck, 'hunger-',hunger)
            choose = input()
            if choose == 'shoot' and buck > 0:
                  fight
            if choose == 'run':
                  run
        if monster != door:
            safe_movement
            
    if action == 'heal':
        bandage = bandage - 1
        health = health + 25
    if action == 'eat':
        food = food - 1
        hunger = hunger + 10
    
print('game over, score -', score,', kills -', kills)
            