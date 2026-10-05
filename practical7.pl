% Experiment No. 7
% Family Tree using Prolog

% Parent facts
parent(john, mary).
parent(john, david).

parent(susan, mary).
parent(susan, david).

parent(mary, alice).
parent(mary, bob).

parent(david, charlie).

% Gender facts
male(john).
male(david).
male(bob).
male(charlie).

female(susan).
female(mary).
female(alice).

% Rules

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).