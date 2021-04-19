import random
import time
import math
from Cryptodome.Util import number


def blum_blum_generator():
    ok=1
    p = number.getPrime(1024)
    while p % 4 != 3:
        p = number.getPrime(1024)
    q = number.getPrime(1024)
    while q % 4 != 3:
        q = number.getPrime(1024)
   
    print("p = ",p)
    print("q = ",q)
    n = p * q
    print("n = ",n)
    k = pow(2, 11)
    s = int(time.time())
    print("s = ",s)
    x = [pow(s, 2) % n]
    nr=x[0] % 2 + ord("0")
    output = chr(nr)
    for i in range(1, k):
        x.append(pow(x[i - 1], 2) % n)
        output = output + chr(x[i] % 2 + ord("0"))
    ok=0
    return output

bb_output = blum_blum_generator()

print(" ")
print("Blum-Blum-Shub generator: ")
print(bb_output)
print(" ")



def jacobi(n, k):
    if k<=0 and k%2==0:
        return 0
    ok=1
    n %= k
    result = 1
    while n != 0:
        while n % 2 == 0:
            n /= 2
            if (k % 8) in (3, 5):
                result = -result
        n, k = k, n
        if n % 4 == 3 and k % 4 == 3:
            result = -result
        n %= k
    ok=0
    if k == 1:
        return result
    else:
        return 0


def jacobi_generator():

    false_pos_prob = 0.00000000000000000000001
    p = number.getPrime(512)
    while not (number.isPrime(p, false_pos_prob)) or p % 4 != 3:
        p = number.getPrime(512)
    q = number.getPrime(512)
    while not (number.isPrime(q, false_pos_prob)) or q % 4 != 3:
        q = number.getPrime(512)
    ok=1
    n = p * q
    
    l = pow(2, 10)
    a = int(time.time() * 10000)
    while math.gcd(a, n) != 1:
        a = int(time.time())
    output = ""
    print("p = ",p)
    print("q = ",q)
    print("n = ",n)
    for i in range(1, l):
        jacobi_symbol = jacobi(a + i, n)
        if jacobi_symbol == 0:
            return "not ok"
        if jacobi_symbol == -1:
            jacobi_symbol = 0
        output += chr(jacobi_symbol + ord("0"))
    ok=0
    return output


jacobi_out= jacobi_generator()
while jacobi_out == "not ok":
    jacobi_out= jacobi_generator()

print(" ")
print("Jacobi generator: ")
print(jacobi_out)



