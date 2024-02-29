from parse import action
from parse import initpredicate


def combine(args, path):
    domain_file = args.domain
    problem_file = args.problem

    f_domain = open(domain_file, "r")
    lines = f_domain.readlines()

    f_domain.close()

    f_combined_file = open(path, 'w')
    f_combined_file.writelines(lines)

    f_problem = open(problem_file, "r")
    lines = f_problem.readlines()

    f_combined_file.writelines(lines)


def parse_action_list(lines, x_max, y_max):
    if len(lines) == 0:
        return []  # No actions to parse
    action_list = []
    actions = []
    count = 0
    one_action_lines = []
    for line in lines:
        # for every 5 lines, call the action to make an object and reset:
        if (count == 4):
            action_list.append(one_action_lines)
            count = 0
            one_action_lines = []
        # with or without resetting we need to read the current line:
        one_action_lines.append(line)
        count = count + 1
    action_list.append(one_action_lines)

    for black_action in action_list:
        actions.append(action.Action(black_action, x_max, y_max))

    return actions

def parse_initial_state(lines: [str]):
    initial_state = []
    for line in lines:
        initial_state.append(initpredicate.InitPredicate(line))
    return initial_state



class Parse:

    def __init__(self, args):
        self.args = args
        self.parsed_dict = {}
        self.black_actions = []
        self.white_actions = []
        self.x_max = 0
        self.y_max = 0
        self.initial_state = []
        self.depth = 0

        problem_path = 'intermediate_files/combined_input.ig'
        combine(args, problem_path)

        f = open(problem_path, 'r')
        lines = f.readlines()

        for line in lines:
            stripped_line = line.strip("\n").strip(" ").split(" ")

            if ('%' == line[0] or line == '\n'):  # ignoring comments
                continue
            if ("#" in line):
                new_key = line.strip("\n")
                self.parsed_dict[new_key] = []
            else:
                self.parsed_dict[new_key].append(stripped_line)

        # Parse domain file
        size = self.parsed_dict["#boardsize"][0]

        self.x_max = int(size[0])
        self.y_max = int(size[1])

        self.initial_state = parse_initial_state(self.parsed_dict["#init"][0])
        print([str(x) for x in self.initial_state])

        # parse depth
        self.depth = int(self.parsed_dict["#depth"][0][0])
        print(self.depth)

        # Parse problem file (action list)
        self.black_actions = parse_action_list(self.parsed_dict["#blackactions"], self.x_max, self.y_max)
        self.white_actions = parse_action_list(self.parsed_dict["#whiteactions"], self.x_max, self.y_max)
