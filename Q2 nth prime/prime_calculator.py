# Reference: Document reference ICPC 2022-2023 pour Universite de Montreal

import math
import sys
import time
def estimate_range(prime_count):
    # Initial guess for N
    N = prime_count * math.log(prime_count)

    # Refine the estimate iteratively
    for _ in range(10):  # Adjust the number of iterations as needed
        N = prime_count * math.log(N)

    return int(N)


def test_estimate_range():
    assert estimate_range(25) >= 1e2
    assert estimate_range(168) >= 1e3
    assert estimate_range(1229) >= 1e4
    assert estimate_range(9592) >= 1e5
    assert estimate_range(78498) >= 1e6
    assert estimate_range(664579) >= 1e7
    assert estimate_range(5761455) >= 1e8
    assert estimate_range(50847534) >= 1e9
    assert estimate_range(455052511) >= 1e10
    assert estimate_range(4118054813) >= 1e11
    assert estimate_range(37607912018) >= 1e12
    print('All test cases passed')
    print(f'{25}th prime number is estimated to be in the range of {estimate_range(25)}')
    print(f'{168}th prime number is estimated to be in the range of {estimate_range(168)}')
    print(f'{1229}th prime number is estimated to be in the range of {estimate_range(1229)}')
    print(f'{9592}th prime number is estimated to be in the range of {estimate_range(9592)}')
    print(f'{78498}th prime number is estimated to be in the range of {estimate_range(78498)}')
    print(f'{664579}th prime number is estimated to be in the range of {estimate_range(664579)}')
    print(f'{5761455}th prime number is estimated to be in the range of {estimate_range(5761455)}')
    print(f'{50847534}th prime number is estimated to be in the range of {estimate_range(50847534)}')
    print(f'{455052511}th prime number is estimated to be in the range of {estimate_range(455052511)}')
    print(f'{4118054813}th prime number is estimated to be in the range of {estimate_range(4118054813)}')
    print(f'{37607912018}th prime number is estimated to be in the range of {estimate_range(37607912018)}')


def erastosthene(n, id):
    P = [True]*n
    ans = [2]
    for i in range(3,n,2):
        if P[i]:
            ans.append(i)
            for j in range(2*i,n,i):
                P[j] = False

    space = sys.getsizeof(ans) + sys.getsizeof(P)
    print(f'Used {space/1e6} mb for the list of primes')
    return ans[id]


def get_nth_prime(nth):
    return erastosthene(estimate_range(nth), nth)


def test_time_get_nth_primes():
    t1 = time.perf_counter()
    erastosthene(estimate_range(20000), 20000)
    print(f'{time.perf_counter() - t1} seconds')

    t1 = time.perf_counter()
    erastosthene(estimate_range(100000), 100000)
    print(f'{time.perf_counter() - t1} seconds')

    t1 = time.perf_counter()
    erastosthene(estimate_range(1000000), 1000000)
    print(f'{time.perf_counter() - t1} seconds')


if __name__ == "__main__":
    print(get_nth_prime(1000000))