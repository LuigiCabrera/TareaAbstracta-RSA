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
    primes = [i for i in range(n) if primes[i]] 

def expomod(x, y, p):
    res = 1
    x = x % p
    if x == 0: return 0
    while y > 0:
        if (y & 1) == 1: res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def ext_euclid(a,b):
    if a % b == 0:
        return b,0,1
    r, x_, y_ = ext_euclid(b, a%b)
    x, y = y_, x_ - int(a/b)*y_
    return r,x,y

def inverso_mult(a, n):
    d, x_, y_ = ext_euclid(a,n)
    if d == 1: return x_ % n
    else: return None

def find_factors(n):
    factors = []
    for i in range(len(primes)):
        if primes[i]*primes[i] > n: break
        if n % primes[i] == 0 and primes[i] != n: 
            factors = [int(n/primes[i]), primes[i]]
            break
    if len(factors) == 0: return False, []
    a, sub_factors1 = find_factors(factors[0])
    b, sub_factors2 = find_factors(factors[1])
    
    if b:
        del factors[1]
        factors += sub_factors2
    if a:
        del factors[0]
        factors += sub_factors1
    return True, factors

def euler(n,factors):
    r = n
    div = 1
    last = -1
    for i in range(len(factors)): 
        if last == factors[i]: continue
        r*= (factors[i]-1)
        div *= factors[i]
        last = factors[i]
    return int(r/div)

def attack(e,n,c):
    # First, verify if m^e < n
    m = int(c ** (1/e))
    if int(m**e) == c: return True, m # Verifica si la raiz es exacta

    # Uncancealed messages if m^e mod n = m
    if expomod(c,e,n) == c: return True, c

    # Brute Force
    r, factors = find_factors(n)
    if r: 
        euler_n = euler(n, factors)
        private_key = inverso_mult(e,euler_n)
        m = expomod(c, private_key, n)
        return True, m
    return False, -1


def main():

    print("\n\n\t\t*** RSA ATTACK ***\n\n")
    print("Generating primes data base...\n")
    # (SER CUIDADOSO, no enviar un numero demasiado grande)
    init_eratosthenes_sieve((1<<20)) 
    # Aprox. 82 000 primos almacenados en tiempo de ejecucion.
    
    while True:
        e = int(input("Ingrese llave publica (e): "))
        n = int(input("Ingrese modulo de encriptacion (n): "))
        c = int(input("Ingrese mensaje encriptado (c): "))
        print(attack(e,n,c))
    
main()