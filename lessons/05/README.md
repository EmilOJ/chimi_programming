# Lesson 5: Computation and Algorithms

## How fast are computers?

```python
from timeit import default_timer as timer

start = timer()

# Do something...

end = timer()

print(f"Finished in {end - start:.10f} seconds")
```

Test on your own computer:

Exercise: Asssign a value to a variable in a `while` loop. How many iterations can you set the while loop to do until you notice the time it takes?

On my computer it took 7 seconds for 100,000,000 iterations.

![](img/chess.jpg)

Possibilities in chess:

*1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*

If it takes 7 seconds to do 100,000,000 computations, to check all chess combinations it'll take

*31709791980000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 years*


For comparison, the age of the universe is: 

*13,900,000,000 years*


## How do we compute complex problems?

### Guess a number

**Naive method**
1. Is it 1?
2. Is it 2?
3. Is it 3?

How many guesses does it take *in the best/worst case* for guessing a number between 1-100?

**Best**: ?

**Worst**: ?

Generalizing: If instead of guessing a number between 1 and 100, we guess a number between 1 and N, the worst case is N, so we say, the time complexity of the naive method is:

*O(N)*

This means:

N = 100, worst case is 100 time units

N = 10000, worst case is 10000 time units

etc...

How many guesses does it take *in the worst case*?

This is called *Linear search* or *Sequential search*

![](img/sequential_search.gif)

**A better method** 

1. Look at the middle number: Is it higher or lower?
2. Repeat...

![](img/binary_search.gif)


How many guesses does it take *in the best/worst case* for guessing a number between 1-100?

**Best**: ?

**Worst**: ?

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100

**Comparison of the two**

![](img/binary-and-linear-search-animations.gif)