% Experiment No. 8
% Tower of Hanoi using Prolog

hanoi(1, Source, Destination, _) :-
    write('Move disk 1 from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl.

hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    M is N - 1,

    hanoi(M, Source, Auxiliary, Destination),

    write('Move disk '),
    write(N),
    write(' from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl,

    hanoi(M, Auxiliary, Destination, Source).
    //?- hanoi(3, source, destination, auxiliary).