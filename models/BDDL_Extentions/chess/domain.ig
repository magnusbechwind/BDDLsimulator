#blackactions
%action 1
:action pawn-move
:parameters (?x,?y)
:preconditions (black-pawn(?x,?y) open(?x, ?y-1))
:effect (open(?x,?y) black-pawn(?x,?y-1))

%action 2
:action pawn-take-left
:parameters (?x,?y)
:preconditions (black-pawn(?x,?y) NOT(open(?x-1, ?y-1)) NOT(black-pawn(?x-1, ?y-1)) NOT(black-rook(?x-1, ?y-1)) NOT(black-knight(?x-1, ?y-1)) NOT(black-bishop(?x-1, ?y-1)) NOT(black-queen(?x-1, ?y-1)) NOT(black-king(?x-1, ?y-1)))
:effect (open(?x,?y) black-pawn(?x-1 ?y-1))

%action 3
:action pawn-take-right
:parameters (?x,?y)
:preconditions (black-pawn(?x,?y) NOT(open(?x+1, ?y-1)) NOT(black-pawn(?x+1, ?y-1)) NOT(black-rook(?x+1, ?y-1)) NOT(black-knight(?x+1, ?y-1)) NOT(black-bishop(?x+1, ?y-1)) NOT(black-queen(?x+1, ?y-1)) NOT(black-king(?x+1, ?y-1)))
:effect (open(?x,?y) black-pawn(?x+1 ?y-1))



%action 4
:action rook-move-horizontal
:parameters (?x ?y) (?p ?q)
:preconditions (black-rook(?x,?y) NOT(black-pawn(?p, ?q)) NOT(black-rook(?p, ?q)) NOT(black-knight(?p, ?q)) NOT(black-bishop(?p, ?q)) NOT(black-queen(?p, ?q)) NOT(black-king(?p, ?q)) sum(left right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) black-rook(?q, ?p))

%action 5
:action rook-move-vertical
:parameters (?x ?y) (?p ?q)
:preconditions (black-rook(?x,?y) NOT(black-pawn(?p, ?q)) NOT(black-rook(?p, ?q)) NOT(black-knight(?p, ?q)) NOT(black-bishop(?p, ?q)) NOT(black-queen(?p, ?q)) NOT(black-king(?p, ?q)) sum(up down)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) black-rook(?q, ?p))



%action 6
:action knight-up-up-right
:parameters (?x ?y)
:preconditions (black-pawn(?x,?y) NOT(black-pawn(?x+1, ?y-2)) NOT(black-rook(?x+1, ?y-2)) NOT(black-knight(?x+1, ?y-2)) NOT(black-bishop(?x+1, ?y-2)) NOT(black-queen(?x+1, ?y-2)) NOT(black-king(?x+1, ?y-2)))
:effect (open(?x ?y) black-knight(?x+1 ?y-2))

%action 7
:action knight-up-right-right
:parameters (?x ?y)
:preconditions (black-pawn(?x,?y) NOT(black-pawn(?x+2, ?y-1)) NOT(black-rook(?x+2, ?y-1)) NOT(black-knight(?x+2, ?y-1)) NOT(black-bishop(?x+2, ?y-1)) NOT(black-queen(?x+2, ?y-1)) NOT(black-king(?x+2, ?y-1)))
:effect (open(?x ?y) black-knight(?x+2, ?y-1))

%action 8
:action knight-down-right-right
:parameters (?x ?y)
:preconditions (black-pawn(?x,?y) NOT(black-pawn(?x+2, ?y+1)) NOT(black-rook(?x+2, ?y+1)) NOT(black-knight(?x+2, ?y+1)) NOT(black-bishop(?x+2, ?y+1)) NOT(black-queen(?x+2, ?y+1)) NOT(black-king(?x+2, ?y+1)))
:effect (open(?x ?y) black-knight(?x+2, ?y+1))

