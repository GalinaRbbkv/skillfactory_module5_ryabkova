# исключения:
from random import randint
import random



class BoardException (Exception):
    pass
class BoardOutException (BoardException):
    def __str__(self):
        return "вы пытались выстрелить мимо доски!"
class BoardUsedException (BoardException):
    def __str__(self):
        return "вы уже стреляли в эту клетку"
class BoardWrongShipException (BoardException):   #исключение для правильного размещения кораблей
    pass

class Dot:  #класс точек
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):      # #метод для сравнения точек
        return self.x == other.x and self.y == other.y

    def __repr__(self):  #метод для вывода точек в консоль
        return f"Dot({self.x}, {self.y})"

class Ship:  #класс корабля описывается нос и далее от носа
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o   #ориентация корабли (0-вертикаль, 1-горизонталь)
        self.lives = l   #жизни корабля
    @property

    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i
            elif self.o == 1:
                cur_y += i
            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots

    def shooten(self, shot):  # проверяем попали или нет
        return shot in self.dots


class Board: #класс игрового поля
    def __init__(self, hid = False, size = 6):
        self.size = size
        self.hid = hid  #нужно ли поле скрывать

        self.count = 0 # количество пораженных кораблей

        self.field = [ ["0"] * size for _ in range(size) ]

        self.busy = [] #занятые точки
        self.ships = [] #список кораблей

    def __str__(self):
        res = ""
        res += " | 1 | 2 | 3 | 4 | 5 | 6 | "
        for i, row in enumerate(self.field):
            res += f"\n{i +1}| " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("♥", "0")
        return res
    def out (self, d):  #метод для проверки находится ли точка в пределах доски
        return not((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contour(self, ship, verb = False):  #контур вокруг точки чтоб разделять корабли
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def add_ship(self, ship):  #размещение корабля
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "♥"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):   #  выстрел
        if self.out(d):
            raise BoardOutException()
        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.shooten(d):
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb = True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True
        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False
    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count == len(self.ships)



class Player:  #Класс игрока
    def __init__(self, board, enemy):
        self.board = board   # наша доска
        self.enemy = enemy # доска противника

    def ask(self):
        raise NotImplementedError

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))   #случайно генерируем две точки от 0 до 5 - для выстрела
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print("Введите ДВЕ координаты ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print("введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)

class Game:

    def try_board(self):       #метод с попытками для создания доски с кораблями
        lens = [3, 2, 2, 1, 1, 1, 1]  #длинны кораблей
        board = Board(size = self.size)
        attempts = 0   #количество попыток поставить корабли
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(random.randint(0, self.size), random.randint(0, self.size)), l, random.randint(0, 1))

                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass

        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board


    def __init__(self, size=6):  #конструктор игры
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True   # скрыли доску противника

        self.ai = AI(co, pl)
        self.us = User(pl, co)


    def greet(self):     #приветсвие
        print("------------------")
        print(" Приветствуем вас ")
        print("     в игре       ")
        print("   Морской бой    ")
        print("------------------")
        print("формат ввода: x y ")
        print("x - номер строки  ")
        print("y - номер столбца ")


    def loop(self):      # игровой цикл
        num = 0   #номер хода
        while True:
            print("-" * 20)
            print("доска пользователя: ")
            print(self.us.board)
            print("-" * 20)
            print("доска компьютера: ")
            print(self.ai.board)
            print("-" * 20)
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("Ходит компьютер !")
                repeat = self.ai.move()

            if repeat:     #повтор хода поэтому номер хода уменьшаем чтоб он остался предыдущим
                num -= 1

            if self.ai.board.defeat(): # проверка если все корабли убиты
                print("-" * 20)
                print("пользователь выиграл!")
                break

            if self.us.board.defeat():  # проверка если все корабли убиты
                print("-" * 20)
                print("компьютер выиграл!")
                break
            num += 1

    def start(self):   #все совмещает
        self.greet()
        self.loop()

g = Game()
g.start()















