#include "exercise.h"

bool isPrime(int val) {
    //bool isPrime = true;
    if(val < 2) return false;

    for(int i = 2; i < val; ++i) {
        if(val%i == 0) {
            return false;
        }
    }

    return true;
}

void primes() {
    for(int i = 0; i <= 100; ++i) {
        if(isPrime(i))
        std::cout << i << ", ";
    }
    std::cout << std::endl;
}

void givePrimes(int first, int last) {
    if(first < last) {
       std::cout << "Primenumbers from " << first << " to " << last << std::endl;
        while(first < last) {
            if(isPrime(first))
            std::cout << first << ", ";
            first++;
        }
    } else {
        std::cout << "Primenumbers from " << last << " to " << first << std::endl;
        while(last < first) {
            if(isPrime(last))
            std::cout << last << ", ";
            last++;
        }
    }
     std::cout << std::endl;
}

void kalkshema(double menge,double preis,double rabatt,double skonto,double versandkosten) {
    double listpreis = menge*preis;
    double rabattgeld = (rabatt*listpreis)/100;
    double zielpreis = listpreis-rabattgeld;
    double skontogeld = (skonto*zielpreis)/100;
    double bareinkauf = zielpreis-skontogeld;
    std::cout << "Listenpreis:\t\t\t\t" << listpreis << " EUR" << std::endl;
    std::cout << "-Rabatt " << rabatt <<" %\t\t\t\t" << rabattgeld  << " EUR" << std::endl;
    std::cout << "= Zieleinkaufspreis\t\t\t" <<  zielpreis << " EUR" << std::endl;
    std::cout << "-Skonto " << skonto <<" %\t\t\t\t" << skontogeld  << " EUR" << std::endl;
    std::cout << "= Bareinkaufspreis\t\t\t" <<  bareinkauf << " EUR" << std::endl;
    std::cout << "+ Versandkosten\t\t\t\t" <<  versandkosten << " EUR" << std::endl;
    std::cout << "= Bezugspreis (Einstandspreis)\t\t" <<  bareinkauf + versandkosten << " EUR" << std::endl;
}
