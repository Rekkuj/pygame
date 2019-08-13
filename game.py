# player_name = 'Rekku'
# player_attack = 10
# player_heal = 16
# health = 100

# List:
# player = ['Rekku', 10, 16, 100]

# you can change the values in list:
# player[1] = 11
# print(player['attack'])

game_running = True

while game_running == True:
    new_round = True
    # Dictionaries (key: value -pairs):
    player = {'name': 'Rekku', 'attack': 10, 'heal': 16, 'health': 100}
    monster = {'name': 'Max', 'attack': 12, 'health': 100}

    print('---'  * 5)
    print('Enter Player name')
    player['name'] = input()

    print('---'  * 5)
    # String concatenation can only concatenate string, not int, so we need to convert health into a string
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    while new_round == True:

        player_won = False
        monster_won = False

        print('---'  * 5)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit')

        player_choice = input()

        if player_choice == 1:
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                # pass (pass is kind of a placeholder to tell python, that it can continue executing and to the author that the code is missing
                player_won = True

            else:
                player['health'] = player['health'] - monster['attack']
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == 2:
            print('Healing player...')
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - monster['attack']
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == 3:
            new_round = False
            game_running = False
            print('Game Over')

        else:
            print('Invalid choice')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' left')

        elif player_won:
            print('Round Over. ' + player['name'] + ' won. Starting a new round..')
            new_round = False

        elif monster_won:
            print('Round Over. The Monster won. Starting a new round..')
            new_round = False

        if player_won == True or monster_won == True:
            new_round = False
            print('Round Over. Starting a new round..')