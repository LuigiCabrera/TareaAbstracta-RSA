import random
from time import time

#sys.setrecursionlimit(10**5) # Set the recursion limit in 10**6 (dedault = 1000)
random.seed(time())

def init_eratosthenes_sieve(n):
    global primes
    primes = [True for i in range(n)]
    primes[0],primes[1] = False, False # 0 and 1 not primes
    i = 2
    while i*i < n:
        if primes[i] == False:
            i+=1
            continue
        for j in range(i*i,n,i): primes[j] = False
        i+=1
    primes = [i for i in range(n) if primes[i] and i > 5] 
    # Primes candidates for p and q need to be greater than 5 (Harder factoring)
    
def random_primes():
    index1 = random.randint(0,len(primes))
    while True:
        index2 = random.randint(0,len(primes))
        if index1 != index2: return primes[index1], primes[index2]

def ext_euclid(a,b):
    if a % b == 0: return b,0,1
    r, x_, y_ = ext_euclid(b, a%b)
    x, y = y_, x_ - int(a/b)*y_
    return r,x,y

def rsa_key_generator():
    p, q = random_primes()
    n = p*q
    euler = (p-1)*(q-1) # Euler es par, por eso e = [3,n-1]

    while True:
        e = random.randint(3, n-1)
        gcd,x,y = ext_euclid(e, euler)
        if gcd == 1:
            d = x % euler
            break
    return n, e, d

def main():
    print("\n\n\t\t*** RSA KEY GENERATOR ***\n\n")
    print("Generating primes data base...\n")

     
    # (SER CUIDADOSO, no enviar un demasiado grande)
    init_eratosthenes_sieve((1<<20)) 
    # Aprox. 82 000 primos almacenados en tiempo de ejecucion.

    while True:
        a = input("Press enter to generate RSA keys (Type 0 to exit): ")
        if a != "": break
        mod, pk, sk = rsa_key_generator()
        print(f"\nPublic Key:\t{pk}\nSecret Key:\t{sk}\nMod:\t\t{mod}\n\n")
    return

main()
