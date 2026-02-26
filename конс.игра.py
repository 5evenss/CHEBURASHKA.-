# Было мало времени  не все успел все реализовать и все исходы достаточно затестить .
import random  
def geroi():  #Статы героя
    print('*' * 50)
    print("Создаем вашего Чебурашку")
    hp = random.randint(67,150)
    udar = random.randint(10,24)
    bronya = random.randint(1,4)
    print("Статистика вашего Чебурашки")
    print(f"Здоровье: {hp}")
    print(f"Удар: {udar}")
    print(f"Защита: {bronya}")
    print('*' * 50)
    return [hp,udar,bronya]

invent = []
pers = geroi()
print()
print("Игра началась. Удачи :)")
print("Ты оказался в лесу. Тебе нужно сделать выбор.... .")
print("1 - Дорога уходит в густой туман")
print("2 - Дорога ведет к болотам")
print("3 - Неизведанная тропинка")

vibor = input("Что выберешь ? (1/2/3):")
if vibor == '1':
    print()
    print('Ты идешь в туман ...')
    print('Кажется ты увидел что-то...')
    print('Это сундук')
    chest = random.randint(1,3)
    if chest == 1:
        print('Поздравляю ! Ты нашел неплохой Меч , который дает к Удару +3')
        pers[1] = pers[1] + 3
        invent.append('Меч (+3 к Удару)')
    elif chest == 2:
        print('Поздравляю ! Ты нашел деревянный Щит, который дает к Защите +3')
        pers[2] = pers [2] + 3
        invent.append('Щит (+3 к Защите)')
    else :
        print('Поздравляю ! Ты нашел зелье , которое дает к Здоровью +20')
        pers[0] = pers[0] + 20
        invent.append('Зелье (+20 к Здоровью *Использовано*)')
    print(f'Твои статы: Здоровье {pers[0]}, Удар {pers[1]}, Защита {pers[2]}')
    print()
    print('Ты услашал .... шаги')
    print('Из тумана выходит Пекка')

    boss1_hp = random.randint(70,100)
    boss1_udar = random.randint(5,20)
    print(f'Босс: Здоровье {boss1_hp}, Удар {boss1_udar}')

#началоо боя 
    while pers[0] > 0 and boss1_hp > 0:

        input('Нажми Enter для удара ....')
        geroi_udar = random.randint(5, pers[1])
        boss1_hp = boss1_hp - geroi_udar
        print(f'Ты нанес боссу {geroi_udar} урона . У босс осталось {boss1_hp} хп')

        if boss1_hp <= 0:
            print("Ты смог победить Рыцаря!")
            money = random.randint(1,1000)
            if money == 1:
                print(f'Сегодня не твой день . Ты заработал всего {money} рублей')
                print(f'Конец игры . Удачи')
            else:
                print(f'Ты нашел {money} монет')
                print('Конец . Спасибо за прохождение ')
            for i in invent:
                print(i)
            print(f"Финальные статы: Здоровье {pers[0]}, Удар {pers[1]}, Защита {pers[2]}")
            break
    
        boss_udar_ger = random.randint(3, boss1_udar)
        uron1 = boss_udar_ger - pers[2]
        pers[0] = pers[0] - uron1
        print(f'Босс снес {uron1} хп. У тебя осталось {pers[0]} хп')

        if pers[0] <= 0:
            print('......')
            print('Ты проиграл рыцарю .... Игра окончена')
            exit()
            

