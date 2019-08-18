# coding: utf-8
""""Creator Andrey (LarceFox) Soubbotin"""
game_name = '''
 ______   ______     __  __     ______      ______     ______   ______
/\__  _\ /\  ___\   /\_\_\_\   /\__  _\    /\  == \   /\  == \ /\  ___\\
\/_/\ \/ \ \  __\   \/_/\_\/_  \/_/\ \/    \ \  __<   \ \  _-/ \ \ \__ \\
   \ \_\  \ \_____\   /\_\/\_\    \ \_\     \ \_\ \_\  \ \_\    \ \_____\\
    \/_/   \/_____/   \/_/\/_/     \/_/      \/_/ /_/   \/_/     \/_____/
'''

print("Добро пожаловать в игру", game_name)

if __name__ == "__main__":

    gamer = {'name': {'question': 'Как тебя зовут?\n', 'answer': None},
              'age': {'question': 'Сколько тебе лет?\n', 'answer': None},
              'sex': {'question': 'Какого ты пола? М/Ж\n', 'answer': None},
              'pet_name': {'question': 'Имя твоего питомца\n', 'answer': None},
              'gambler_bool': {'question': 'Любишь играть в игры? да/нет\n', 'answer': None},
              }

    for item in gamer:
        
        while True:
            temp = input(gamer[item]['question']).lower()

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
            gamer[item]['answer'] = temp
            break



    while True:

        if gamer['age']['answer'] < 18:
                print('Тебе нельзя играть')
                break

        elif gamer['age']['answer'] > 90:
            print("Для тебя это может быть утомительно!")

            for i in range(2):
                if input('Вы точно хотите играть? (Да/Нет)\n') == 'Да':
                    pass
                else:
                    print('До свидания, ', gamer['name']['answer'], ' !')
                    quit()

            print('Хорошо тогда начнем игру!')

        else:
            print('Добро пожаловать в Игру, ', gamer['name']['answer'], ' !')

        print('Я могу назвать буквы алфавита, которых нет в твоем имени. и Произнести их.')

        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        for char in letters:
            if char not in gamer['name']['answer'].lower():
                print(char)



        # Задание от 15.08.19г.
        print('Я задумал 16 чисел от 1 - 16 и расположил их в произвольном порядке:\n')

        numbers = (16, 1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8)
        masq = list('*' * len(numbers)) #  Генерация звездочек по количеству элементов
        moves = 0

        for i, number in enumerate(numbers):

            i += 1 #  enumerate - нумерует элементы с "0" для приведения к нумерации элементов с "1"
            output = ('|%s' * len(numbers) + '|') % tuple(masq) #  выводит маску |*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|
            print(output)

            while True:

                moves += 1

                index = input(f'Угадай на каком по счету месте цифра {i}\n')

                if  not index.isdigit(): #  проверка на численное, если да - приводит к int, и переводит в нумерацию с "0"

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
