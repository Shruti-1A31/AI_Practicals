% Experiment No. 10
% 8-Puzzle Problem using Prolog

% Goal state
goal([1,2,3,4,5,6,7,8,0]).


% Legal moves of blank space

move([0,B,C,D,E,F,G,H,I],
     [B,0,C,D,E,F,G,H,I]).

move([A,0,C,D,E,F,G,H,I],
     [0,A,C,D,E,F,G,H,I]).

move([A,B,0,D,E,F,G,H,I],
     [A,B,F,D,E,0,G,H,I]).

move([A,B,C,0,E,F,G,H,I],
     [A,B,C,E,0,F,G,H,I]).

move([A,B,C,D,0,F,G,H,I],
     [A,B,C,D,E,0,G,H,I]).

move([A,B,C,D,E,0,G,H,I],
     [A,B,C,D,0,F,G,H,I]).

move([A,B,C,D,E,F,0,H,I],
     [A,B,C,D,E,F,H,0,I]).

move([A,B,C,D,E,F,G,0,I],
     [A,B,C,D,E,F,0,G,I]).

move([A,B,C,D,E,F,G,H,0],
     [A,B,C,D,E,F,G,0,H]).


% Breadth-first search

solve(Start, Path) :-
    bfs([[Start]], [], RevPath),
    reverse(RevPath, Path).


bfs([[State|Path]|_], _, [State|Path]) :-
    goal(State).

bfs([[State|Path]|Rest], Visited, Solution) :-
    findall(
        [Next,State|Path],
        (
            move(State, Next),
            \+ member(Next, Visited),
            \+ member(Next, [State|Path])
        ),
        NewPaths
    ),

    append(Rest, NewPaths, Queue),

    bfs(Queue, [State|Visited], Solution).
    //?- solve([1,2,3,4,0,6,7,5,8], Path).