elif vibor == '2':
    print("Ты идешь по тропинке...кажется... к болоту")
    print('На пути старый мост')
    print('Под мостом ты замечаешь что-то лежит....')
    chest2 = random.randint(1,3)
    if chest2 == 1:
        print('Ты нашел странный амулет, который дает к Удару +4')
        pers[1] = pers[1] + 4
        invent.append('Амулет Шамана (+4 к Удару)')
    elif chest2 ==2:
        print('Ты нашел ботинки , которые дают  к Защите +4')
        pers[2] = pers[2] + 4
        invent.append('Болотные сапоги (+4 к Защите)')
    else:
        print('Ты нашел зелье из лягушек , которое дает к Здоровью +25')
        pers[0] = pers[0] + 25
        invent.append('Зелье из лягушек (+25 к Здоровью *Использовано*)')
    print(f'Твои статы: Здоровье {pers[0]}, Удар {pers[1]}, Защита{pers[2]}')
    print()
    print('Из болота выходит Лешрак')

    boss2_hp = random.randint(60,100)
    boss2_udar = random.randint(10,30)
    print(f'Лешрак: Здоровье {boss2_hp},Удар {boss2_udar}')
    print('Лешрак предлагает сыграть в Камень-Ножницы-Бумага до 3 побед')
    print('Если проиграешь - умираешь . Если выиграешь - получишь сокровище')

    print('1 - Согласиться на Камень-Ножницы-Бумага')
    print('2 - Сразиться с Лешраком')
    boss2_gamechange = int(input('Выбирай... (1/2)'))
    if boss2_gamechange == 1:  #К-Н-Б игра
        geroi_score = 0
        boss2_score = 0
        while geroi_score < 3 and boss2_score < 3:
            print(f'Счет : Ты {geroi_score} , Лешрак {boss2_score}')
            print('Твой ход :')
            print('1 - Камень')
            print('2 - Ножницы')
            print('3 - Бумага')

            tvoi_vibor = int(input('Выбери 1/2/3' ))
            boss_vibor = random.randint(1,3)

            if tvoi_vibor == boss_vibor :
                print('Ничья')
            elif (tvoi_vibor == 1 and boss_vibor == 2) or (tvoi_vibor == 2 and boss_vibor == 3) or (tvoi_vibor == 3 and boss_vibor == 1):
                print('Ты выиграл раун')
                geroi_score+=1
            else:
                print('Лешрак выиграл раунд')
                boss2_score+=1
        if geroi_score == 3:
            print('Ты выиграл Лешрака')
            money2 = random.randint(1,1000)
            loot2 = random.randint(1,4)
            if loot2 == 1:
                print(f'Лешрак дал тебе {money2} монет и Волшебное Кольцо, которое дает ко Всем статам +5')
                pers[0]+=5
                pers[1]+=5
                pers[2]+=5
                invent.append('Волшебное кольцо (+5 ко всему)')
            elif loot2 == 2:
                print(f'Лешрак дал {money2} монет Амулет , который дает к Здоровью +30')
                pers[0]+=30
                invent.append('Амулет (+30 к Здороью)')
            elif loot2 == 3:
                print(f'Лешрак дал тебе {money2} монет кинжал, который дает к Удару +8')
                pers[1]+=8
                invent.append('Кинжал (+8 к Урону)')
            elif loot2 == 4 :
                print(f'Лешрак дал тебе {money2} монет Чешую , которая дает к Защите +8')
                pers[2]+=8
                invent.append('Чешуя (+8 к Защите)')
            print('Полученные вещи:')
            for i in invent:
                print(i)
            print(f"Финальные статы: Здоровье {pers[0]}, Удар {pers[1]}, Защита {pers[2]}")
            print('Спасибо за игру')

        else:
            print('Ты проиграл Лешраку в игре... Кажись тебе конец')
            print('Игра окончена')
    elif boss2_gamechange == 2 :  #Если выбран файт с лешраком
        print('Ты выбрал сразиться')
        while pers[0] > 0 and boss2_hp > 0:
            input('Нажми Enter чтобы ударить')
            geroi_udar = random.randint(5, pers[1])
            boss2_hp = boss2_hp - geroi_udar
            print(f'Ты нанес {geroi_udar} урона . У Лешрака осталось {boss2_hp} хп')

            if boss2_hp <= 0:
                print('Кажется ты смог победить Лешрака')
                money2 = random.randint(1,1000)
                loot2 = random.randint(1,3)
                if loot2 == 1:
                    print(f'Ты нашел {money2} монет и Клык Лешрака , который дает к Удару +6')
                    pers[1]+=6
                    invent.append('Клык Лешрака (+6 к Удару)')
                elif loot2 == 2:
                    print(f'Ты нашел {money2} рублей и Шкуру Лешрака, который дает к Защите +6')
                    pers[2] += 6
                    invent.append('Шкура Лешрака (+6 к Защите)')
                else:
                    print(f'Ты нашел {money2} монет и Сердце Лешрака, которое дает к Здоровье +35')
                    pers[0] += 35
                    invent.append('Сердце Лешрака (+35 к Здоровью)')
                print(f'Твои статы: Здоровье {pers[0]}, Удар {pers[1]}, Защита {pers[2]}')
                print(invent)
                print('Спасибо за прохождение игры')

            boss2_udar_ger = random.randint(8, boss2_udar)  #Протестить нужно
            uron2 = boss2_udar_ger - pers[2]
            if uron2 < 0 :  
                uron2 =0
            pers[0]-=uron2

            print(f'Лешрак снес {uron2} хп. У тебя осталось {pers[0]} хп')
            
            if pers[0] <= 0:
                print('Лешрак победил')
                print('Игра окончена.В следующий раз повезет')
                exit()
else :
    print('...')
    print("Сделав неправильный выбор , ты упал в яму. Игра окончена . Сегодня не твой день (")