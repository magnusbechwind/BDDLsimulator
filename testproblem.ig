#boardsize
5 5
#init
black(1,6) black(2,6) black(3,6) black(1,5) black(2,5) black(3,5) white(1,1) white(2,1) white(3,1) white(1,2) white(2,2) white(3,2)
#depth
3
#blackgoal
black(?x,?y) black(?x+1,?y)
black(?x,?y) black(?x,?y+1)
black(?x,?y) black(?x+1,?y+1)
black(?x,?y) black(?x+1,?y-1)
#whitegoal
white(?x,?y) white(?x+1,?y)
white(?x,?y) white(?x,?y+1)
white(?x,?y) white(?x+1,?y+1)
white(?x,?y) white(?x+1,?y-1)
