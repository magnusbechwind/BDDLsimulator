from parse.subcondition import SubCondition, CoordinateType


def parse_sub_conditions(lines, x_max, y_max):
    sub_conditions = []
    for sub_cond in lines:
        sub_conditions.append(SubCondition(sub_cond, x_max, y_max))

    return sub_conditions


def compute_bounds(subconditions: list[SubCondition], x_max, y_max):
    x_min = 1
    x_max = x_max
    y_min = 1
    y_max = y_max

    for cond in subconditions:
        x_min = max(x_min, cond.x_min)
        x_max = min(x_max, cond.x_max)
        y_min = max(y_min, cond.y_min)
        y_max = min(y_max, cond.y_max)

    return x_min, x_max, y_min, y_max


class Action:

    def __init__(self, action_lines, x_max, y_max):

        self.action_name = ''
        self.parameters = []
        self.x_min = 1
        self.y_min = 1
        self.x_max = x_max
        self.y_max = y_max
        self.preconditions = []
        self.effects = []

        # just action name is enough:
        self.action_name = action_lines[0][-1]

        # Compute index-bounds based on constraints and board-size
        preconditions = action_lines[2][1:]  # Line 2 is :precondition constraint*
        effects = action_lines[3][1:]  # Line 3 is :effect constraint*

        self.preconditions = parse_sub_conditions(preconditions, x_max, y_max)
        self.effects = parse_sub_conditions(effects, x_max, y_max)

        conditions = []
        conditions.extend(self.preconditions)
        conditions.extend(self.effects)

        self.x_min, self.x_max, self.y_min, self.y_max = compute_bounds(conditions, x_max, y_max)

        # parsing the parameter names, for now restricting to one pair only:
        # asserting if the current line is parameter line:
        # assert (action_lines[1][0] == ':parameters')
        for i in range(1, len(action_lines[1])):
            parameter = action_lines[1][i].strip(")").strip("(").strip(",")
            self.parameters.append(parameter)

    def __str__(self):
        return ('action: ' + self.action_name +
                '\n  parameters: ' + str(self.parameters) +
                '\n  x_min: ' + str(self.x_min) +
                '\n  x_max: ' + str(self.x_max) +
                '\n  y_min: ' + str(self.y_min) +
                '\n  y_max: ' + str(self.y_max) +
                '\n  preconditions: ' + str([str(cond) for cond in self.preconditions])[1:-1] +
                '\n  effects: ' + str([str(cond) for cond in self.effects])[1:-1])
