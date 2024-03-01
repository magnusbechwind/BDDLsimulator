class SubCondition:
    """
    Represents the sub-condition pred(e1, e2) or not(pred(e1, e2))
    """

    def __init__(self, sub_cond):
        self.x_offset = 0
        self.y_offset = 0
        self.predicate = ""
        self.should_be = True

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
            self.x_offset = x_value

        elif ('-' in x_index):
            x_value = int(x_index.split("-")[-1])
            self.x_offset = - x_value

        if ('+' in y_index):
            y_value = int(y_index.split("+")[-1])
            self.y_offset = y_value

        elif ('-' in y_index):
            y_value = int(y_index.split("-")[-1])
            self.y_offset = - y_value

    def __str__(self):
        string = self.predicate + "(?x"
        if self.x_offset > 0:
            string = string + "+" + str(self.x_offset)
        if self.x_offset < 0:
            string = string + str(self.x_offset)
        string = string + ",?y"
        if self.y_offset > 0:
            string = string + "+" + str(self.y_offset)
        if self.y_offset < 0:
            string = string + str(self.y_offset)

        string = string + ")"

        if self.should_be:
            return string
        else:
            return "NOT(" + string + ")"
