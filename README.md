### Fast integer factorisation of some semiprimes

* Given positive integers $a$ and $b$ such that $a>b$ and $\gcd(a,b)=1$, and a semiprime, $N$, we may compute a factor, $q$, of $N$ by creating the sequence $$Q_{k+1} = \left\lfloor\frac{b}{a} Q_{k}\right\rfloor,$$ where $Q_0 = N$. The sequence terminates if $Q_k < 2$, in which case the method has failed for the $a/b$-rational base representation. Otherwise, the sequence terminates when $$q = \gcd\left(\prod_{j=0}^{\lceil\log_2(k)\rceil} Q_k^2 - j^2, N \right) \neq 1,$$ in which case we have found a factor, $q$, of $N$. 
