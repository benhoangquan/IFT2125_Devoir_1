// Hoang Quan Tran, 20249088
// Richard Gu, 20211389

#include "PrimeCalculator.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;

// ce fichier contient les definitions des methodes de la classe PrimeCalculator
// this file contains the definitions of the methods of the PrimeCalculator class

// Reference: https://t5k.org/howmany.html
// Upper bound for the nth prime number is nthPrime <= ln n + ln ln n - 1 + 1.8 ln ln n / ln n for n >= 13

PrimeCalculator::PrimeCalculator() {}

int PrimeCalculator::estimateUpperBound(int nthPrime)
{
    if (nthPrime <= 25)
        return 100;
    else
        return (int)(nthPrime * (log(nthPrime) + log(log(nthPrime)) - 1 + 1.8 * log(log(nthPrime)) / log(nthPrime)));
}

// Reference: https://www.geeksforgeeks.org/program-to-find-the-nth-prime-number/
void PrimeCalculator::SieveOfEratosthenes(vector<int> &primes, int upperBound)
{
    // Create a boolean array "IsPrime[0..MAX_SIZE]" and
    // initialize all entries it as true. A value in
    // IsPrime[i] will finally be false if i is
    // Not a IsPrime, else true.
    bool IsPrime[upperBound];
    memset(IsPrime, true, sizeof(IsPrime));

    for (int p = 2; p * p < upperBound; p++)
    {
        // If IsPrime[p] is not changed, then it is a prime
        if (IsPrime[p] == true)
        {
            // Update all multiples of p greater than or
            // equal to the square of it
            // numbers which are multiple of p and are
            // less than p^2 are already been marked.
            for (int i = p * p; i < upperBound; i += p)
                IsPrime[i] = false;
        }
    }

    // Store all prime numbers
    for (int p = 2; p < upperBound; p++)
        if (IsPrime[p])
            primes.push_back(p);
}

int PrimeCalculator::CalculateNthPrime(int n)
{
    int upperBound = estimateUpperBound(n);
    vector<int> primes;
    SieveOfEratosthenes(primes, upperBound);
    return primes[n - 1];
}