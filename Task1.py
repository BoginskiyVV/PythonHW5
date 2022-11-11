# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит 201 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) * Подумайте как наделить бота ""интеллектом""

# from random import randint


# def move_player(name_player, candies, max_move):
#     valid = False
#     while not valid:
#         move = input(f'{name_player}, Ваш ход... ')
#         try:
#             move = int(move)
#             if move > 0 and move <= max_move and move <= candies:
#                 print(f'Вы забрали {move} конфет')
#                 candies -= move
#                 print(f'Осталось {candies} конфет')
#                 valid = True
#             else:
#                 print(f'Количество взятых конфет должно быть в интервале от 1 до {max_move} или не больше оставшегося количества конфет')
#         except:
#             print('Необходимо ввести целое число.')
#     return candies

# def move_stupid_bot(candies, max_move):
#     move = randint(1, max_move) if candies >= max_move else randint(1, candies)
#     print(f'Бот забрал {move} конфет')
#     candies -= move
#     print(f'Осталось {candies} конфет')
#     return candies

# def move_smart_bot(candies, max_move):
#     move = candies % (max_move + 1)
#     if move == 0:
#         move = randint(1, max_move) if candies >= max_move else candies
#     print(f'Бот забрал {move} конфет')
#     candies -= move
#     print(f'Осталось {candies} конфет')
#     return candies

# def check_win(candies, determing_moves, first_name, second_name):
#     if candies == 0:
#         return first_name if determing_moves % 2 == 0 else second_name
#     else:
#         return False

# type_game = input('Введите 1, если хотите играть с другим игроком, и любую другую цифру, если с ботом... ')
# if (type_game == '1'):
#     Process_game.player_vs_player()
# else:
#     intel = input('Введите 0, если хотите играть с глупым ботом, и любую другую цифру, если с умным... ')
#     if intel == '0':
#         Process_game.player_vs_stupid_bot ()
#     else:
#         Process_game.player_vs_smart_bot ()

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}.\
    Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")