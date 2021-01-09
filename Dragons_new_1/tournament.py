# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from tkinter import*
global tk
tk = Tk()
def func1():

    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    if 1 in g[pos]:
        pos=1
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
        start_game()
        exit()
    else:
        tk.title('Сюда прийти нельзя')
def func2():


    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    if 2 in g[pos]:
        pos=2
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
        start_game()
        exit()
    else:
        tk.title('Сюда прийти нельзя')
def func3():

    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    if 3 in g[pos]:
        pos=3
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
        start_game()
        exit()
    else:
        tk.title('Сюда прийти нельзя')
def func4():

    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    if 4 in g[pos]:
        pos=4
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
        start_game()
        exit()
    else:
        tk.title('Сюда прийти нельзя')
def func5():

    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    if 5 in g[pos]:
        pos=5
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
        start_game()
        exit()
    else:
        tk.title('Сюда прийти нельзя')
def func6():
    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    if 6 in g[pos]:
        pos=6
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
        start_game()
        exit()
    else:
        tk.title('Сюда прийти нельзя')
def func7():

    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    if 7 in g[pos]:
        pos=7
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
        start_game()
        exit()
    else:
        tk.title('Сюда прийти нельзя')
def func8():

    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    if 8 in g[pos]:
        pos=8
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
    else:
        tk.title('Сюда прийти нельзя')
def func9():

    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    if 9 in g[pos]:
        pos=9
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
        start_game()
        exit()
    else:
        tk.title('Сюда прийти нельзя')
def func0():

    if 0 in g[pos]:
        pos=0
        open('map.txt','w').write(' '.join(list(map(str,visited+[pos]))))
        start_game()
        exit()
    else:
        tk.title('Сюда прийти нельзя')

def karta():

    
    tk.title('Карта Мухосранска')
    w=Canvas(tk,width=640,height=480)
    w.pack()
    g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
    visited=list(map(int,open('map.txt','r').read().split()))
    pos=visited[-1]
    cor=[(320,400),(215,350),(310,270),(390,350),(175,270),(60,210),(210,210),(300,100),(310,210),(520,240)]
    
    if pos in [5,7,8,9]:
        l=Label(text='Win',font='TimesNewRoman 105',fg='#00ff00')
        l.pack()
        l.place(x=0,y=0,relwidth=1,relheight=1)
    else:
        for i in range(10):
            ux=cor[i][0]
            uy=cor[i][1]
            ur=15
            for e in g[i]:
                w.create_line(ux,uy,cor[e][0],cor[e][1],width=3,fill='#654321')
            if i==0:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func0)
            elif i==1:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func1)
            elif i==2:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func2)
            elif i==3:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func3)
            elif i==4:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func4)
            elif i==5:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func5)
            elif i==6:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func6)
            elif i==7:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func7)
            elif i==8:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func8)
            elif i==9:b=Button(tk,text=str(i),relief=RIDGE,fg='#00ff00'if i!=pos else '#ffffff',bg='#654321'if i in visited else'#123456',command=func9)
            b.pack()
            b.place(x=ux-ur,y=uy-ur,width=2*ur,height=2*ur)
    tk.mainloop()
def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')
        hero._experience+=10

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
        karta()
    else:
        print('К сожалению, Вы проиграли...')

def game_trollnament(hero, troll_list):
    for troll in troll_list:
        print('Вышел', troll._color, 'тролль!')
        while troll.is_alive() and hero.is_alive():
            print('Вопрос:', troll.question())
            answer = input('Ответ:')

            if troll.check_answer(answer):
                hero.attack(troll)
                print('Верно! \n** троллю неприятно **')
            else:
                troll.attack(hero)
                print('Ошибка! \n** от вас откусили кусочек... **')
        if troll.is_alive():
            break
        print('Тролль', troll._color, 'затроллен!\n')
        hero._experience+=20

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
        karta()
    else:
        print('К сожалению, Вас сожрали...')

def rod_dragon(number):
    if number%100 in [11,12,13,14]:return 'драконов'
    if number%10 in [2,3,4]:return 'дракона'
    if number%10==1:return 'дракон'
    else:return 'драконов'

def rod_troll(number):
    if number%100 in [11,12,13,14]:return 'троллей'
    if number%10 in [2,3,4]:return 'тролля'
    if number%10==1:return 'тролль'
    else:return 'троллей'

def start_game():

    try:
        if len(list(map(int,open('map.txt','r').read().split())))==1:
            print('Добро пожаловать в арифметико-ролевую игру с драконами!')
            print('Представьтесь, пожалуйста: ', end = '')
            hero = Hero(input())
            karta()
        if randint(1,2)==1:
            dragon_number = randint(2,3)
            dragon_list = generate_dragon_list(dragon_number)
            print('У Вас на пути', dragon_number, rod_dragon(dragon_number)+'!')
            game_tournament(hero, dragon_list)
            karta()
        else:
            troll_number = randint(2,3)
            troll_list = generate_troll_list(troll_number)
            print('Вам не дают пройти', troll_number, rod_troll(troll_number)+'!')
            game_trollnament(hero, troll_list)
            

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
