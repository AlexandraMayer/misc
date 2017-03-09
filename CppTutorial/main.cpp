#include <iostream>
#include <fstream>
#include <typeinfo>
#include "exercise.h"
#include <map>
#include <cstring>
#include <algorithm>

int h = 42;

int main() {
    /*
    std::cout << "Enter two numbers:" << std::endl;
    int v1 = 0, v2 = 0;
    std::cin >> v1 >> v2;
    std::cout << "The product of " << v1;
    std::cout << " and " << v2;
    std::cout << " is: " << v1*v2 << std::endl;
    int val0 = 50, result = 0;
    while (val0 <= 100) {
        result += val0;
        val0 ++;
    }
    std::cout << result << std::endl;
    int ex10 = 10;
    while(ex10 >= 0) {
        std::cout << ex10 << " ";
        ex10--;
    }
    std::cout << std::endl;

    std::cout << "Enter two numbers:" << std::endl;
    int v3 = 0, v4 = 0;
    std::cin >> v3 >> v4;
    std::cout << "printing numbers from ";
    if(v3 < v4) {
        std::cout << v3 << " to " << v4 << std::endl;
        while(v3 <= v4) {
            std::cout << v3 << " ";
            v3++;
        }
     } else {
        std::cout << v4 << " to " << v3 << std::endl;
        while(v4 <= v3) {
            std::cout << v4 << " ";
            v4++;
        }
    }
    std::cout << std::endl;
    int sum = 0;

    for(int i = - 100; i <= 100; i++)
        sum +=  i;

    std::cout << sum << std::endl;

    int result2 = 0;
    for (int i = 50; i <= 100; i++) {
        result2 += i;
    }
    std::cout << result2 << std::endl;

    for( int j = 10; j >= 0 ;j--) {
        std::cout << j << " ";
    }
    std::cout << std::endl;

    int currVal = 0, val = 0;
    // read first number and ensure that we have data to process
    if (std::cin >> currVal) {
        int cnt = 1;  // store the count for the current value we're processing
        while (std::cin >> val) { // read the remaining numbers
            if (val == currVal)   // if the values are the same
                ++cnt;            // add 1 to cnt
            else { // otherwise, print the count for the previous value
                std::cout << currVal << " occurs "
                          << cnt << " times" << std::endl;
                currVal = val;    // remember the new value
                cnt = 1;          // reset the counter
            }
        }  // while loop ends here
        // remember to print the count for the last value in the file
        std::cout << currVal <<  " occurs "
                  << cnt << " times" << std::endl;
    } // outermost if statement ends here

   std::ofstream myfile;
   myfile.open ("example.txt");
   myfile << "Writing this to a file.\n";
   myfile.close(); 
*/
    /*
    unsigned u = 10, u2 = 42;
    std::cout << u2 - u << std::endl;
    std::cout << u - u2 << std::endl;

    int i = 10, i2 =42;
    std::cout << i2 - i << std::endl;
    std::cout << i - i2 << std::endl;

    std::cout << i - u << std::endl;
    std::cout << u - i << std::endl;

    int month = 07;
    std::cout << month << std::endl;

    std::string s = "Who goes with F\145rgus?\012";

    std::cout << s;

    auto ex27 = 3.14e1L;
    std::cout << ex27  << std::endl;
    std::cout << typeid(ex27).name()  << std::endl;

    auto ex27b = 3.14L;
    std::cout << typeid(ex27b).name()  << std::endl;

    std::cout << "\062\t\115\n" << std::endl;

    int e = 3.14;
    std::cout << e << std::endl;

    double salary, wage = 9999.99;

    int h = 100;
    int k = h;

    std::cout << k << std::endl;

    int l = 100, sum = 0;
    for(int l = 0; l != 10; l++) {
        sum += l;
    }
    std::cout << l << " " << sum << std::endl;
    int in = 0, &r1 = in; double d = 0, &r2 = d;
    r2 = 3.14159;
    std::cout << d << std::endl;
    r2 = r1;
    std::cout << d << std::endl;
    in = r2;
    std::cout << r1 << std::endl;
    r1 = d;
    std::cout << d << std::endl;

    int ip, &ri = ip;
    ip = 5; ri = 10;
    std::cout << ip << " " << ri << std::endl;
    int *point;
    int ptr = 12;
    point = &ptr;
    std::cout << (*point) << std::endl;
    *point = 20;

    std::cout << ptr << std::endl;
    */
/*
    int i = 42;
    std::cout << i << std::endl;
    int *p1 = &i;
    std::cout << i << std::endl;
    std::cout << *p1 << std::endl;
    *p1 = *p1 * *p1;
    std::cout << i << std::endl;
    std::cout << *p1 << std::endl;
*/
    //const int buf;
    int cnt = 0;
    const int sz = cnt;
    ++cnt; //++sz;

    std::cout <<"Das hier ist ein  Hi vertikalen Tabulator \v Hello World"<< std::endl;

    std::cout << "int: " << sizeof(int) << std::endl;

    primes();

    int first;
    int last;

    std::cout << "Please Type two numbers" << std::endl;
    std::cin >> first >> last;
    givePrimes(first,last);

    /*
    double menge,preis,rabatt,skonto,versand;
    std::cout << "\nBitte Menge eingeben" << std::endl;
    std::cin >> menge;
    std::cout << "\nBitte Preis eingeben" << std::endl;
    std::cin >> preis;
    std::cout << "\nBitte Rabatt in % eingeben" << std::endl;
    std::cin >> rabatt;
    std::cout << "\nBitte skonto in % eingeben" << std::endl;
    std::cin >> skonto;
    std::cout << "\nBitte Versandkosten eingeben" << std::endl;
    std::cin >> versand;
    std::cout << std::endl;
    kalkshema(menge,preis,rabatt,skonto,versand);
*/
    int menge, preis;
    std::cout << "\nBitte Menge eingeben" << std::endl;
    std::cin >> menge;
    std::cout << "\nBitte Preis eingeben" << std::endl;
    std::cin >> preis;

    std::cout << "Gesamtpreis: ";
    if(menge > 10) {
        std::cout << ((preis)*95)/100 << " \244" << std::endl;
    } else if (menge > 50) {
        std::cout << (preis*95)/100 << " \244" << std::endl;
    } else {
        std::cout << (preis) << " \244" << std::endl;
    }

    std::string m_filename, word ,line;
    char x;
    std::map<std::string,int> words;
    /*
    std::cout << "\nBitte Name der Datei eingeben" << std::endl;
    std::cin >> m_filename;
    std::ifstream infile(m_filename);
    if(infile.fail()){
       std::cerr << "Could not open file." << std::endl;
       return 1;
    }
    int n;
    infile >>( n);
    std::cout << n;

    for(int i = 0; i <=  n; i++){
        std::getline(infile, line);
        std::cout << line << std::endl;
    }

    /*

    while(std::getline(fin,line)) {
        if(words.find(word) != words.end()) {
            (words.find(word)->second) ++;
        } else if (word.length() > 5) {
            words[word] = 1;
        }
    }
    fin.close();
    for(auto it = words.begin(); it != words.end(); ++it ) {
        std::cout << it->first << "\t\t\t" << it->second << std::endl;
    }

    */
    int i = 0;
    std::ifstream fin;
    //std::map<std::string,int> words;
    char falseChars[9];
    falseChars[0] = '.';
    falseChars[1] = ',';
    falseChars[2] = '?';
    falseChars[3] = '\'';
    falseChars[4] = '\"';
    falseChars[5] = '!';
    falseChars[6] = '(';
    falseChars[7] = ')';
    falseChars[8] = ':';

    fin.open("Sherlock.txt");
    if(!fin.is_open()) std::cerr << "Could not open file." << std::endl;
    while (fin >> word) {
        i++;
        if(word.size() > 10) {
            std::cout << h << std::endl;
            for (int i= 0; i < 9; i++) {
                word.erase(std::remove(word.begin(), word.end(), falseChars[i]),word.end());
            }
            std::cout << word << std::endl;
            if(word.size() > 4 && (words.find(word) == words.end())) {
                words[word] = 1;
            } else if (word.size() > 10) {
                words[word] += 1;
            }
        }

    }


    fin.close();
    for(auto it = words.begin(); it != words.end(); ++it ) {
        std::cout << it->first << "\t\t" << it->second << std::endl;
    }

    return 0;
}
