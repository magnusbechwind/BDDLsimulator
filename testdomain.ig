#blackactions
%action 1
:action test
:parameters (?x, ?y)
% this works for for xmin+1 ymin+1 to xmax-1 ymax-1 aka 2-4
:precondition (open(?x+1,?y+1) open(?x-1,?y-1)) NOT(open(?x+1,?y-1))
:effect (black(?x,?y))
#whiteactions
