import argparse

from parse.parser import Parse as parse
from game.game import Game

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

if __name__ == '__main__':
    text = "A tool to for simulating BDDL problems"
    parser = argparse.ArgumentParser(description=text, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-D", "--domain", help="domain file path", default="models/SAT2023_GDDL/GDDL_models/breakthrough/domain.ig")
    parser.add_argument("-P", "--problem", help="problem file path", default="models/SAT2023_GDDL/GDDL_models/breakthrough/2x4_13.ig")
    parser.add_argument("--debug", type=int, help="[0/1], default 0", default=0)
    parser.add_argument("--print_indices", type=int, help="whether to print indices on game-board, [0/1] defaults 1", default=1)
    parser.add_argument("--show_grid", type=int, help="whether to print grid, [0/1] defaults 1", default=1)

    args = parser.parse_args()

    parsed_instance = parse(args)

    game = Game(parsed_instance, args.show_grid == 1, args.print_indices == 1)

    if args.debug == 1:
        print(parsed_instance)

    game.play()









