### Fast factorisation of some semiprimes

The algorithm implemented here, `factor_rational_base`, will factor semiprimes, $N = p q$ when $p \gg q$, $p = c (a/b)^n + \Delta$, where $c,n$ are integer constants, $a,b$ are sufficiently small to be found by an exhaustive search and $\Delta < (a/b)^n/q$. 


* Given positive integers $a$ and $b$ such that $a>b$ and $\gcd(a,b)=1$, and a semiprime, $N$, we may compute a factor, $q$, of $N$ by creating the sequence $$Q_{k+1} = \left\lfloor\frac{b}{a} Q_{k}\right\rfloor,$$ where $Q_0 = N$. The sequence terminates if $Q_k < 2$, in which case the method has failed for the $a/b$-rational base representation. Otherwise, the sequence terminates when $$q = \gcd\left(\prod_{j=0}^{\lceil\log_2(k)\rceil} Q_k^2 - j^2, N \right) \neq 1,$$ in which case we have found a factor, $q$, of $N$. 

* `factor_rational_base` exhaustively tests each possible $a/b$-rational base representation of $p$ in lexicographic order. That is, $a/b=2,3,4,3/2,5,6,5/2,4/3,7,5/3,\cdots$

* Much like other existing algorithms for integer factorisation, it is exceedingly unlikely that `factor_rational_base` will quickly factor an arbitrary, large semiprime.

* `factor_rational_base` cannot quickly factor any semiprimes from the RSA Factoring Challenge.
