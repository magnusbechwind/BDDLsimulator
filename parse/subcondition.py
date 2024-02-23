from parse.predicate import Predicate


class SubCondition:
    """
    Represents the sub-condition pred(e1, e2) or not(pred(e1, e2))
    """
    predicate: Predicate

    def __init__(self, predicate, x_offset, y_offset, should_be):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.predicate = predicate
        self.should_be = should_be

    def __str__(self):
        return str(self.predicate) + "(?x+" + str(self.x_offset) + ", ?y+" + str(self.y_offset) + "):" + str(self.should_be)
