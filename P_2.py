import random
import time

print('*' * 10, 'Игра таинственного торговца', '*' * 10)

# Карточки игрока
dragon = {'Здоровье': 2, 'Сила': 3}
elf = {'Здоровье': 12, 'Сила': 23}
ork = {'Здоровье': 32, 'Сила': 43}
ork = {'Здоровье': 32, 'Сила': 43}
ork = {'Здоровье': 32, 'Сила': 43}
ork = {'Здоровье': 32, 'Сила': 43}
# Игра

cards = [dragon, elf, ork]
cards_comp = [dragon, elf, ork]

print('Ваши карты:')
print('Дракон', dragon)
print('Эльф', elf)
print('Орк', ork)
card = input('Ваш ход, какую карту выберете?')
card_comp = random.choice(cards_comp)
if card == 'Дракон':
    print('Ваша карта:', dragon)
    card = dragon
elif card == 'Эльф':
    print('Ваша карта:', elf)
    card = elf
elif card == 'Орк':
    print('Ваша карта:', ork)
    card = ork
time.sleep(1)
print('Карта противника:', card_comp)
while True:
    print('Вы атакуете!')
    time.sleep(2)
    if card['Сила'] >= card_comp['Здоровье']:
        print('Противник повержен!')
        break
    if card['Сила'] < card_comp['Здоровье']:
        print('Противник ранен ранены')
        card_comp['Здоровье'] = card_comp['Здоровье'] - card['Сила']
        print(card_comp)
        print('Ход противника!')
        time.sleep(2)
        if card_comp['Сила'] >= card['Здоровье']:
            print('Вы проиграли')
            break
        elif card_comp['Сила'] < card['Здоровье']:
            print('Вы ранены ранен')
            card['Здоровье'] = card['Здоровье'] - card_comp['Сила']
            print(card)
