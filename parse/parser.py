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


def parse_initial_state(parsed_dict):
    if len(parsed_dict["#init"]) > 0:
        lines = parsed_dict["#init"][0]
        initial_state = []
        for line in lines:
            initial_state.append(initpredicate.InitPredicate(line))
        return initial_state
    return []


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
        self.black_goals = []
        self.white_goals = []

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

        self.initial_state = parse_initial_state(self.parsed_dict)

        # parse depth
        self.depth = int(self.parsed_dict["#depth"][0][0])

        # Parse problem file (action list)
        self.black_actions = parse_action_list(self.parsed_dict["#blackactions"], self.x_max, self.y_max)
        self.white_actions = parse_action_list(self.parsed_dict["#whiteactions"], self.x_max, self.y_max)

        black_goals = self.parsed_dict["#blackgoal"]
        for black_goal in black_goals:
            self.black_goals.append(action.parse_sub_conditions(black_goal, self.x_max, self.y_max))

        white_goals = self.parsed_dict["#whitegoal"]
        for white_goals in white_goals:
            self.white_goals.append(action.parse_sub_conditions(white_goals, self.x_max, self.y_max))

    def __str__(self):
        string = ('Board-size: ' + str(self.x_max) + 'x' + str(self.y_max) + '\n' +
                  'Initial state: ' + str([str(init) for init in self.initial_state])[1:-1] + '\n' +
                  'Depth: ' + str(self.depth) + '\n' +
                  'Black Goals: \n')

        for goal in self.black_goals:
            for cond in goal:
                string = string + str(cond)
            string = string + '\n'

        string = string + "White Goals: \n"

        for goal in self.white_goals:
            for cond in goal:
                string = string + str(cond)
            string = string + '\n'

        string = string + "Black Actions: \n"

        for black_action in self.black_actions:
            string = string + str(black_action) + '\n'

        string = string + "White Actions: \n"

        for white_action in self.white_actions:
            string = string + str(white_action) + '\n'

        return string