%action 9
:action knight-down-down-right
:parameters (?x ?y)
:preconditions (black-pawn(?x,?y) NOT(black-pawn(?x+1, ?y+2)) NOT(black-rook(?x+1, ?y+2)) NOT(black-knight(?x+1, ?y+2)) NOT(black-bishop(?x+1, ?y+2)) NOT(black-queen(?x+1, ?y+2)) NOT(black-king(?x+1, ?y+2)))
:effect (open(?x ?y) black-knight(?x+1, ?y+2))

%action 10
:action knight-down-down-left
:parameters (?x ?y)
:preconditions (black-pawn(?x,?y) NOT(black-pawn(?x-1, ?y+2)) NOT(black-rook(?x-1, ?y+2)) NOT(black-knight(?x-1, ?y+2)) NOT(black-bishop(?x-1, ?y+2)) NOT(black-queen(?x-1, ?y+2)) NOT(black-king(?x-1, ?y+2)))
:effect (open(?x ?y) black-knight(?x-1, ?y+2))

%action 11
:action knight-down-left-left
:parameters (?x ?y)
:preconditions (black-pawn(?x,?y) NOT(black-pawn(?x-2, ?y+1)) NOT(black-rook(?x-2, ?y+1)) NOT(black-knight(?x-2, ?y+1)) NOT(black-bishop(?x-2, ?y+1)) NOT(black-queen(?x-2, ?y+1)) NOT(black-king(?x-2, ?y+1)))
:effect (open(?x ?y) black-knight(?x-2, ?y+1))

%action 12
:action knight-up-left-left
:parameters (?x ?y)
:preconditions (black-pawn(?x,?y) NOT(black-pawn(?x-2, ?y-1)) NOT(black-rook(?x-2, ?y-1)) NOT(black-knight(?x-2, ?y-1)) NOT(black-bishop(?x-2, ?y-1)) NOT(black-queen(?x-2, ?y-1)) NOT(black-king(?x-2, ?y-1)))
:effect (open(?x ?y) black-knight(?x-2, ?y-1))

%action 13
:action knight-up-up-left
:parameters (?x ?y)
:preconditions (black-pawn(?x,?y) NOT(black-pawn(?x-1, ?y-2)) NOT(black-rook(?x-1, ?y-2)) NOT(black-knight(?x-1, ?y-2)) NOT(black-bishop(?x-1, ?y-2)) NOT(black-queen(?x-1, ?y-2)) NOT(black-king(?x-1, ?y-2)))
:effect (open(?x ?y) black-knight(?x-1, ?y-2))



%action 14
:action bishop-leftup-rightdown
:parameters (?x, ?y) (?p, ?q)
:preconditions (black-bishop(?x,?y) NOT(black-pawn(?p, ?q)) NOT(black-rook(?p, ?q)) NOT(black-knight(?p, ?q)) NOT(black-bishop(?p, ?q)) NOT(black-queen(?p, ?q)) NOT(black-king(?p, ?q)) sum(up-left down-right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) black-bishop(?p, ?q))

%action 15
:action bishop-rightup-leftdown
:parameters (?x, ?y) (?p, ?q)
:preconditions (black-bishop(?x,?y) NOT(black-pawn(?p, ?q)) NOT(black-rook(?p, ?q)) NOT(black-knight(?p, ?q)) NOT(black-bishop(?p, ?q)) NOT(black-queen(?p, ?q)) NOT(black-king(?p, ?q)) sum(down-left up-right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) black-bishop(?p, ?q))



%action 16
:action queen-leftup-rightdown
:parameters (?x, ?y) (?p, ?q)
:preconditions (black-queen(?x,?y) NOT(black-pawn(?p, ?q)) NOT(black-rook(?p, ?q)) NOT(black-knight(?p, ?q)) NOT(black-bishop(?p, ?q)) NOT(black-queen(?p, ?q)) NOT(black-king(?p, ?q)) sum(up-left down-right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) black-queen(?p, ?q))

%action 17
:action queen-rightup-leftdown
:parameters (?x, ?y) (?p, ?q)
:preconditions (black-queen(?x,?y) NOT(black-pawn(?p, ?q)) NOT(black-rook(?p, ?q)) NOT(black-knight(?p, ?q)) NOT(black-bishop(?p, ?q)) NOT(black-queen(?p, ?q)) NOT(black-king(?p, ?q)) sum(down-left up-right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) black-queen(?p, ?q))

