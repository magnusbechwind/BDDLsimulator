# Does addition and subtraction for now in the string,
# assuming only two numbers in the computation string:
def compute(string):
    # no spaces:
    assert (" " not in string)
    # if addition:
    if ("+" in string):
        split_str = string.split("+")
        sum = int(split_str[0]) + int(split_str[1])
        return sum
    elif ('-' in string):
        split_str = string.split("-")
        dif = int(split_str[0]) - int(split_str[1])
        return dif
    else:
        # nothing to compute:
        return int(string)
