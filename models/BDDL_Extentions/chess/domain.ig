
#pieces
black-pawn black-rook black-knight black-bishop black-queen black-king white-pawn white-rook white-knight white-bishop white-queen white-king open
#groups
black(black-pawn black-rook black-knight black-bishop black-queen black-king)
white(white-pawn white-rook white-knight white-bishop white-queen white-king)

#blackactions
%action 1
:action pawn-move
:parameters (?x,?y)
:preconditions (black-pawn(?x,?y) open(?x, ?y-1))
:effect (open(?x,?y) black-pawn(?x,?y-1))

%action 2
:action pawn-take-left
:parameters (?x,?y)
:preconditions (black-pawn(?x,?y) white(?x-1, ?y-1)
:effect (open(?x,?y) black-pawn(?x-1 ?y-1))

%action 3
:action pawn-take-right
:parameters (?x,?y)
:preconditions (black-pawn(?x,?y) white(?x+1, ?y-1)
:effect (open(?x,?y) black-pawn(?x+1 ?y-1))



%action 4
:action rook-move
:parameters (?x ?y) (?end_x ?end_y)
:preconditions (black-rook(?x,?y) NOT(black(?end_x, ?end_y)) union(up down left right)((?x, ?y)(?end_x, ?end_y) (open)))
:effect (open(?x, ?y) black-rook(?end_x, ?end_y))



%action 5
:action knight-up-up-right
:parameters (?x ?y)
:preconditions (black-knight(?x,?y) NOT(black(?x+1 ?y-2)))
:effect (open(?x ?y) black-knight(?x+1 ?y-2))

%action 6
:action knight-up-right-right
:parameters (?x ?y)
:preconditions (black-knight(?x,?y) NOT(black(?x+2, ?y-1))
:effect (open(?x ?y) black-knight(?x+2, ?y-1))

%action 7
:action knight-down-right-right
:parameters (?x ?y)
:preconditions (black-knight(?x,?y) NOT(black(?x+2, ?y+1))
:effect (open(?x ?y) black-knight(?x+2, ?y+1))

%action 8
:action knight-down-down-right
:parameters (?x ?y)
:preconditions (black-knight(?x,?y) NOT(black(?x+1, ?y+2))
:effect (open(?x ?y) black-knight(?x+1, ?y+2))

%action 9
:action knight-down-down-left
:parameters (?x ?y)
:preconditions (black-knight(?x,?y) NOT(black(?x-1, ?y+2))
:effect (open(?x ?y) black-knight(?x-1, ?y+2))

%action 10
:action knight-down-left-left
:parameters (?x ?y)
:preconditions (black-knight(?x,?y) NOT(black(?x-2, ?y+1))
:effect (open(?x ?y) black-knight(?x-2, ?y+1))

%action 11
:action knight-up-left-left
:parameters (?x ?y)
:preconditions (black-knight(?x,?y) NOT(black(?x-2, ?y-1))
:effect (open(?x ?y) black-knight(?x-2, ?y-1))

%action 12
:action knight-up-up-left
:parameters (?x ?y)
:preconditions (black-knight(?x,?y) NOT(black(?x-1, ?y-2))
:effect (open(?x ?y) black-knight(?x-1, ?y-2))



%action 13
:action bishop-move
:parameters (?x, ?y) (?x_end, ?y_end)
:preconditions (black-bishop(?x,?y) NOT(black(?end_x, ?end_y)) union(up-right up-left down-right down-left)((?x, ?y)(?end_x, ?end_y) (open)))
:effect (open(?x, ?y) black-bishop(?x_end, ?y_end))



%action 14
:action queen-move
:parameters (?x, ?y) (?x_end, ?y_end)
:preconditions (black-queen(?x,?y) NOT(black(?end_x, ?end_y)) union(up-right up-left down-right down-left up down left right)((?x, ?y)(?end_x, ?end_y) (open)))
:effect (open(?x, ?y) black-queen(?x_end, ?y_end))



%action 15
:action king-up-right
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black(?x+1, ?y-1))
:effect (open(?x ?y) black-king(?x+1 ?y-1))

%action 16
:action king-up
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black(?x, ?y-1))
:effect (open(?x ?y) black-king(?x, ?y-1))

%action 17
:action king-up-left
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black(?x-1, ?y-1))
:effect (open(?x ?y) black-king(?x-1, ?y-1))

%action 18
:action king-left
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black(?x-1, ?y))
:effect (open(?x ?y) black-king(?x-1, ?y))

%action 19
:action king-left-down
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black(?x-1, ?y+1))
:effect (open(?x ?y) black-king(?x-1, ?y+1))

%action 20
:action king-down
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black(?x, ?y+1))
:effect (open(?x ?y) black-king(?x, ?y+1))

%action 21
:action king-down-right
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black(?x-1, ?y+1))
:effect (open(?x ?y) black-king(?x-1, ?y+1))

%action 22
:action king-right
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black(?x-1, ?y))
:effect (open(?x ?y) black-king(?x-1, ?y))



#whiteactions
%action 1
:action pawn-move
:parameters (?x,?y)
:preconditions (white-pawn(?x,?y) open(?x, ?y+1))
:effect (open(?x,?y) white-pawn(?x,?y+1))

%action 2
:action pawn-take-left
:parameters (?x,?y)
:preconditions (white-pawn(?x,?y) black(?x-1, ?y+1)
:effect (open(?x,?y) white-pawn(?x-1 ?y+1))

%action 3
:action pawn-take-right
:parameters (?x,?y)
:preconditions (white-pawn(?x,?y) black(?x+1, ?y+1)
:effect (open(?x,?y) white-pawn(?x+1 ?y+1))



%action 4
:action rook-move
:parameters (?x ?y) (?end_x ?end_y)
:preconditions (white-rook(?x,?y) NOT(white(?end_x, ?end_y)) union(up down left right)((?x, ?y)(?end_x, ?end_y) (open)))
:effect (open(?x, ?y) white-rook(?end_x, ?end_y))



%action 5
:action knight-up-up-right
:parameters (?x ?y)
:preconditions (white-knight(?x,?y) NOT(white(?x+1 ?y-2)))
:effect (open(?x ?y) white-knight(?x+1 ?y-2))

%action 6
:action knight-up-right-right
:parameters (?x ?y)
:preconditions (white-knight(?x,?y) NOT(white(?x+2, ?y-1))
:effect (open(?x ?y) white-knight(?x+2, ?y-1))

%action 7
:action knight-down-right-right
:parameters (?x ?y)
:preconditions (white-knight(?x,?y) NOT(white(?x+2, ?y+1))
:effect (open(?x ?y) white-knight(?x+2, ?y+1))

%action 8
:action knight-down-down-right
:parameters (?x ?y)
:preconditions (white-knight(?x,?y) NOT(white(?x+1, ?y+2))
:effect (open(?x ?y) white-knight(?x+1, ?y+2))

%action 9
:action knight-down-down-left
:parameters (?x ?y)
:preconditions (white-knight(?x,?y) NOT(white(?x-1, ?y+2))
:effect (open(?x ?y) white-knight(?x-1, ?y+2))

%action 10
:action knight-down-left-left
:parameters (?x ?y)
:preconditions (white-knight(?x,?y) NOT(white(?x-2, ?y+1))
:effect (open(?x ?y) white-knight(?x-2, ?y+1))

%action 11
:action knight-up-left-left
:parameters (?x ?y)
:preconditions (white-knight(?x,?y) NOT(white(?x-2, ?y-1))
:effect (open(?x ?y) white-knight(?x-2, ?y-1))

%action 12
:action knight-up-up-left
:parameters (?x ?y)
:preconditions (white-knight(?x,?y) NOT(white(?x-1, ?y-2))
:effect (open(?x ?y) white-knight(?x-1, ?y-2))



%action 13
:action bishop-move
:parameters (?x, ?y) (?x_end, ?y_end)
:preconditions (white-bishop(?x,?y) NOT(white(?end_x, ?end_y)) union(up-right up-left down-right down-left)((?x, ?y)(?end_x, ?end_y) (open)))
:effect (open(?x, ?y) white-bishop(?x_end, ?y_end))



%action 14
:action queen-move
:parameters (?x, ?y) (?x_end, ?y_end)
:preconditions (white-queen(?x,?y) NOT(white(?end_x, ?end_y)) union(up-right up-left down-right down-left up down left right)((?x, ?y)(?end_x, ?end_y) (open)))
:effect (open(?x, ?y) white-queen(?x_end, ?y_end))



%action 15
:action king-up-right
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white(?x+1, ?y-1))
:effect (open(?x ?y) white-king(?x+1 ?y-1))

%action 16
:action king-up
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white(?x, ?y-1))
:effect (open(?x ?y) white-king(?x, ?y-1))

%action 17
:action king-up-left
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white(?x-1, ?y-1))
:effect (open(?x ?y) white-king(?x-1, ?y-1))

%action 18
:action king-left
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white(?x-1, ?y))
:effect (open(?x ?y) white-king(?x-1, ?y))

%action 19
:action king-left-down
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white(?x-1, ?y+1))
:effect (open(?x ?y) white-king(?x-1, ?y+1))

%action 20
:action king-down
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white(?x, ?y+1))
:effect (open(?x ?y) white-king(?x, ?y+1))

%action 21
:action king-down-right
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white(?x-1, ?y+1))
:effect (open(?x ?y) white-king(?x-1, ?y+1))

%action 22
:action king-right
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white(?x-1, ?y))
:effect (open(?x ?y) white-king(?x-1, ?y))