%action 18
:action queen-move-horizontal
:parameters (?x ?y) (?p ?q)
:preconditions (black-queen(?x,?y) NOT(black-pawn(?p, ?q)) NOT(black-rook(?p, ?q)) NOT(black-knight(?p, ?q)) NOT(black-bishop(?p, ?q)) NOT(black-queen(?p, ?q)) NOT(black-king(?p, ?q)) sum(left right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) black-queen(?q ?p)

%action 19
:action queen-move-vertical
:parameters (?x ?y) (?p ?q)
:preconditions (black-queen(?x,?y) NOT(black-pawn(?p, ?q)) NOT(black-rook(?p, ?q)) NOT(black-knight(?p, ?q)) NOT(black-bishop(?p, ?q)) NOT(black-queen(?p, ?q)) NOT(black-king(?p, ?q)) sum(up down)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) black-queen(?q, ?p))




%action 20
:action king-up-right
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black-pawn(?x+1, ?y-1)) NOT(black-rook(?x+1, ?y-1)) NOT(black-knight(?x+1, ?y-1)) NOT(black-bishop(?x+1, ?y-1)) NOT(black-queen(?x+1, ?y-1)) NOT(black-king(?x+1, ?y-1)))
:effect (open(?x ?y) black-king(?x+1 ?y-1))

%action 21
:action king-up
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black-pawn(?x, ?y-1)) NOT(black-rook(?x, ?y-1)) NOT(black-knight(?x, ?y-1)) NOT(black-bishop(?x, ?y-1)) NOT(black-queen(?x, ?y-1)) NOT(black-king(?x, ?y-1)))
:effect (open(?x ?y) black-king(?x, ?y-1))

%action 22
:action king-up-left
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black-pawn(?x-1, ?y-1)) NOT(black-rook(?x-1, ?y-1)) NOT(black-knight(?x-1, ?y-1)) NOT(black-bishop(?x-1, ?y-1)) NOT(black-queen(?x-1, ?y-1)) NOT(black-king(?x-1, ?y-1)))
:effect (open(?x ?y) black-king(?x-1, ?y-1))

%action 23
:action king-left
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black-pawn(?x-1, ?y)) NOT(black-rook(?x-1, ?y)) NOT(black-knight(?x-1, ?y)) NOT(black-bishop(?x-1, ?y)) NOT(black-queen(?x-1, ?y)) NOT(black-king(?x-1, ?y)))
:effect (open(?x ?y) black-king(?x-1, ?y))

%action 24
:action king-left-down
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black-pawn(?x-1, ?y+1)) NOT(black-rook(?x-1, ?y+1)) NOT(black-knight(?x-1, ?y+1)) NOT(black-bishop(?x-1, ?y+1)) NOT(black-queen(?x-1, ?y+1)) NOT(black-king(?x-1, ?y+1)))
:effect (open(?x ?y) black-king(?x-1, ?y+1))

%action 25
:action king-down
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black-pawn(?x, ?y+1)) NOT(black-rook(?x, ?y+1)) NOT(black-knight(?x, ?y+1)) NOT(black-bishop(?x, ?y+1)) NOT(black-queen(?x, ?y+1)) NOT(black-king(?x, ?y+1)))
:effect (open(?x ?y) black-king(?x, ?y+1))

%action 26
:action king-down-right
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black-pawn(?x-1, ?y+1)) NOT(black-rook(?x-1, ?y+1)) NOT(black-knight(?x-1, ?y+1)) NOT(black-bishop(?x-1, ?y+1)) NOT(black-queen(?x-1, ?y+1)) NOT(black-king(?x-1, ?y+1)))
:effect (open(?x ?y) black-king(?x-1, ?y+1))

