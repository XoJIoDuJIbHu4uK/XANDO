XANDO = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]

ROWS = 3
COLS = 3
win =('X','X','X')
win2 = ('O','O','O')

for i in range(ROWS):
    for j in range(COLS):
        print(XANDO[i][j], end=" ")
    print()


def printing(func):
    func()
    def wrapper():
        i = int(input("Место по горизонтали(слева-направо) от 1 до 3: ")) - 1
        j = int(input("Место по вертикали(сверху-вниз) от 1 до 3: ")) - 1
        ftp = input("Введите X или O: ")
        if (ftp == "X") or (ftp == "O"):
            if XANDO[i][j] == "-":
                XANDO[i][j] = ftp
                for i in range(ROWS):
                    for j in range(COLS):
                        print(XANDO[i][j], end = " ")
                    print()
                print("---")
                print("Начало следующего хода")
            else:
                print("Место, который вы выбрали - уже занято. Повторите ввод.")
        else:
            print("Вы ввели неправильный символ. Пожалуйста, вводите X или O заглавными буквами на англ. раскладке.")
        return func
    return wrapper

@printing
def strike():
    print(" Добрый день! Это игра крестики-нолики.", "\n",
          "Для корректной работы вводите данные, как того просит программа(цифрами от 1 до 3, X или O заглавными буквами на англ. раскладке.", "\n",
          "Приятной игры!")


while True:
    if (list(win) == XANDO[0]) or (list(win2) == XANDO[0]):
        print(XANDO[0][0], "Победил")
        break
    elif (list(win) == XANDO[1]) or (list(win2) == XANDO[1]):
        print(XANDO[1][1], "Победил")
        break
    elif (list(win) == (XANDO[2])) or (list(win2) == XANDO[2]):
        print(XANDO[2][2], "Победил")
        break
    else:
        if (win == (XANDO[0][0], XANDO[1][0], XANDO[2][0])) or (win2 == (XANDO[0][0], XANDO[1][0], XANDO[2][0])):
            print(XANDO[0][0], "Победил")
            break
        elif (win == (XANDO[0][1], XANDO[1][1], XANDO[2][1])) or (win2 == (XANDO[0][1], XANDO[1][1], XANDO[2][1])):
            print(XANDO[0][1], "Победил")
            break
        elif (win == (XANDO[0][2], XANDO[1][2], XANDO[2][2])) or (win2 == (XANDO[0][2], XANDO[1][2], XANDO[2][2])):
            print(XANDO[0][2], "Победил")
            break
        else:
            if (win == (XANDO[0][0], XANDO[1][1], XANDO[2][2])) or (win2 == (XANDO[0][0], XANDO[1][1], XANDO[2][2])):
                print(XANDO[0][0], "Победил")
                break
            elif (win == (XANDO[0][2], XANDO[1][1], XANDO[2][0])) or (win2 == (XANDO[0][2], XANDO[1][1], XANDO[2][0])):
                print(XANDO[0][2], "Победил")
                break
            else:
                if "-" in XANDO:
                    print("Ничья!")
                    break
                else:
                    strike()