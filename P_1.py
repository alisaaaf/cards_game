import time
import random

charecters = {}
charecters['Крыса'] = {"здоровье": 2, "сила": 1}
charecters['Добби'] = {"здоровье": 3, "сила": 4}

charecters['Человек'] = {"здоровье": 4, "сила": 5}
charecters['Маг-полукровка'] = {"здоровье": 5, "сила": 6}

charecters['Маг'] = {"здоровье": 7, "сила": 7}
charecters['Воландеморт'] = {"здоровье": 10, "сила": 8}

cards_me = ['Крыса','Маг-полукровка','Маг']
print('Ваши карты:')
for character in cards_me:
    character_info = characters[character]
    print(f"{character}: здоровье - {character_info['здоровье']}, сила - {character
card = input('Ваш ход, какую карту выберете?')
card_comp = random.choice(cards_me)
if card == 'Крыса':
    print('Ваша карта:', charecters['Крыса'])
    card = charecters['Крыса']
elif card == 'Маг-полукровка':
    print('Ваша карта:', charecters['Маг-полукровка'])
    card = charecters['Маг-полукровка']
elif card == 'Маг':
    print('Ваша карта:', charecters['Маг'])
    card = charecters['Маг']
    time.sleep(1)
    print('Карта противника:', card_comp)
while True:
        print('Вы атакуете!')
        time.sleep(2)
        if card['Сила'] >= card_comp['Здоровье']:
            print('Противник повержен!')
            break
        if card_me['Сила'] < card_comp['Здоровье']:
            print('Противник ранен ранены')
            card_comp['Здоровье'] = card_comp['Здоровье'] - card_me['Сила']
            print(card_comp)
            print('Ход противника!')
            time.sleep(2)
            if card_comp['Сила'] >= card_me['Здоровье']:
                print('Вы проиграли')
                break
            elif card_comp['Сила'] < card_me['Здоровье']:
                print('Вы ранены ранен')
                card_me['Здоровье'] = card_me['Здоровье'] - card_comp['Сила']
                print(card_me)
cards_comp = ['Добби','Человек','Воландеморт']