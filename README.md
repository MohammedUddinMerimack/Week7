# Week7
Week 7 Project takes an existing code (finPrimes) provided by Professor Gautham Krishnamurthy and modifies the code to be more efficient. 
Generates prime numbers between 2 and 5000 and prints the first 10 prime numbers

Code Revision - 1.0.0 (Initial Release)
Audience - Public
 


Code Revision  - 1.1.0
Audience - Public. 
The "isPrime" function has been modified to be more efficient. All other functions remain the same.

What Changed -
The "isPrime" function was replaced with a more efficient version. The original version of the function “isPrime” relied on bruteforce to determine if a value is indeed prime. It used a nested loop which iterates through all pairs of i and j returning “False” if any pair multiplies to “x” and “True” when a prime is found. This makes it time consuming for very large numbers. A simpler and more efficient way would be to determine if a value is prime, is to simply check if the value is divisible by the square root of “x”. We can then improve this even further by modifying the code to only check for odd values of “x” with exception for 2. The only even number that needs to be checked is 2. 2 needs to remain so we can make sure the value is divisible by even numbers. All even numbers are divisible by 2 so we can skip checking if a value is divisible by other even numbers such as 4, 6 etc. This will help to reduce the time complexity from O(n^2) to just O(√n). 

Known Issues - None 


Requirements 
Python 3.12.0 or higher

To Run
Double click on the program or open in your desired IDE

