import os
import sys
import hashlib
import math
import random
from decimal import Decimal


def generate_large_prime():
    is_prime = False
    while not is_prime:
        big_number = random.getrandbits(1024)
        is_prime = fermat(big_number)
    return big_number

def fermat(x):
    return pow(2, x-1, x) == 1

def calculate_cypher_key(relative_prime_number):
    #escolher um numero aleatorio maior q 1 e menor q relative_prime_number
    #calcular o computeGCD dele
    #se for igual a 1 retorna o numero calculado
    sys.setrecursionlimit(1000000)

    is_cypher = 0
    while is_cypher != 1:
        cypher_key = random.randrange(pow(2,1000), relative_prime_number)
        is_cypher, a, b = computeGCD(cypher_key, relative_prime_number)
        if(is_cypher == 1):
            return cypher_key


    #for x in range(pow(2, 1000), relative_prime_number):
    #    is_cypher, a, b = computeGCD(x, relative_prime_number)
    #    if(is_cypher == 1):
    #        return x

    #while not is_cypher:
    #    cypher_key = random.randrange(2, relative_prime_number)
    #    is_cypher = computeGCD(cypher_key, relative_prime_number)
    #return cypher_key

def calculate_decypher_key(module, relative_prime_number, cypher_key):

    sys.setrecursionlimit(1000000)

    #(this-1 mod m).
    #e.modInverse(euler);
    #cypherkey elevado na menos 1 mod module

    # d = e.modInverse(euler);

    d = modinv(cypher_key, relative_prime_number)

    is_decypher = (d * cypher_key) % relative_prime_number
    if(is_decypher == 1):
        return d



    #while not is_decypher:
    #    decypher_key = random.randrange(0, module)
    #    is_decypher = (cypher_key * decypher_key) % relative_prime_number  == 1
    #return decypher_key

#def computeGCD(x, y): 
#   while(y): 
#       x, y = y, x % y
#   return x == 1


def computeGCD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = computeGCD(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = computeGCD(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m




if __name__ == "__main__":

    message = 9

    
    p_prime_number = generate_large_prime()
    print("Prime number P: ", p_prime_number)
    
    q_prime_number = generate_large_prime()
    print("Prime number Q: ", q_prime_number)

    module = p_prime_number * q_prime_number #N

    relative_prime_number = (p_prime_number - 1) * (q_prime_number - 1) #ROLA DE N
    print("Relative Primes: ", relative_prime_number)

    cypher_key = calculate_cypher_key(relative_prime_number)#E


    decypher_key = calculate_decypher_key(module, relative_prime_number, cypher_key)#D

    print("Public Key: ", cypher_key, " and ", module)

    cypher_text = pow(message, cypher_key, module)

    print("Cypher Text: ", cypher_text)

    decypher_text = pow(cypher_text, decypher_key, module)

    print("Decypher Text", decypher_text)


# 1 - calcula 2 numeros primos grandes: p e q
# 2 - multiplica eles
# 3 - calcula numeros que são primos relativos = (p-1) * (q-1)
# 4 - escolher um numero maior q 1 dentro do universo de numeros acima que seja relativamente primo ao numero calculado (mdc(gcd em ingles) = 1)
# 5 - achar o numero inverso do que tu calculou ali em cima no módulo de primos relativos

#chave publica {passso4, passo2}
#chave privada {passo5, p do passo1, q do passo2}

# para cifrar faz mensagem elevado no passo4 mod passo2
# decifrar faz mensagem cifrada elevado no passo5 mod passo2












