% Experiment No. 9
% N-Queens Problem using Prolog

nqueens(N, Solution) :-
    numlist(1, N, Columns),
    permutation(Columns, Solution),
    safe(Solution).


safe([]).

safe([Queen | Queens]) :-
    no_attack(Queen, Queens, 1),
    safe(Queens).


no_attack(_, [], _).

no_attack(Queen, [NextQueen | Queens], Distance) :-
    Queen =\= NextQueen,
    abs(Queen - NextQueen) =\= Distance,

    NextDistance is Distance + 1,

    no_attack(Queen, Queens, NextDistance).
    //?- nqueens(4, Solution).