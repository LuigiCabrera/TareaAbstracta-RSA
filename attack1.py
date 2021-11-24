
def expomod(x, y, p):
    res = 1
    x = x % p
    if x == 0: return 0
    while y > 0:
        if (y & 1) == 1: res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def attack(e,n,c):
    # First, verify if m^e < n
    m = int(c ** (1/e))
    if int(m**e) == c: return True, m # Verifica si la raiz es exacta

    # Uncancealed messages if m^e mod n = m
    if expomod(c,e,n) == c: return True, c

    # Fuerza Bruta?
    for m_ in range(int(n**(1/e)),n):
        if expomod(m_,e,n) == c: return True,m_

    return False, -1


def main():
    print("\n\n\t\t*** RSA ATTACK ***\n\n")
    while True:
        e = int(input("Ingrese llave publica (e): "))
        n = int(input("Ingrese modulo de encriptacion (n): "))
        c = int(input("Ingrese mensaje encriptado (c): "))
        print(attack(e,n,c))
    
main()