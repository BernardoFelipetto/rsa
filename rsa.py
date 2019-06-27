import os
import sys
import hashlib
import math
import random
import binascii


###
# Para rodar apenas digite py -3 rsa.py no terminal
###

def generate_large_prime():
    is_prime = False
    while not is_prime:
        #gera um numero aleatório de 1024 bits
        big_number = random.getrandbits(1024)
        is_prime = fermat(big_number)
    return big_number

def fermat(x):
    #verifica se o numero é primo usando o teorema de fermat
    return pow(2, x-1, x) == 1

def calculate_cypher_key(phi_number):
    sys.setrecursionlimit(1000000)

    is_cypher = 0
    while is_cypher != 1:
        #Escolhe um numero aleatório entre 2^1000 representando os 1000 bits e phi
        cypher_key = random.randrange(pow(2,1000), phi_number)
        is_cypher, a, b = egcd(cypher_key, phi_number)
        #Verifica se o seu GCD é 1 de acordo com o algoritmo fornecido
        if(is_cypher == 1):
            return cypher_key

def calculate_decypher_key(system_module, phi_number, cypher_key):
    sys.setrecursionlimit(1000000)

    #calcula o numero inverso da cypher key
    d = modinv(cypher_key, phi_number)

    #valida se D * cypher key mod phi é igual a 1, validando que é seu inverso realmente
    is_decypher = (d * cypher_key) % phi_number
    if(is_decypher == 1):
        return d

#algoritmo extendido de euclides fornecido
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#calculo do módulo inverso
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str.encode())
    return ascii_str

if __name__ == "__main__":

    #numero P primo
    p_prime_number = generate_large_prime()
    
    #numero Q primo
    q_prime_number = generate_large_prime()

    #módulo do sistema N
    system_module = p_prime_number * q_prime_number

    #numero phi de N
    phi_number = (p_prime_number - 1) * (q_prime_number - 1)

    #chave para cifrar E
    cypher_key = calculate_cypher_key(phi_number)

    print ("Chave Pública: \nE > ", cypher_key, "\nN > ", system_module)

    #chave para decifrar D
    decypher_key = calculate_decypher_key(system_module, phi_number, cypher_key)

    print ("Chave Privada: \nD > ", decypher_key, "\nP > ", p_prime_number, "\nQ > ", q_prime_number,)

    menu_option = 0
    exit_system = False
    message = None

    while not exit_system:
        print("Digite um número")
        print("1 - Cifrar Mensagem")
        print("2 - Decifrar Mensagem")
        menu_option = int(input("0 - Encerrar Programa\n"))

        if menu_option == 1:
            message = input("Digite a mensagem\n")
            message_bytes = message.encode()

            hex_message = binascii.hexlify(message_bytes)

            int_message = int(hex_message, 16)
            cypher_text = pow(int_message, cypher_key, system_module)
            print("Texto Cifrado: ", cypher_text)

        elif menu_option == 2:
            message = int(input("Digite o texto cifrado\n"))
            decypher_int = pow(message, decypher_key, system_module)
            decypher_hex = hex(decypher_int)

            text = hex_to_ascii(decypher_hex)

            print("Texto Decifrado: ", text.decode())
        else:
            exit_system = True

    sys.exit(0)