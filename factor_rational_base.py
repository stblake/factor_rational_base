
# factor_rational_base is a fast algorithm for factoring semiprimes of a specific structure. 

# factor_rational_base will factor $N = p q$, where $p \approx c (a/b)^n$ with $(a/b)^n > q$ and 
# $a,b$ can be found by an exhaustive search. The algorithm does not require knowledge of 
# $c$ or $n$. 

# Sam Blake

# started 17 July, 2021

# TODOs: 
# 		- parallelise a,b search. 
#       - better search strategy for a,b (if possible). 


import math
import gmpy2
from gmpy2 import mpz, mpq, next_prime

def factor_rational_base(N, initial_base = 3, specific_base = 1, max_base = 0, return_base = False, verbose = False):
	"""GNU MP-based implementation of a fast factorisation algorithm for some semiprimes."""
    
	if type(N) is int:
		N = mpz(N)
    
	if type(N) is not mpz:
		return 1
    
	if N < 2 or gmpy2.is_prime(N):
		return 1
    
	if specific_base < 1:
		print('ERROR: specific_base should be greater than 1.')
		return 1
    
	if specific_base != 1 and specific_base != mpz(1):
		a,b = specific_base.numerator, specific_base.denominator
		return factor_candidate_base_representation(N, a, b, verbose)
    
	if type(initial_base) is int:
		initial_base = mpz(initial_base)
    
	if type(initial_base) is not mpz:
		print('ERROR: initial_base is not an integer.')
		return 1
    
	if initial_base < 3:
		printf('ERROR: initial_base should be at least 3.')
    
	j = initial_base
    
	while True:
		if verbose:
			print(j)
            
		partitions = lex_partitions(j)
        
		for b,a in partitions:
			if verbose:
				print(f'    {a}, {b}')
			fac = factor_candidate_base_representation(N, a, b, verbose)
			if fac != 1:
				if return_base:
					return (mpq(int(a),int(b)),fac)
				else:
					return fac
		j += 1
		if max_base > 0 and j > max_base:
			if verbose:
				print(f'Exiting as we reached max_base.')
			break
	return 1


# factor_rational_base(mpz(71182049442858712148942698958093))
# mpz(120398147)

# factor_rational_base(\
#    mpz(32910716859144836902319093071490228285161562532098591993504414537604089702286327911158801))
# mpz(123081930193807529345720357345999)


def factor_candidate_base_representation(N, a, b, verbose = False):
	"""Given a semiprime, $N$, and a/b candidate base representation, then factor_candidate_base_representation \
	will attempt to factor $N$ assuming $N = p q$, with $p \\approx c (a/b)^n$ and $(a/b)^n > q$."""
	q = N
	n_gcd, n_divs = 0, 0
    
	while True:
		n_divs += 1
		q, _ = gmpy2.t_divmod(gmpy2.mul(b, q), a)
		if q < 2:
			return 1
		for k in range(0, 2 + math.ceil(math.log2(n_divs))):
			n_gcd += 1
			gcd = gmpy2.gcd(q**2 - k**2, N)
			if gcd != mpz(1) and gcd != N:
				if verbose:
					print(f'k = {k}, q = {q}, n_gcd = {n_gcd}, n_divs = {n_divs}')
				return gcd
	return 1


# factor_candidate_base_representation(\
#     mpz(32910716859144836902319093071490228285161562532098591993504414537604089702286327911158801), \
#     11, 3)
# mpz(123081930193807529345720357345999)


def lex_partitions(m):
    """Given an integer, m, lex_partitions will partition $m$ into all $a,b$ such that \
    $m = a + b$ with $a < b$ and $a,b$ coprime."""
    partitions = []
    for k in range(1, m):
        if k < m - k and gmpy2.gcd(k, m - k) == 1:
            partitions.append([k, m - k])
    
    return partitions


# lex_partitions(10)
# [[1, 9], [3, 7]]

# lex_partitions(25)
#[[1, 24],[2, 23],[3, 22],[4, 21],[6, 19],[7, 18],[8, 17],[9, 16],[11, 14],[12, 13]]

