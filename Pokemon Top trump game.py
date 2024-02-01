

print('Welcome to Pokemon Top Trump. The rules are simple. The computer '
      'will generate a random pokemon for you and your opponent. From there '
      'the pokemon with the highest chosen stats will win!')



import random
import requests

# This program uses randit() to returns the stats from the URL(API).
def random_pokemon():
     pokemon_number = random.randint(1, 151)
     url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
     response = requests.get(url)
     pokemon = response.json()

     return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience']

    }

# I have used a new variable my_pokemon to obtain a random pokemon from the API.

my_pokemon = random_pokemon()


stat_choice = input('Which stat do you want to use? ( id, height, weight, base_experience)')


# I printed multiple returns to showcase the random pokemons stats of the player and the opponent.

print("You were given {}. ".format(my_pokemon['name']))
print('The pokemon given stats are listed below:')
print("id number {}. ".format(my_pokemon['id']))
print("{} cm. ".format(my_pokemon['height']))
print("{} kg. ".format(my_pokemon['weight']))
print("Base experience {}. ".format(my_pokemon['base_experience']))



opponent_pokemon = random_pokemon()
print("The opponent chose {}. ".format(opponent_pokemon['name']))
print("The opponent stats are listed below:")
print("id number {}. ".format(opponent_pokemon['id']))
print("{} cm. ".format(opponent_pokemon['height']))
print("{} kg. ".format(opponent_pokemon['weight']))
print("Base experience {}. ".format(opponent_pokemon['base_experience']))

print("")

#Now the program will compare the stats to see if the player win or loose

my_stat = my_pokemon[stat_choice]
opponent_stat = opponent_pokemon[stat_choice]
if my_stat > opponent_stat:
    print('You Win!')
elif my_stat < opponent_stat:
    print('You Lose!')
else:
    print('Draw!')



#ask the player if they want to play antoher round with import sys function.


import sys

another_round = input('Would you like to play another round? yes/no ')
if another_round.lower() == "no":
    sys.exit("Bye see you next time!")

#If the player shoose YES the next round will be the opponent turn to choose a stats.

stat = ['id', 'height', 'weight', 'base_experience']
stat_choice = random.choice(stat)
print('Your opponent chose {} as a stat.'.format(stat_choice))
ase_

def random_pokemon():
     pokemon_number = random.randint(1, 151)
     url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
     response = requests.get(url)
     pokemon = response.json()

     return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],

    }

opponent_pokemon = random_pokemon()

print('Your opponent was given {}'.format(opponent_pokemon['name']))
opponent_pokemon = random.randint(1,151)
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_pokemon)
response = requests.get(url)
opponent_pokemon = response.json()

print("The opponent stats are listed below:")
print("id number {}. ".format(opponent_pokemon['id']))
print("{} cm. ".format(opponent_pokemon['height']))
print("{} kg. ".format(opponent_pokemon['weight']))
print("Base experience {}. ".format(opponent_pokemon['base_experience']))


my_pokemon = random_pokemon()

print("You were given {}. ".format(my_pokemon['name']))
print('The pokemon given stats are listed below:')
print("id number {}. ".format(my_pokemon['id']))
print("{} cm. ".format(my_pokemon['height']))
print("{} kg. ".format(my_pokemon['weight']))
print("Base experience {}. ".format(my_pokemon['base_experience']))


my_stat = my_pokemon[stat_choice]
opponent_stat = opponent_pokemon[stat_choice]
if my_stat > opponent_stat:
    print('You Win!')
elif my_stat < opponent_stat:
    print('You Lose!')
else:
    print('Draw!')



