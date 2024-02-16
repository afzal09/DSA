# Big-Oh

## What is Big-Oh ?
#### It is a method for analyzing asymtotic runtime of algorithms depending on the given Input against Time

## Why Big-Oh is used ?
#### It is used to measure performance and efficiency of algorithms.on the given input against time

## example
let n be the size of program's input
let T(n) be the problem solving function or operation
let F(n) bs another function preferablly simple.This is not real function but simple function to convey how the algorithm run asymtotically to other function
then we say  T(n) E O(F(n)) if and only if T(n) <= c.F(n)
where c is constant and for all n~0~ <= n.

| Constant | Logarithmic | Linear | n-log-n | Quadratic | Cubic | Exponential |
|----------|-------------|--------|---------|-----------|-------|-------------|
|    1     |    log n    |    n   | n log n |    n^2    |  n^3  |     n!      |

Algorithms should run in form constant = O(1) to n-log-n = O(n log n) time

## Problem 

1. The code computes the product of a & b

```java
int product(int a, int b){
    int sum = 0;
    for(i=0;i < b;i++){
        sum += a
    }
    return sum
}
```



The runtime is O(n) in Linear Time Since the for loop iterates over the input b

2. the code computrs the square root of a number

```java
int sqrt(int n){
    for(int g=1, guess * guess <= n; g++){
        if(guess * guess == n){
            return n;
        }
        return -1;
    }
}
```

The runtime is O(√n) since the for loop iterates till guess * guess <= n
which is guess^2 = n;  guess = √n