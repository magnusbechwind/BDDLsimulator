from enum import Enum

from parse.action import Action
from parse.parser import Parse
from parse.subcondition import SubCondition


def board_range_to(to):
    return range(1, to + 1)


def board_range_from_to(start, end):
    return range(start, end + 1)


class GameBoard:

    def __str__(self):
        board = ""
        for y in board_range_to(self.y_max):
            row = ""
            for x in board_range_to(self.x_max):
                row = row + self.get(x, y) + "(" + str(x) + "," + str(y) + ") "
            board = board + row + "\n"

        return board

    def insert(self, pred, x, y):
        self.game_board[x - 1][y - 1] = pred

    def get(self, x, y):
        return self.game_board[x - 1][y - 1]

    def find_legal(self, action: Action):
        legal_indices: [tuple[int, int]] = []
        for x in board_range_from_to(action.x_min, action.x_max):
            for y in board_range_from_to(action.y_min, action.y_max):
                if self.is_fulfilled(action.preconditions, x, y):
                    legal_indices.append((x, y))
        return legal_indices

    def has_winning_state(self, goals: list[list[SubCondition]]):
        for goal in goals:
            #  These ranges can be optimized by computing max and min bounds per goal
            for x in board_range_to(self.x_max):
                for y in board_range_to(self.y_max):
                    if self.is_fulfilled(goal, x, y):
                        return True
        return False

    def is_fulfilled(self, preconditions: list[SubCondition], x, y):
        for cond in preconditions:
            is_same = self.get(x + cond.x_offset, y + cond.y_offset) == cond.predicate
            if not (is_same == cond.should_be):
                return False
        return True

    def apply_action(self, action: Action, x, y):
        for effect in action.effects:
            self.insert(effect.predicate, x + effect.x_offset, y + effect.y_offset)

    def __init__(self, parsed_instance: Parse):
        self.game_board = [["open" for _ in range(parsed_instance.y_max)] for _ in range(parsed_instance.x_max)]
        self.x_max = parsed_instance.x_max
        self.y_max = parsed_instance.y_max

        for init in parsed_instance.initial_state:
            self.game_board[init.x - 1][init.y - 1] = init.predicate


class Player(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"


class Game:

    def __init__(self, parsed_instance: Parse):

        self.game_board = GameBoard(parsed_instance)

        self.black_actions = parsed_instance.black_actions
        self.white_actions = parsed_instance.white_actions
        self.black_goals = parsed_instance.black_goals
        self.white_goals = parsed_instance.white_goals

        self.current_player: Player = Player.BLACK
        self.current_actions = self.black_actions
        self.current_goals: list[list[SubCondition]] = self.black_goals

    def play(self):
        while True:
            print("Current turn: " + str(self.current_player) + "\n")
            print(self.game_board)

            print("Current available actions for player " + str(self.current_player) + ":\n")

            self.print_legal(self.current_actions)

            move = input("Specify action and coordinates - format i x y\n")
            move = move.split(' ')
            action_index = int(move[0])
            x = int(move[1])
            y = int(move[2])

            self.game_board.apply_action(self.current_actions[action_index], x, y)

            if self.game_board.has_winning_state(self.current_goals):
                print("Player " + str(self.current_player) + " has won!")
                return

            self.change_turn()
            print("\n")

    def change_turn(self):
        if self.current_player == Player.BLACK:
            self.current_player = Player.WHITE
            self.current_actions = self.white_actions
            self.current_goals = self.white_goals
        else:
            self.current_player = Player.BLACK
            self.current_actions = self.black_actions
            self.current_goals = self.black_goals

    def print_legal(self, actions):
        for i, action in enumerate(actions):
            print("Action [" + str(i) + "] '" + action.action_name + "' is legal at: " + str(
                self.game_board.find_legal(action)))
        print("\n")
