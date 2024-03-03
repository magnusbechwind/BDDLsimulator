def gen_board(x, y, preds):
    print("|", end="")
    for i in range(x):
        print("----", end="")
    print("|")
    for i in range(y):
        print("| ", end="")
        for j in range(x):
            if preds[i,j] == "open":
                print("   |", end="")
            else:
                print(preds[i,j][0] + "  |")
        print("\n|", end="")
        for j in range(x):
            print("----", end="")
        print("|\n", end="")



gen_board(5, 5, [])
