import argparse

from parse.parser import Parse as parse
from game.game import Game

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

if __name__ == '__main__':
    text = "A tool to for simulating BDDL problems"
    parser = argparse.ArgumentParser(description=text, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-D", "--domain", help="domain file path", default="models/SAT2023_GDDL/GDDL_models/connect-c/domain.ig")
    parser.add_argument("-P", "--problem", help="problem file path", default="models/SAT2023_GDDL/GDDL_models/connect-c/2x2_3_connect2.ig")
    parser.add_argument("--debug", type=int, help="[0/1], default 0", default=0)

    # TODO remove
    parser.add_argument("--test", type=int, default= 0)

    args = parser.parse_args()
    if args.test == 1:
        args.domain = "./models/SAT2023_GDDL/GDDL_models/breakthrough/domain.ig"
        args.problem = "./models/SAT2023_GDDL/GDDL_models/breakthrough/3x6_9.ig"

    parsed_instance = parse(args)

    game = Game(parsed_instance)
    game.play()









