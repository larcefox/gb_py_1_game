# coding: utf-8
""""Creator Andrey (LarceFox) Soubbotin"""

import random



def welcome():
    game_name = '''
     ______   ______     __  __     ______      ______     ______   ______
    /\__  _\ /\  ___\   /\_\_\_\   /\__  _\    /\  == \   /\  == \ /\  ___\\
    \/_/\ \/ \ \  __\   \/_/\_\/_  \/_/\ \/    \ \  __<   \ \  _-/ \ \ \__ \\
       \ \_\  \ \_____\   /\_\/\_\    \ \_\     \ \_\ \_\  \ \_\    \ \_____\\
        \/_/   \/_____/   \/_/\/_/     \/_/      \/_/ /_/   \/_/     \/_____/
    '''

    print("Добро пожаловать в игру", game_name)


def pleer_info():
    pleer = {'name': {'question': 'Как тебя зовут?\n', 'answer': None},
             'age': {'question': 'Сколько тебе лет?\n', 'answer': None},
             'sex': {'question': 'Какого ты пола? М/Ж\n', 'answer': None},
             'pet_name': {'question': 'Имя твоего питомца\n', 'answer': None},
             'gambler_bool': {'question': 'Любишь играть в игры? да/нет\n', 'answer': None},
             }

    for item in pleer:

        while True:

            temp = input(pleer[item]['question']).lower()

            if item == 'age':
                if temp.isdigit():
                    temp = int(temp)
                else:
                    continue

            elif item == 'sex':
                # если в ответ пришло не м или ж сообщаем ошибку и запускаем цикл вопроса заново
                if not (temp == 'м' or temp == 'ж'):
                    print('Ваш пол надо вводить либо м либо ж')
                    continue

            elif item == 'gambler_bool':
                if not (temp == 'да' or temp == 'нет'):
                    print('В ответе нужно вводить либо да либо нет')

                    if temp == 'нет':
                        temp = False
                    elif temp == 'да':
                        temp = True

            elif temp == 'exit':
                quit()

            # сохраняем ответ в структуру словаря
            pleer[item]['answer'] = temp
            break

    return pleer


def pleer_check(pleer_info):

    if pleer_info['age']['answer'] < 18:
        print('Тебе нельзя играть')
        quit()

    elif pleer_info['age']['answer'] > 90:
        print("Для тебя это может быть утомительно!")

        for i in range(2):
            if input('Вы точно хотите играть? (да/нет)\n').lower() == 'да':
                pass
            else:
                print('До свидания, ', pleer_info['name']['answer'].title(), ' !')
                quit()

        print('Хорошо тогда начнем игру!')

    else:
        print('Добро пожаловать в Игру, ', pleer_info['name']['answer'].title(), '!')


def letters_name(pleer_info):
    print('Я могу назвать буквы алфавита, которых нет в твоем имени. и Произнести их.')

    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for char in letters:
        if char not in pleer_info['name']['answer'].lower():
            print(char)


def number_guess():

    while True:
        # Задание от 15.08.19г.
        print('Я задумал 16 чисел от 1 - 16 и расположил их в произвольном порядке:\n')

        numbers = (16, 1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8)
        masq = list('*' * len(numbers))  # Генерация звездочек по количеству элементов
        moves = 0

        for i, number in enumerate(numbers, start=1):

            output = ('|%s' * len(numbers) + '|') % tuple(masq)  # выводит маску |*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|
            print(output)

            while True:

                moves += 1

                index = input(f'Угадай на каком по счету месте цифра {i}\n')

                if not index.isdigit():  # проверка на численное, если да - приводит к int, и переводит в нумерацию с "0"

                    if index == 'menu':
                        return

                    elif index == 'exit':
                        exit()

                    print('\nМожно вводить только цифры!')
                    continue

                else:
                    index = int(index) - 1

                if (index) == numbers.index(i):
                    masq[index] = i
                    print('\nДа! Ты угадал!')
                    break

                else:
                    print(output)
                    print('\nНет! Попробуй еще раз!')
                    continue

        print('Поздравляю, ты выиграл! Сделано ходов:', moves)
        break


def rsp_game():

    log_file = open('python.txt', 'w+')

    def score_draw():
        print('{:*^15}'.format('комп'), '{:*^15}'.format('игрок'), file=log_file)
        print('*{: ^14}'.format(figures[rn_ch]), '{: ^14}*'.format(figures[temp]), file=log_file)
        print('*{: ^14}'.format('победил:'), '{: ^14}*'.format(winner), file=log_file)
        print('{:*^15}'.format(score[0]), '{:*^15}\n'.format(score[1]), file=log_file)

        print('{:*^15}'.format('комп'), '{:*^15}'.format('игрок'))
        print('*{: ^14}'.format(figures[rn_ch]), '{: ^14}*'.format(figures[temp]))
        print('*{: ^14}'.format('победил:'), '{: ^14}*'.format(winner))
        print('{:*^15}'.format(score[0]), '{:*^15}\n'.format(score[1]))

    score = (0,0)

    print("Игра \"Камень, ножницы, бумага\".")

    figures =  {"1": "камень",
                "2": "ножницы",
                "3": "бумага",}


    result = {

        "13": "комп",
        "21": "комп",
        "32": "комп",
        "11": "Дружба!",
        "22": "Дружба!",
        "33": "Дружба!",
        "12": "игрок",
        "23": "игрок",
        "31": "игрок",

    }

    winner = ""

    while True:

        for key, value in figures.items():
            print(f'{key}. {value}')

        temp = input(f'Выбери фигуру.\n')

        if temp == 'menu':
            log_file.close()
            return

        elif temp == 'exit':
            log_file.close()
            exit()

        if temp in (figures):
            rn_ch = random.choice(list(figures.keys()))

            if temp + rn_ch in list(result)[0:3]:
                score = (score[0] + 1, score[1])
                winner = result[temp + rn_ch]
                score_draw()

            elif temp + rn_ch in list(result)[3:6]:
                winner = result[temp + rn_ch]
                score_draw()

            elif temp + rn_ch in list(result)[6:9]:
                score = (score[0], score[1] + 1)
                winner = result[temp + rn_ch]
                score_draw()
        else:

            print("Выбери нолмер фигуры!\n")

        '''
        комп    игрок
        бумага    ножницы
    
        победил: игрок
        счет:
        комп    игрок
        2    5
        '''

def menu(pleer):

    menu_text = {
        "1": {'name': 'Буквы алфавита, которых нет в твоем имени', 'func': letters_name, 'param': pleer},
        "2": {'name': 'Угадай числа', 'func': number_guess},
        "3": {'name': 'Камень, ножницы, бумага', 'func': rsp_game},
        "4": {'name': 'Выйти из игры', 'func': quit, 'param': 0}
    }



    while True:
        print("\nМеню игры:")
        for key, value in menu_text.items():
            print(f'{key}. {value["name"]}')

        temp = input('Выберите номер игры \n')
        if temp in menu_text:

            if 'param' in menu_text[temp]:
                menu_text[temp]['func'](menu_text[temp]['param'])
            else:
                menu_text[temp]['func']()
        else:
            temp = input('Неправильный пункт меню. Выберите номер игры \n')


if __name__ == "__main__":


    while True:

        welcome()
        pleer = pleer_info()
        pleer_check(pleer)
        menu(pleer)
