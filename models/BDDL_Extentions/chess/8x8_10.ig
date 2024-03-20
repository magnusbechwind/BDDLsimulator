#boardsize
8 8
#init
black-rook(1,8) black-knight(2,8) black-bishop(3,8) black-queen(4,8) black-king(5,8) black-bishop(6,8) black-knight(7,8)  black-rook(8,8) black-pawn(1,7) black-pawn(2,7) black-pawn(3,7) black-pawn(4,7) black-pawn(5,7) black-pawn(6,7) black-pawn(7,7) black-pawn(8,7) white-rook(1,1) white-knight(2,1) white-bishop(3,1) white-queen(4,1) white-king(5,1) white-bishop(6,1) white-knight(7,1)  white-rook(8,1) white-pawn(1,2) white-pawn(2,2) white-pawn(3,2) white-pawn(4,2) white-pawn(5,2) white-pawn(6,2) white-pawn(7,2) white-pawn(8,2)
#depth
10
#blackgoal
NOT(white-king(?x, ?y))
#whitegoal
NOT(black-king(?x, ?y))
