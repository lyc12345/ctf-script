## Parse Data 
* tcpflow -f surveillance.pcap  
* python parse.py > output
* sage solve.sage

## Solution

* 39 equations but 40 variables
* P(modulus) is 134-bit, but key is 128-bit
* use LLL to solve biased modular linear equations
* reference: <https://crypto.stackexchange.com/questions/44644/how-does-the-biased-k-attack-on-ecdsa-work?fbclid=IwAR3LJgQiMFfgy9_vtIvKqI8RLtsjZThJ1zDu8Mf7JkECcK91rmkDNNVZGGU">
