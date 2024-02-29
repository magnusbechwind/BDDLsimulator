class InitPredicate:
    """
    Represents the #init predicate pred(int, int)
    """

    def __init__(self, pred_str):
        pred_str = pred_str.replace(' ', '').split("(")
        self.predicate = pred_str[0]
        pred_str = pred_str[1].strip(")").split(",")
        self.x = int(pred_str[0])
        self.y = int(pred_str[1])

    def __str__(self):
        return self.predicate + "(" + str(self.x) + "," + str(self.y) + ")"
