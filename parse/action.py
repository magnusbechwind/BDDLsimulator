from util import compute


class Action:
    """
    Computes and sets the index bounds for the action having the provided constraints
    """

    def compute_and_set_index_bounds(self, constraints):
        x_min_constraint = 0
        x_max_constraint = 0
        y_min_constraint = 0
        y_max_constraint = 0

        for constraint in constraints:
            # Constraints only possible where computation happens
            if ('+' in constraint or '-' in constraint):
                # we do not want any spaces:
                constraint = constraint.replace(' ', '')
                # stripping any "(" or ")":
                assert (" " not in constraint)
                constraint = constraint.strip("(").strip(")")
                constraint = constraint.strip("NOT").strip("black").strip("white").strip("open")
                constraint = constraint.strip("(").strip(")")
                x_index, y_index = constraint.split(",")

                # check if bound is more constraining than current constraints
                if ('+' in x_index):
                    x_value = int(x_index.split("+")[-1])
                    if (x_max_constraint < x_value):
                        x_max_constraint = x_value
                elif ('-' in x_index):
                    x_value = int(x_index.split("-")[-1])
                    if (x_min_constraint < x_value):
                        x_min_constraint = x_value

                if ('+' in y_index):
                    y_value = int(y_index.split("+")[-1])
                    if (y_max_constraint < y_value):
                        y_max_constraint = y_value
                elif ('-' in y_index):
                    y_value = int(y_index.split("-")[-1])
                    if (y_min_constraint < y_value):
                        y_min_constraint = y_value

        # Check if more constraining that board-size
        if x_min_constraint > 0:
            self.x_min = self.x_min + x_min_constraint

        if x_max_constraint > 0:
            self.x_max = self.x_max - x_max_constraint

        if y_min_constraint > 0:
            self.y_min = self.y_min + y_min_constraint

        if y_max_constraint > 0:
            self.y_max = self.y_max - y_max_constraint

    def __init__(self, action_lines, x_max, y_max):

        self.action_name = ''
        self.parameters = []
        self.x_min = 1
        self.y_min = 1
        self.x_max = x_max
        self.y_max = y_max
        self.positive_preconditions = []
        self.negative_preconditions = []
        self.positive_effects = []
        self.negative_effects = []

        # Compute index-bounds based on constraints and board-size
        constraints = []
        constraints.extend(action_lines[2][1:])  # Line 2 is :precondition constraint*
        constraints.extend(action_lines[3][1:])  # Line 3 is :effect constraint*
        self.compute_and_set_index_bounds(constraints)

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
                '\n  positive preconditions: ' + str(self.positive_preconditions) +
                '\n  negative preconditions: ' + str(self.negative_preconditions) +
                '\n  positive effects: ' + str(self.positive_effects) +
                '\n  negative effects: ' + str(self.negative_effects) + '\n')
