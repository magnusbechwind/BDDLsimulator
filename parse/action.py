from parse.subcondition import SubCondition

def parse_sub_conditions(lines):
    sub_conditions = []
    for sub_cond in lines:
        sub_conditions.append(SubCondition(sub_cond))

    return sub_conditions

def compute_bounds(subconditions: list[SubCondition]):
    x_min_constraint = 0
    x_max_constraint = 0
    y_min_constraint = 0
    y_max_constraint = 0

    for subcond in subconditions:
        x_offset = subcond.x_offset
        y_offset = subcond.y_offset

        if x_offset > 0 and x_max_constraint < x_offset:
            x_max_constraint = x_offset

        elif x_offset < 0 and x_min_constraint < abs(x_offset):
            x_min_constraint = abs(x_offset)

        if y_offset > 0 and y_max_constraint < y_offset:
            y_max_constraint = y_offset

        elif y_offset < 0 and y_min_constraint < abs(y_offset):
            y_min_constraint = abs(y_offset)

    return x_min_constraint, y_min_constraint, x_max_constraint, y_max_constraint
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

        # Compute index-bounds based on constraints and board-size

        preconditions = action_lines[2][1:]  # Line 2 is :precondition constraint*
        effects = action_lines[3][1:]  # Line 3 is :effect constraint*

        self.preconditions = parse_sub_conditions(preconditions)
        self.effects = parse_sub_conditions(effects)

        conditions = []
        conditions.extend(self.preconditions)
        conditions.extend(self.effects)

        x_min_constraint, y_min_constraint, x_max_constraint, y_max_constraint = compute_bounds(conditions)

        # Check if more constraining that board-size
        if x_min_constraint > 0:
            self.x_min = self.x_min + x_min_constraint

        if x_max_constraint > 0:
            self.x_max = self.x_max - x_max_constraint

        if y_min_constraint > 0:
            self.y_min = self.y_min + y_min_constraint

        if y_max_constraint > 0:
            self.y_max = self.y_max - y_max_constraint

        # just action name is enough:
        self.action_name = action_lines[0][-1]

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
                '\n  y_min: ' + str(self.y_min) +
                '\n  x_max: ' + str(self.x_max) +
                '\n  y_max: ' + str(self.x_max) +
                '\n  preconditions: ' + str([str(cond) for cond in self.preconditions])[1:-1] +
                '\n  effects: ' + str([str(cond) for cond in self.effects])[1:-1])
