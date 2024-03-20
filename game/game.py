from enum import Enum

from parse.action import Action
from parse.parser import Parse
from parse.subcondition import SubCondition, CoordinateType


def board_range_to(to):
    return range(1, to + 1)


def board_range_from_to(start, end):
    return range(start, end + 1)


def coordinates_from_cond(cond, x, y):
    if cond.x_type == CoordinateType.ABSOLUTE:
        final_x = cond.x
    else:  # If not ABSOLUTE then it is an offset to be applied
        final_x = x + cond.x
    if cond.y_type == CoordinateType.ABSOLUTE:
        final_y = cond.y
    else:
        final_y = y + cond.y
    return final_x, final_y


def pad_to_size(string, size):
    final_string = string
    for _ in range(len(string), size):
        final_string = final_string + " "

    return final_string


class GameBoard:

    def __str__(self):
        board = ""
        line = "-" * (self.padding_target + 3) * self.x_max + "-"
        if self.show_grid:
            board = board + line + "\n"
        for y in board_range_to(self.y_max):
            row = ""
            if self.show_grid:
                row = "|"
            for x in board_range_to(self.x_max):
                pred = self.get(x, y)
                coordinates = "(" + str(x) + "," + str(y) + ")"
                if self.print_indices:
                    pred = pred + coordinates
                pred = pad_to_size(pred, self.padding_target)
                if self.show_grid:
                    pred = pred + "|"
                row = row + '  ' + pred

            board = board + row + "\n"
            if self.show_grid:
                board = board + line
            board = board + "\n"
        return board

    def insert(self, pred, x, y):
        self.game_board[x - 1][y - 1] = pred

    def insert_from_cond(self, pred, cond, x, y):

        final_x, final_y = coordinates_from_cond(cond, x, y)

        self.insert(pred, final_x, final_y)

    def get(self, x, y):
        return self.game_board[x - 1][y - 1]

    def get_from_cond(self, cond: SubCondition, x, y):

        final_x, final_y = coordinates_from_cond(cond, x, y)

        return self.get(final_x, final_y)

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

            if x < cond.x_min:
                return False
            if x > cond.x_max:
                return False
            if y < cond.y_min:
                return False
            if y > cond.y_max:
                return False

            is_same = self.get_from_cond(cond, x, y) == cond.predicate
            if not (is_same == cond.should_be):
                return False
        return True

    def apply_action(self, action: Action, x, y):
        for effect in action.effects:
            self.insert_from_cond(effect.predicate, effect, x, y)

    def __init__(self, parsed_instance: Parse, show_grid, print_indices):
        self.game_board = [["open" for _ in range(parsed_instance.y_max)] for _ in range(parsed_instance.x_max)]
        self.x_max = parsed_instance.x_max
        self.y_max = parsed_instance.y_max
        self.padding_target = 0
        self.show_grid = show_grid
        self.print_indices = print_indices

        predicates = ["open", "black", "white"]
        for predicate in predicates:
            if len(predicate) > self.padding_target:
                self.padding_target = len(predicate)

        if self.print_indices:
            self.padding_target = self.padding_target + len(str(self.x_max)) + len(str(self.y_max)) + 3

        for init in parsed_instance.initial_state:
            self.game_board[init.x - 1][init.y - 1] = init.predicate


class Player(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"


class Game:

    def __init__(self, parsed_instance: Parse, show_grid, print_indices):

        self.game_board = GameBoard(parsed_instance, show_grid, print_indices)

        self.black_actions = parsed_instance.black_actions
        self.white_actions = parsed_instance.white_actions
        self.black_goals = parsed_instance.black_goals
        self.white_goals = parsed_instance.white_goals

        self.current_player: Player = Player.BLACK
        self.current_actions = self.black_actions
        self.current_goals: list[list[SubCondition]] = self.black_goals
        self.legal_moves = []

    def play(self):
        while True:
            print("Current turn: " + str(self.current_player) + "\n")
            print(self.game_board)

            print("Current available actions for player " + str(self.current_player) + ":\n")

            self.print_legal(self.current_actions)

            while True:
                move = input("Specify action and coordinates - format (action_index x y) (q to quit)\n")

                if move.lower() == 'q':
                    exit(0)

                move = move.split(' ')
                try:
                    action_index = int(move[0])
                    x = int(move[1])
                    y = int(move[2])
                except:
                    print("Wrong input format")
                    continue

                if not (action_index < len(self.legal_moves)):
                    print("Action index " + str(action_index) + " not valid")
                    continue

                if not (x, y) in self.legal_moves[action_index]:
                    action = self.current_actions[action_index].action_name
                    print(action + " not valid for indices: " + "(" + str(x) + ", " + str(y) + ")")
                    continue

                break

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
        self.legal_moves = []
        for i, action in enumerate(actions):
            legal = self.game_board.find_legal(action)
            self.legal_moves.insert(i, legal)
            print("Action [" + str(i) + "] '" + action.action_name + "' is legal at: " + str(legal))
        print("\n")
