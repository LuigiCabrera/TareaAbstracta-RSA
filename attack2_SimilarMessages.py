import sys
sys.setrecursionlimit(2000)

def ext_euclid(a,b):
    if a % b == 0:
        return b,0,1
    r, x_, y_ = ext_euclid(b, a%b)
    x, y = y_, x_ - int(a/b)*y_
    return r,x,y

def BigIntPow(a,n):
    if n==0: return 1
    x = BigIntPow(a,n/2)
    x = x*x
    if n%2==1: x = x*a
    return x

def attack_SimilarMessages(e1, c1, e2, c2, n):
    gcd1, x, y = ext_euclid(e1,e2)
    gcd2, inv_c2, x2 = ext_euclid(c2,n)
    if gcd1 == 1 and gcd2 == 1:
        x = x % e2
        inv_c2 = inv_c2 % n
        if y < 0: m = (BigIntPow(c1,x) * BigIntPow(inv_c2,-y) ) % n
        else: m = (BigIntPow(c1,-x) * BigIntPow(inv_c2,y) ) % n
        return True, m
    else: return False, -1

def main():
    print("\n\n\t\t*** RSA ATTACK ***\n\n")
    while True:
        e1 = int(input("Ingrese llave publica 1 (e1): "))
        e2 = int(input("Ingrese llave publica 2 (e2): "))

        c1 = int(input("Ingrese mensaje encriptado 1 (c1): "))
        c2 = int(input("Ingrese mensaje encriptado 2 (c2): "))

        n = int(input("Ingrese modulo de encriptacion (n): "))

        r, m = attack_SimilarMessages(e1, c1, e2, c2, n)

        if r: print("Mensaje Decifrado: {m}")
        else: print("No Se ha podido decifrar el mensaje")
                
        print()

main()
