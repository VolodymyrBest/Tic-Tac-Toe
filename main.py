from random import choice


class Game:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = list(range(self.x, self.y))

    def draw_board(self):
        print("-------------")
        for i in range(3):
            print("|", self.board[0 + i*3], "|", self.board[1 + i*3], "|", self.board[2 + i*3], "|")
            print("-------------")

    def take_input(self, player_token):
        while True:
            player_answer = input("Куда поставим " + player_token + "? ")
            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if 1 <= player_answer <= 9:
                if str(self.board[player_answer - 1]) not in 'XO':
                    self.board[player_answer - 1] = player_token
                    break
                else:
                    print("Эта клеточка уже занята")
            else:
                print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

    def bot_move(self, player_token):
        board_list = []
        for i in self.board:
            if str(i) not in 'XO':
                board_list.append(i)
        bot_answer = choice(board_list)
        self.board[int(bot_answer) - 1] = player_token

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in win_coord:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]]:
                return self.board[i[0]]
        return False


if __name__ == '__main__':

    game = Game(1, 10)

    def main():
        counter = 0
        while True:
            game.draw_board()
            if counter % 2 == 0:
                game.take_input("X")
            else:
                game.bot_move("O")   #<-- если играет 2 человека заменить на game.take_input("O")
            counter += 1
            if counter > 4:
                result = game.check_win()
                if result:
                    print(result, "выиграл!")
                    break
            if counter == 9:
                print("Ничья!")
                break

    main()

