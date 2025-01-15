# Finite-automaton-processor
Processor of finite automaton, both ***deterministic*** and ***non-deterministic***

Python program of less than 100 lines to which you pass as arguments a file with the description of the automaton and the string to process.

## Execution example
```
> finite-automaton-processor.py description1.txt 0011
```
Out:
```
Initial state: ['A']
Entry: 0 --> New state: ['B']
Entry: 0 --> New state: ['A']
Entry: 1 --> New state: ['D']
Entry: 1 --> New state: ['A']
A --> ACCEPTED

Press ENTER to exit
```

## File format
```
state1 state2 …
finalState1 finalState2 …
symbol1 symbol2 …
--TRANSITION TABLE--
AS MANY ROWS AS THERE ARE STATES
AS MANY COLUMNS AS THERE ARE SYMBOLS IN THE ALPHABET + 1 (empty string).
Each column ends with the symbol #
```

Example:
```
A B C D
A
0 1
--TRANSITION TABLE--
B # D # #
A # C # #
D # B # #
C # A # #
```

In the folder *Examples* there are some examples of automaton descriptions.
