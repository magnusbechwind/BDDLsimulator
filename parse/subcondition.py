from enum import Enum


class CoordinateType(Enum):
    OFFSET = 1
    ABSOLUTE = 2

class SubCondition:
    """
    Represents the sub-condition pred(e1, e2) or not(pred(e1, e2))
    """

    def __init__(self, sub_cond, x_max, y_max):
        self.x = 0
        self.y = 0
        self.x_min = 1
        self.x_max = x_max
        self.y_min = 1
        self.y_max = y_max
        self.predicate = ""
        self.should_be = True
        self.x_type = None
        self.y_type = None
        self.string = sub_cond

        sub_cond = sub_cond.replace(' ', '')
        sub_cond = sub_cond.strip("(").strip(")")
        if sub_cond[:3] == "NOT":
            self.should_be = False

        sub_cond = sub_cond.strip("NOT").strip("(").split("(", 1)
        self.predicate = sub_cond[0]

        sub_cond = sub_cond[1]
        sub_cond = sub_cond.strip("(").strip(")")

        x_index, y_index = sub_cond.split(",")

        if ('+' in x_index):
            x_value = int(x_index.split("+")[-1])
            self.x = x_value
            self.x_max = self.x_max - x_value

        elif ('-' in x_index):
            x_value = int(x_index.split("-")[-1])
            self.x = - x_value
            self.x_min = self.x_min + x_value

        if ('+' in y_index):
            y_value = int(y_index.split("+")[-1])
            self.y = y_value
            self.y_max = self.y_max - y_value

        elif ('-' in y_index):
            y_value = int(y_index.split("-")[-1])
            self.y = - y_value
            self.y_min = self.y_min + y_value



    def __str__(self):
        return self.string
