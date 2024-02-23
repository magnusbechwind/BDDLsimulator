from parse.predicate import Predicate
from parse.subcondition import SubCondition


class Action:

    def compute_bound_and_set_subcond(self, constraint):
        should_be = True
        x_offset = 0
        y_offset = 0

        # we do not want any spaces:
        constraint = constraint.replace(' ', '')
        # stripping any "(" or ")":
        assert (" " not in constraint)
        constraint = constraint.strip("(").strip(")")

        if constraint[:3] == "NOT":
            should_be = False

        constraint = constraint.strip("NOT").split("(", 1)
        pred_str = constraint[0]
        pred = Predicate(pred_str)

        constraint = constraint[1]
        constraint = constraint.strip("(").strip(")")
        x_index, y_index = constraint.split(",")

        # check if bound is more constraining than current constraints
        if ('+' in x_index):
            x_value = int(x_index.split("+")[-1])
            x_offset = x_value
            if (self.x_max_constraint < x_value):
                self.x_max_constraint = x_value
        elif ('-' in x_index):
            x_value = int(x_index.split("-")[-1])
            x_offset = - x_value
            if (self.x_min_constraint < x_value):
                self.x_min_constraint = x_value

        if ('+' in y_index):
            y_value = int(y_index.split("+")[-1])
            y_offset = y_value
            if (self.y_max_constraint < y_value):
                self.y_max_constraint = y_value
        elif ('-' in y_index):
            y_value = int(y_index.split("-")[-1])
            y_offset = - y_value
            if (self.y_min_constraint < y_value):
                self.y_min_constraint = y_value

        return SubCondition(pred, x_offset, y_offset, should_be)

    def compute_and_set_index_bounds(self, constraints):

        """
        Computes and sets the index bounds for the action having the provided constraints
        """

        for constraint in constraints[1:]:
            sub_cond = self.compute_bound_and_set_subcond(constraint)

            # Append to preconditions or effects depending on what we were parsing
            if constraints[0] == ":precondition":
                self.preconditions.append(sub_cond)
            elif constraints[0] == ":effect":
                self.effects.append(sub_cond)

    def __init__(self, action_lines, x_max, y_max):

        self.action_name = ''
        self.parameters = []
        self.x_min_constraint = 0
        self.x_max_constraint = 0
        self.y_min_constraint = 0
        self.y_max_constraint = 0
        self.x_min = 1
        self.y_min = 1
        self.x_max = x_max
        self.y_max = y_max
        self.preconditions = []
        self.effects = []

        # Compute index-bounds based on constraints and board-size

        preconditions = action_lines[2]  # Line 2 is :precondition constraint*
        effects = action_lines[3]  # Line 3 is :effect constraint*
        self.compute_and_set_index_bounds(preconditions)
        self.compute_and_set_index_bounds(effects)

        # Check if more constraining that board-size
        if self.x_min_constraint > 0:
            self.x_min = self.x_min + self.x_min_constraint

        if self.x_max_constraint > 0:
            self.x_max = self.x_max - self.x_max_constraint

        if self.y_min_constraint > 0:
            self.y_min = self.y_min + self.y_min_constraint

        if self.y_max_constraint > 0:
            self.y_max = self.y_max - self.y_max_constraint

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
