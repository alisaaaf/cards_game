import random
import time

print('*' * 10, 'Игра таинственного торговца', '*' * 10)

rat = {'Здоровье': 2, 'Сила': 1}
dobby = {'Здоровье': 3, 'Сила': 4}
human = {'Здоровье': 4, 'Сила': 5}
half_mag = {'Здоровье': 5, 'Сила': 6}
magician = {'Здоровье': 7, 'Сила': 7}
volandemort = {'Здоровье': 10, 'Сила': 8}

cards = [rat, human, magician]
print('Ваши карты:')
print('Крыса', rat)
print('Человек', human)
print('Маг', magician)

card = input('Ваш ход, какую карту выберете?')
card_comp = random.choice(cards)
if card == 'Крыса':
    print('Ваша карта:', rat)
    card = rat
elif card == 'Человек':
    print('Ваша карта:', human)
    card = human
elif card == 'Маг':
    print('Ваша карта:', magician)
    card = magician
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
