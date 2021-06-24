import tkinter, random

okno = tkinter.Tk();
okno.geometry('600x600');

holst = tkinter.Canvas(okno, width=600, height=600);
holst.pack();

game = list(range(1, 17))

r = 150;

def platon_dont_like_work():
    ss = 0;
    da = True
    for i in game:
        if i-1 != ss:
            da = False;
            break;
        else:
            ss=i;
    holst.delete('all');
    for x in range(4):
        for y in range(4):
            number = 4*y+x
            if game[number] == 16:
                continue
            holst.create_rectangle(
                x*r, y*r,
                x*r+r, y*r+r,
                fill='#7700FF');
            holst.create_text(
                x*r+r/2, y*r+r/2,
                text = game[number],
                font = 'TimesNewRoman 40');

random.shuffle(game);
platon_dont_like_work();

def Vanya(event):
    x = event.x // r
    y = event.y // r
    number = 4*y+x
    zero_number = game.index(16) #Номер ячейки где нуль
    deference = abs (number - zero_number);
    if deference == 4:
        game[number], game[zero_number] = game[zero_number], game[number]
        platon_dont_like_work();
    elif deference == 1:
        a = max(number, zero_number)
        if a%4 != 0:
             game[number], game[zero_number] = game[zero_number], game[number]
             platon_dont_like_work()

holst.bind('<Button-1>', Vanya);
