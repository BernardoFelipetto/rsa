import os
import sys
import hashlib
import math
import random

def generate_large_prime():
    is_prime = False
    while not is_prime:
        big_number = random.getrandbits(1024)
        is_prime = fermat(big_number)
    return big_number

def fermat(x):
    return pow(2, x-1, x) == 1

if __name__ == "__main__":
    p_prime_number = generate_large_prime()
    q_prime_number = generate_large_prime()

    print(prime_number)




# 1 - calcula 2 numeros primos grandes: p e q
# 2 - multiplica eles
# 3 - calcula numeros que são primos relativos = (p-1) * (q-1)
# 4 - escolher um numero maior q 1 dentro do universo de numeros acima que seja relativamente primo ao numero calculado (mdc(gcd em ingles) = 1)
# 5 - achar o numero inverso do que tu calculou ali em cima no módulo de primos relativos

#chave publica {passso4, passo2}
#chave privada {passo5, p do passo1, q do passo2}

# para cifrar faz mensagem elevado no passo4 mod passo2
# decifrar faz mensagem cifrada elevado no passo5 mod passo2












