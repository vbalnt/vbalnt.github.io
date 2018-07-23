+++
date = "2017-09-14"
draft = true
title = "Asymptotic notation"
+++

## Introduction


Consider an algorithm that naively loops through a list, and compares
each value with a predefined input provided by a user.

One might ask, `how long will this take?` In other words, how many
steps (operations) a computer needs to perform? Knowing the total
number of steps, and the time needed per step, we can infer the total
time.

It is self-evident that such an answer is dependent on several
factors, such as the speed of the processing unit, the language we use
etc. For example, the same code written in the same language executed
on a new CPU will take less time than on a 10 year-old CPU.
Thus, we instead focus on the `complexity` of algorithms, i.e. how
does the algorithm scales in terms of resources needed, in relation to
the input given. 


## Measuring the efficiency of an algorithm
Let's assume that we write a program that processes a list $L$. We
carefully measure the execution time for different cardinalities of
the list $L$, and we use a statistical method to fit a polynomial
function $f(n)$ to the measurements.

$$ f_A(n) = 10 n^2 + 100 n + 50 $$

Plugging different list sizes to $n$ will give us the total execution time
$f(n)$.

The next day, we redo the experiments on a different machine, and we
get a different polynomial approximation. 

$$ f_B(n) = 100 n^2 + 20 n + 100 $$

In addition, we ask another friend to write a program that does the
same thing, and when we profile his code on the machine $A$, we come
up with this 

$$ \ell_A(n) = n^3 + 10$$

Below we show some examples of total resources needed, for different
sizes of $n$:

| List size ($n$) | $f_A(n)$        | $f_B(n)$        | $\ell_A(n)$    |
| -------------   | :-------------: | :-----:         | :-----:        |
| 1               | 160             | 220             | 11             |
| 10              | 2050            | 10300           | 1010           |
| 1000            | $\approx 10^6$  | $\approx 10^7$ | $\approx 10^9$ |



## Bounds of functions

Since we are interested in analysing the growth-rate instead of the
absolute growth values of functions, we use bounds of functions, which
are familiar from real analysis. For a more formal discussion, there
is Knuth's letter [[^KNUTH]].


### $O(g(n))$

We say that  $$g(n) \in  O(f(n))$$ iff $\exists$ constants
$\alpha,n_0>0$ s.t. 

$$ \forall n>n_0 ,\;  |g(n)| \leq \alpha f(n) $$

### $\Omega(g(n))$

We say that  $$g(n) \in  \Omega(f(n))$$ iff $\exists$ constants
$\alpha,n_0>0$ s.t. 

$$ \forall n>n_0 ,\;  g(n) \geq \alpha f(n) $$

### $\Theta(g(n))$

We say that  $$g(n) \in  \Theta(f(n))$$ iff $\exists$ constants
$\alpha, \beta,n_0>0$ s.t. 

$$ \forall n>n_0 ,\; \alpha f(n) \leq g(n) \leq \beta f(n) $$

> Note that usually we are concerned with $O(g(n))$ since this gives an
> upper bound i.e. worst case scenario for our algorithm. 

## Some properties

- Maximum rule: $O(f(n)+g(n)) = O(max(f(n), g(n)))$
 

## When do the constants matter?
From Papadimitriou:

Dont ignore the ippotic stance against constants. Programmers, would
love to double their running time. 


[^KNUTH]: [KNUTH - BIG OMICRON AND BIG OMEGA AND BIG THETA ](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.230.8232&rep=rep1&type=pdf)
