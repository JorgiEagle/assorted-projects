## Mathematics

The total number of all possible rolls are as follows.
We can have any number of dice between 1 and 6.
Of each of those dice, each side, 1-6, has an equal chance of being shown.

Two key aspects to bear in mind:
1. Choices are with replacement. If we roll a 1, we can roll 1 again.
2. As all the dice are rolled together, order does not matter. As such we are concerned with **combinations**, not permutations

The formula for combinations with replacement is: $n+r-1 \choose r$

| Parameter | Meaning | Our Context |
| --- | --- | --- |
| n | Number of options to choose from | Sides of the dice, 6 |
| r | Number of items to choose | Number of dice |


Hence, the total number of possible dice rolls for a given number of dice, **r**, is: $5+r \choose r$

The overall total number of possible dice rolls for all numbers of dice, between 1 and 6 is:

$\displaystyle\sum_{r=1}^{6} {5+r \choose r} = 923$

### Winning Rolls

Winning rolls are not easily mathematically obtainable, and so the number of winning rolls is achieved through counting. This is practical for relatively small values of r.