%action 27
:action king-right
:parameters (?x ?y)
:preconditions (black-king(?x,?y) NOT(black-pawn(?x-1, ?y)) NOT(black-rook(?x-1, ?y)) NOT(black-knight(?x-1, ?y)) NOT(black-bishop(?x-1, ?y)) NOT(black-queen(?x-1, ?y)) NOT(black-king(?x-1, ?y)))
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
:preconditions (white-pawn(?x,?y) NOT(open(?x-1, ?y+1)) NOT(white-pawn(?x-1, ?y+1)) NOT(white-rook(?x-1, ?y+1)) NOT(white-knight(?x-1, ?y+1)) NOT(white-bishop(?x-1, ?y+1)) NOT(white-queen(?x-1, ?y+1)) NOT(white-king(?x-1, ?y+1)))
:effect (open(?x,?y) white-pawn(?x-1 ?y+1))

%action 3
:action pawn-take-right
:parameters (?x,?y)
:preconditions (white-pawn(?x,?y) NOT(open(?x+1, ?y+1)) NOT(white-pawn(?x+1, ?y+1)) NOT(white-rook(?x+1, ?y+1)) NOT(white-knight(?x+1, ?y+1)) NOT(white-bishop(?x+1, ?y+1)) NOT(white-queen(?x+1, ?y+1)) NOT(white-king(?x+1, ?y+1)))
:effect (open(?x,?y) white-pawn(?x+1 ?y+1))



%action 4
:action rook-move-horizontal
:parameters (?x ?y) (?p ?q)
:preconditions (white-rook(?x,?y) NOT(white-pawn(?p, ?q)) NOT(white-rook(?p, ?q)) NOT(white-knight(?p, ?q)) NOT(white-bishop(?p, ?q)) NOT(white-queen(?p, ?q)) NOT(white-king(?p, ?q)) sum(left right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) white-rook(?q, ?p))

%action 5
:action rook-move-vertical
:parameters (?x ?y) (?p ?q)
:preconditions (white-rook(?x,?y) NOT(white-pawn(?p, ?q)) NOT(white-rook(?p, ?q)) NOT(white-knight(?p, ?q)) NOT(white-bishop(?p, ?q)) NOT(white-queen(?p, ?q)) NOT(white-king(?p, ?q)) sum(up down)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) white-rook(?q, ?p))



%action 6
:action knight-up-up-right
:parameters (?x ?y)
:preconditions (white-pawn(?x,?y) NOT(white-pawn(?x+1, ?y-2)) NOT(white-rook(?x+1, ?y-2)) NOT(white-knight(?x+1, ?y-2)) NOT(white-bishop(?x+1, ?y-2)) NOT(white-queen(?x+1, ?y-2)) NOT(white-king(?x+1, ?y-2)))
:effect (open(?x ?y) white-knight(?x+1 ?y-2))

%action 7
:action knight-up-right-right
:parameters (?x ?y)
:preconditions (white-pawn(?x,?y) NOT(white-pawn(?x+2, ?y-1)) NOT(white-rook(?x+2, ?y-1)) NOT(white-knight(?x+2, ?y-1)) NOT(white-bishop(?x+2, ?y-1)) NOT(white-queen(?x+2, ?y-1)) NOT(white-king(?x+2, ?y-1)))
:effect (open(?x ?y) white-knight(?x+2, ?y-1))

%action 8
:action knight-down-right-right
:parameters (?x ?y)
:preconditions (white-pawn(?x,?y) NOT(white-pawn(?x+2, ?y+1)) NOT(white-rook(?x+2, ?y+1)) NOT(white-knight(?x+2, ?y+1)) NOT(white-bishop(?x+2, ?y+1)) NOT(white-queen(?x+2, ?y+1)) NOT(white-king(?x+2, ?y+1)))
:effect (open(?x ?y) white-knight(?x+2, ?y+1))

%action 9
:action knight-down-down-right
:parameters (?x ?y)
:preconditions (white-pawn(?x,?y) NOT(white-pawn(?x+1, ?y+2)) NOT(white-rook(?x+1, ?y+2)) NOT(white-knight(?x+1, ?y+2)) NOT(white-bishop(?x+1, ?y+2)) NOT(white-queen(?x+1, ?y+2)) NOT(white-king(?x+1, ?y+2)))
:effect (open(?x ?y) white-knight(?x+1, ?y+2))

