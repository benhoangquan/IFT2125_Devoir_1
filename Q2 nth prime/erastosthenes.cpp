// C++ program to the nth prime number

#include <vector>
#include <cmath>
#include <iostream>
using namespace std;

// initializing the max value
int estimateUpperBound(int nthPrime)
{
    if (nthPrime <= 25)
        return 100;
    else
        return (int)(nthPrime * (log(nthPrime) + log(log(nthPrime)) - 1 + 1.8 * log(log(nthPrime)) / log(nthPrime)));
}

// Function to generate N prime numbers using
// Sieve of Eratosthenes
void SieveOfEratosthenes(vector<int> &primes, int upperBound)
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

int getNthPrime(int n)
{
    int upperBound = estimateUpperBound(n);
    vector<int> primes;
    SieveOfEratosthenes(primes, upperBound);
    return primes[n - 1];
}

// Driver Code
int main()
{
    // To store all prime numbers
    int testArray[5] = {1, 3, 260, 1000, 10000};
    for (int i = 0; i < 5; i++)
    {
        cout << "The " << testArray[i] << "th prime number is " << getNthPrime(testArray[i]) << endl;
    }

    return 0;
}
