#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

// Reference: https://t5k.org/howmany.html
// Upper bound for the nth prime number is nthPrime =< ln n + ln ln n - 1 + 1.8 ln ln n / ln n for n >= 13

int estimateUpperBound(int nthPrime)
{
    if (nthPrime <= 25)
        return 100;
    else
        return (int)(nthPrime * (log(nthPrime) + log(log(nthPrime)) - 1 + 1.8 * log(log(nthPrime)) / log(nthPrime)));
}

// Custom comparator for min heap
struct compare
{
    bool operator()(const std::pair<int, int> &a, const std::pair<int, int> &b)
    {
        return a.first > b.first;
    }
};

std::vector<int> dijkstra(int n)
{
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, compare> primes_pool;
    primes_pool.push(std::make_pair(4, 2));

    std::vector<int> primes = {2};

    for (int i = 3; i <= n; ++i)
    {
        while (primes_pool.top().first < i)
        {
            auto [multiple, prime] = primes_pool.top();
            primes_pool.pop();
            primes_pool.push(std::make_pair(multiple + prime, prime));
        }
        if (primes_pool.top().first == i)
        {
            auto [multiple, prime] = primes_pool.top();
            primes_pool.pop();
            primes_pool.push(std::make_pair(multiple + prime, prime));
        }
        else
        {
            primes.push_back(i);
            primes_pool.push(std::make_pair(i * i, i));
        }
    }

    // Calculate the space used by primes and primes_pool
    long space = sizeof(primes) + sizeof(std::vector<int>) * primes.capacity() +
                 sizeof(primes_pool) + sizeof(std::pair<int, int>) * primes_pool.size();

    std::cout << "Space: " << space / 1e6 << " MB" << std::endl;

    return primes;
}

int getNthPrime(int n)
{
    return dijkstra(estimateUpperBound(n))[n - 1];
}

int main()
{
    int testCases[4] = {10, 100, 1000, 10000};
    for (int n : testCases)
    {
        // int n = 1000; // Example value
        int primes = getNthPrime(n);
        std::cout << "estimateUpperBound(" << n << ") = " << estimateUpperBound(n) << std::endl; // "estimateUpperBound(1000) = 7919
        std::cout << "The " << n << "th prime number is " << primes << std::endl;
    }
}