%action 10
:action knight-down-down-left
:parameters (?x ?y)
:preconditions (white-pawn(?x,?y) NOT(white-pawn(?x-1, ?y+2)) NOT(white-rook(?x-1, ?y+2)) NOT(white-knight(?x-1, ?y+2)) NOT(white-bishop(?x-1, ?y+2)) NOT(white-queen(?x-1, ?y+2)) NOT(white-king(?x-1, ?y+2)))
:effect (open(?x ?y) white-knight(?x-1, ?y+2))

%action 11
:action knight-down-left-left
:parameters (?x ?y)
:preconditions (white-pawn(?x,?y) NOT(white-pawn(?x-2, ?y+1)) NOT(white-rook(?x-2, ?y+1)) NOT(white-knight(?x-2, ?y+1)) NOT(white-bishop(?x-2, ?y+1)) NOT(white-queen(?x-2, ?y+1)) NOT(white-king(?x-2, ?y+1)))
:effect (open(?x ?y) white-knight(?x-2, ?y+1))

%action 12
:action knight-up-left-left
:parameters (?x ?y)
:preconditions (white-pawn(?x,?y) NOT(white-pawn(?x-2, ?y-1)) NOT(white-rook(?x-2, ?y-1)) NOT(white-knight(?x-2, ?y-1)) NOT(white-bishop(?x-2, ?y-1)) NOT(white-queen(?x-2, ?y-1)) NOT(white-king(?x-2, ?y-1)))
:effect (open(?x ?y) white-knight(?x-2, ?y-1))

%action 13
:action knight-up-up-left
:parameters (?x ?y)
:preconditions (white-pawn(?x,?y) NOT(white-pawn(?x-1, ?y-2)) NOT(white-rook(?x-1, ?y-2)) NOT(white-knight(?x-1, ?y-2)) NOT(white-bishop(?x-1, ?y-2)) NOT(white-queen(?x-1, ?y-2)) NOT(white-king(?x-1, ?y-2)))
:effect (open(?x ?y) white-knight(?x-1, ?y-2))



%action 14
:action bishop-leftup-rightdown
:parameters (?x, ?y) (?p, ?q)
:preconditions (white-bishop(?x,?y) NOT(white-pawn(?p, ?q)) NOT(white-rook(?p, ?q)) NOT(white-knight(?p, ?q)) NOT(white-bishop(?p, ?q)) NOT(white-queen(?p, ?q)) NOT(white-king(?p, ?q)) sum(up-left down-right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) white-bishop(?p, ?q))

%action 15
:action bishop-rightup-leftdown
:parameters (?x, ?y) (?p, ?q)
:preconditions (white-bishop(?x,?y) NOT(white-pawn(?p, ?q)) NOT(white-rook(?p, ?q)) NOT(white-knight(?p, ?q)) NOT(white-bishop(?p, ?q)) NOT(white-queen(?p, ?q)) NOT(white-king(?p, ?q)) sum(down-left up-right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) white-bishop(?p, ?q))



%action 16
:action queen-leftup-rightdown
:parameters (?x, ?y) (?p, ?q)
:preconditions (white-queen(?x,?y) NOT(white-pawn(?p, ?q)) NOT(white-rook(?p, ?q)) NOT(white-knight(?p, ?q)) NOT(white-bishop(?p, ?q)) NOT(white-queen(?p, ?q)) NOT(white-king(?p, ?q)) sum(up-left down-right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) white-queen(?p, ?q))

%action 17
:action queen-rightup-leftdown
:parameters (?x, ?y) (?p, ?q)
:preconditions (white-queen(?x,?y) NOT(white-pawn(?p, ?q)) NOT(white-rook(?p, ?q)) NOT(white-knight(?p, ?q)) NOT(white-bishop(?p, ?q)) NOT(white-queen(?p, ?q)) NOT(white-king(?p, ?q)) sum(down-left up-right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) white-queen(?p, ?q))

