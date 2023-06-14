# An In-Depth Look at Advanced Attacks on Asymmetric Cryptosystem
### Purpose

- This project aim to provide to you a deep look into asymmetric cryptosystem : how does it works, its weaknesses and how dangerous it is when we don't implement it correctly . This project will focus on 3 main asymmetric cryptosystem : RSA, ECC  and lattice-based cryptography.

### Scenario
- Asymmetric ciphers are used to transfer shared-key (reason for this is because most of asymmetric ciphers are time-consuming as it costs a lot to compute and transfer ciphertext)
- Asymmetric ciphers, DSA can be used to sign, protect the interity of contracts.
- Asymmetric ciphers are used widely and its application can be found everywhere.
- Weak implementation or misuse could lead to secret key reveal, or decryption of ciphertext without secret key, even forged signature on fake contracts.

### Goal
- An overview of the current state of security provided by asymmetric cryptography in protecting information.
- Deeper understanding of the vulnerabilities of asymmetric cryptography and how attackers can exploit them.
- Providing the most common methods for attacking asymmetric cryptography.
- Developing some demos how an attacker can exploit a vulnerability in asymmetric cryptography.
- Promoting awareness and understanding of the importance of secure encryption practices.

### Configuration
- Operating system : Windows 11 Home single Language 64 bit
- Processor : 11th Gen Intel(R) Core(TM) i7 - 11800H @ 2.30Ghz (16CPUs)
- GPU : NVIDIA GeForce RTX 3050 Laptop GPU
- Memory : 8Gb

### Reference

-   https://wstein.org/edu/2010/414/projects/chu.pdf - How big can RSA be factored.
-   https://www.iacr.org/archive/pkc2004/29470001/29470001.pdf - A generalization of Wiener Attack
-   https://crypto.stanford.edu/~dabo/pubs/papers/RSA-survey.pdf - Twenty years of attack on RSA cryptosystem
-   https://www.ijireeice.com/upload/2015/april-15/IJIREEICE%2028.pdf - Attack on ECDLP
-   https://wstein.org/edu/2010/414/projects/novotney.pdf - Smart attack on Weak elliptic curve
-   https://eprint.iacr.org/2009/537.pdf - Cryptanalysis of two knapsack public-key cryptosystem
-   https://eprint.iacr.org/2016/215.pdf - Approximate GCD problem

And bunch of papers, articles that i cannot list here as it has a lot :v


### Contributor

| Fullname | ID | Github |
| --- | --- | --- |
| Dinh Thanh Phat | 21520083 | [Sinkthemall](https://github.com/sinkthemall) |
| Tran Nguyen Huy | 21520937 | [Sm1leisnotbad](https://github.com/sm1leisnotbad) |

### Usage

To use the project, please run these command below in your terminal:
```
git clone https://github.com/sinkthemall/Do-an-mat-ma-hoc.git
cd ./Do-an-mat-ma-hoc
./setup.sh
```

To the setup environment, you can just run the ```setup.sh``` file to automate all setup tasks. Or if you want to install individual component, then below is the list you need to install, setup:
-   sagemath
-   python
-   ncat
-   some neccessary modules for python:
    -   primefac
    -   sympy
    -   numpy
    -   gmpy2
    -   pwntools
    -   pycryptodome