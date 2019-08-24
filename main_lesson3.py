# coding: utf-8
""""Creator Andrey (LarceFox) Soubbotin"""


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
            if input('Вы точно хотите играть? (Да/Нет)\n') == 'Да':
                pass
            else:
                print('До свидания, ', pleer_info['name']['answer'], ' !')
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


def number_guess(pleer_info):
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

                    if index == 'exit':
                        quit()

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

def menu(**kwargs):

    while True:
        print('\n\nМеню игры\n')
        for game in kwargs:
            print(f'{kwargs[game]["num"]}. {kwargs[game]["name"]}')

        answer = input('Выбери номер игры:\n')

        if answer.isdigit():
            answer = int(answer)
        elif answer == 'exit':
            quit()
        else:
            print("Укажите цифру номера игры!")
            continue

        for game in kwargs:
            if answer == kwargs[game]["num"]:
                kwargs[game]['func'](kwargs[game]['param'])
                break
        else:
            print("Укажи цифру номера игры!")


if __name__ == "__main__":


    while True:

        welcome()
        pleer = pleer_info()
        pleer_check(pleer)

        menu(game1 = {'name' : 'Буквы алфавита, которых нет в твоем имени', 'num': 1, 'func' : letters_name, 'param' : pleer},
             game2 = {'name' : 'Угадай числа', 'num': 2, 'func' : number_guess, 'param' : None},
             game3 = {'name' : 'Выйти из игры', 'num': 3, 'func' : quit, 'param' : None})
