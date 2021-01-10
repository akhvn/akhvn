from tkinter import*

from sys import*
def func(i):
    import tournament
    global b,g,cor,pos,visited,tk
    if i in g[pos] and not i in visited:
        b[i]['fg']='#ffffff'
        pos=i
        visited+=[pos]
        open('map.txt','w').write(' '.join(list(map(str,visited))))
        b[i]['bg']='#123456'
        b[i]['fg']='#00ff00'
        tournament.start_game()
        visited=0
    else:
        tk.title('Сюда прийти нельзя')
def karta():
    
    global b,g,tk,cor,pos,visited
    tk.title('Карта Мухосранска')
    w=Canvas(tk,width=640,height=480)
    w.pack()
    f=open('hero.txt','r')
    hero_data=f.read().split()
    f.close()
    if int(hero_data[0])<=0:
        l=Label(text='Lose',font='TimesNewRoman 105',fg='#ff0000')
        l.pack()
        l.place(x=0,y=0,relwidth=1,relheight=1)
    elif pos in [5,7,8,9]:
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
            b.append(Button(tk,text=str(i),relief=RIDGE,fg='#ffffff'if i!=pos else '#00ff00',bg='#123456'if i in visited else'#654321',command=(lambda x:(lambda:func(x)))(i)))
            b[-1].pack()
            b[-1].place(x=ux-ur,y=uy-ur,width=2*ur,height=2*ur)
    #if visited==0:tk.quit()
    tk.mainloop()
b=[]
tk=Tk()
g=[[1,2,3],[0,4],[0,6,8],[0,9],[1,5],[4],[2,7],[6],[2],[3]]
cor=[(320,400),(215,350),(310,270),(390,350),(175,270),(60,210),(210,210),(300,100),(310,210),(520,240)]
visited=list(map(int,open('map.txt','r').read().split()))
pos=visited[-1]

if __name__=='__main__':
    pass
    karta()
