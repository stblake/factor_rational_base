### Fast factorisation of some semiprimes

The algorithm implemented here, `factor_rational_base`, will factor semiprimes, $N = p q$ when $p \gg q$, $p = c (a/b)^n + \Delta$, where $c,n$ are integer constants, $a,b$ are sufficiently small to be found by an exhaustive search and $\Delta < (a/b)^n/q$. 


* Given positive integers $a$ and $b$ such that $a>b$ and $\gcd(a,b)=1$, and a semiprime, $N$, we may compute a factor, $q$, of $N$ by creating the sequence $$Q_{k+1} = \left\lfloor\frac{b}{a} Q_{k}\right\rfloor,$$ where $Q_0 = N$. The sequence terminates if $Q_k < 2$, in which case the method has failed for the $a/b$-rational base representation. Otherwise, the sequence terminates when $$q = \gcd\left(\prod_{j=0}^{\lceil\log_2(k)\rceil} Q_k^2 - j^2, N \right) \neq 1,$$ in which case we have found a factor, $q$, of $N$. 

* `factor_rational_base` exhaustively tests each possible $a/b$-rational base representation of $p$ in lexicographic order. That is, $a/b=2,3,4,3/2,5,6,5/2,4/3,7,5/3,\cdots$

* Much like other existing algorithms for integer factorisation, it is exceedingly unlikely that `factor_rational_base` will quickly factor an arbitrary, large semiprime.

* `factor_rational_base` cannot quickly factor any semiprimes from the RSA Factoring Challenge.


### Example

In the following example we construct the semiprime $N = pq$, where $p \approx (13/3)^128$ and factor $N$ using `factor_rational_base`: 


```
import math
import random
import gmpy2
from gmpy2 import mpz, mpq, next_prime
from factor_rational_base import factor_rational_base


q = next_prime(random.randint(10**31, 10**32))
p = next_prime(int(mpq(13,3)**128) + 123456879487639485857923456789)
print(p, q)
N = p*q
print(N)

3260081754204342696614851730588737100566813075532442238801303354056997440025572973 45131317303089645649402477791361
147131784083009296687436354719243871894564758968612490088337521714811692655848217307415504613330168146531574486253

%time factor_rational_base(N, verbose = True)

3
    2, 1
4
    3, 1
5
    4, 1
    3, 2
6
    5, 1
7
    6, 1
    5, 2
    4, 3
8
    7, 1
    5, 3
9
    8, 1
    7, 2
    5, 4
10
    9, 1
    7, 3
11
    10, 1
    9, 2
    8, 3
    7, 4
    6, 5
12
    11, 1
    7, 5
13
    12, 1
    11, 2
    10, 3
    9, 4
    8, 5
    7, 6
14
    13, 1
    11, 3
    9, 5
15
    14, 1
    13, 2
    11, 4
    8, 7
16
    15, 1
    13, 3
k = 1, q = 45131317303089645649402477791360, n_gcd = 1018, n_divs = 128
CPU times: user 346 ms, sys: 5.5 ms, total: 352 ms
Wall time: 352 ms
mpz(45131317303089645649402477791361)

```
