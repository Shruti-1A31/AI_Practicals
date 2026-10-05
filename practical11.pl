% Experiment No. 11
% Travelling Salesperson Problem using Prolog

% Distances between cities

distance(a, b, 10).
distance(a, c, 15).
distance(a, d, 20).

distance(b, a, 10).
distance(b, c, 35).
distance(b, d, 25).

distance(c, a, 15).
distance(c, b, 35).
distance(c, d, 30).

distance(d, a, 20).
distance(d, b, 25).
distance(d, c, 30).


% Calculate total cost

path_cost([_], 0).

path_cost([A,B|Rest], Cost) :-
    distance(A, B, D),
    path_cost([B|Rest], Remaining),
    Cost is D + Remaining.


% TSP solution

tsp(Start, Route, Cost) :-
    findall(City, city(City), Cities),
    delete(Cities, Start, Remaining),
    permutation(Remaining, Permuted),

    append([Start|Permuted], [Start], Route),

    path_cost(Route, Cost).


city(a).
city(b).
city(c).
city(d).


% Find minimum route

best_tsp(Start, BestRoute, MinCost) :-
    findall(
        Cost-Route,
        tsp(Start, Route, Cost),
        Solutions
    ),

    keysort(Solutions, Sorted),
    Sorted = [MinCost-BestRoute|_].
    //?- best_tsp(a, Route, Cost).