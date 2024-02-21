// Hoang Quan Tran, 20249088
// Richard Gu, 20211389

// ce fichier contient les declarations des methodes de la classe PrimeCalculator
// peut être modifié si vous voulez ajouter d'autres méthodes à la classe
// this file contains the declarations of the methods of the PrimeCalculator class
// can be modified if you wish to add other methods to the class
#include <vector>

class PrimeCalculator
{
public:
    PrimeCalculator();
    int estimateUpperBound(int nthPrime);
    void SieveOfEratosthenes(std::vector<int> &primes, int upperBound);
    int CalculateNthPrime(int n);
};