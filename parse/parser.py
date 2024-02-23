from parse import action


def combine(args, path):
    domain_file = args.domain
    problem_file = args.problem

    f_domain = open(domain_file, "r")
    lines = f_domain.readlines()

    f_domain.close()

    parsed_dict = {}

    f_combined_file = open(path, 'w')
    f_combined_file.writelines(lines)

    f_problem = open(problem_file, "r")
    lines = f_problem.readlines()

    f_combined_file.writelines(lines)

class Parse:

    def __init__(self, args):
        self.args = args
        self.parsed_dict = {}
        self.black_actions = []

        problem_path = 'intermediate_files/combined_input.ig'
        combine(args, problem_path)

        f = open(problem_path, 'r')
        lines = f.readlines()

        for line in lines:
            stripped_line = line.strip("\n").strip(" ").split(" ")

            if ('%' == line[0] or line == '\n'): #ignoring comments
                continue
            if ("#" in line):
                new_key = line.strip("\n")
                self.parsed_dict[new_key] = []
            else:
                self.parsed_dict[new_key].append(stripped_line)

        black_action_list = []
        count = 0
        one_action_lines = []
        for line in self.parsed_dict['#blackactions']:
            # for every 5 lines, call the action to make an object and reset:
            if (count == 4):
                black_action_list.append(one_action_lines)
                count = 0
                one_action_lines = []
            # with or without resetting we need to read the current line:
            one_action_lines.append(line)
            count = count + 1
        black_action_list.append(one_action_lines)

        for black_action in black_action_list:
            self.black_actions.append(action.Action(black_action, 5, 5))