%action 18
:action queen-move-horizontal
:parameters (?x ?y) (?p ?q)
:preconditions (white-queen(?x,?y) NOT(white-pawn(?p, ?q)) NOT(white-rook(?p, ?q)) NOT(white-knight(?p, ?q)) NOT(white-bishop(?p, ?q)) NOT(white-queen(?p, ?q)) NOT(white-king(?p, ?q)) sum(left right)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) white-queen(?q ?p)

%action 19
:action queen-move-vertical
:parameters (?x ?y) (?p ?q)
:preconditions (white-queen(?x,?y) NOT(white-pawn(?p, ?q)) NOT(white-rook(?p, ?q)) NOT(white-knight(?p, ?q)) NOT(white-bishop(?p, ?q)) NOT(white-queen(?p, ?q)) NOT(white-king(?p, ?q)) sum(up down)((?x, ?y) (?p, ?q))(open))
:effect (open(?x, ?y) white-queen(?q, ?p))




%action 20
:action king-up-right
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white-pawn(?x+1, ?y-1)) NOT(white-rook(?x+1, ?y-1)) NOT(white-knight(?x+1, ?y-1)) NOT(white-bishop(?x+1, ?y-1)) NOT(white-queen(?x+1, ?y-1)) NOT(white-king(?x+1, ?y-1)))
:effect (open(?x ?y) white-king(?x+1 ?y-1))

%action 21
:action king-up
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white-pawn(?x, ?y-1)) NOT(white-rook(?x, ?y-1)) NOT(white-knight(?x, ?y-1)) NOT(white-bishop(?x, ?y-1)) NOT(white-queen(?x, ?y-1)) NOT(white-king(?x, ?y-1)))
:effect (open(?x ?y) white-king(?x, ?y-1))

%action 22
:action king-up-left
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white-pawn(?x-1, ?y-1)) NOT(white-rook(?x-1, ?y-1)) NOT(white-knight(?x-1, ?y-1)) NOT(white-bishop(?x-1, ?y-1)) NOT(white-queen(?x-1, ?y-1)) NOT(white-king(?x-1, ?y-1)))
:effect (open(?x ?y) white-king(?x-1, ?y-1))

%action 23
:action king-left
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white-pawn(?x-1, ?y)) NOT(white-rook(?x-1, ?y)) NOT(white-knight(?x-1, ?y)) NOT(white-bishop(?x-1, ?y)) NOT(white-queen(?x-1, ?y)) NOT(white-king(?x-1, ?y)))
:effect (open(?x ?y) white-king(?x-1, ?y))

%action 24
:action king-left-down
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white-pawn(?x-1, ?y+1)) NOT(white-rook(?x-1, ?y+1)) NOT(white-knight(?x-1, ?y+1)) NOT(white-bishop(?x-1, ?y+1)) NOT(white-queen(?x-1, ?y+1)) NOT(white-king(?x-1, ?y+1)))
:effect (open(?x ?y) white-king(?x-1, ?y+1))

%action 25
:action king-down
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white-pawn(?x, ?y+1)) NOT(white-rook(?x, ?y+1)) NOT(white-knight(?x, ?y+1)) NOT(white-bishop(?x, ?y+1)) NOT(white-queen(?x, ?y+1)) NOT(white-king(?x, ?y+1)))
:effect (open(?x ?y) white-king(?x, ?y+1))

%action 26
:action king-down-right
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white-pawn(?x-1, ?y+1)) NOT(white-rook(?x-1, ?y+1)) NOT(white-knight(?x-1, ?y+1)) NOT(white-bishop(?x-1, ?y+1)) NOT(white-queen(?x-1, ?y+1)) NOT(white-king(?x-1, ?y+1)))
:effect (open(?x ?y) white-king(?x-1, ?y+1))

%action 27
:action king-right
:parameters (?x ?y)
:preconditions (white-king(?x,?y) NOT(white-pawn(?x-1, ?y)) NOT(white-rook(?x-1, ?y)) NOT(white-knight(?x-1, ?y)) NOT(white-bishop(?x-1, ?y)) NOT(white-queen(?x-1, ?y)) NOT(white-king(?x-1, ?y)))
:effect (open(?x ?y) white-king(?x-1, ?y))
