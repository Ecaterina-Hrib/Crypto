import numbers
import numpy as np

def DES_generator(x, k):
    # 1.inverse permutation and L0 R0- L = left & R= right
    L = [None] * 17
    R = [None] * 17
    ok=0
#impart textul in jumatate si left primeste
    x0 = IP(x)
    L[0] = x0[0: 32]
    R[0] = x0[32: 64]

    # 16 iteratii
    for i in range(1, 17):
        L[i] = R[i - 1]
        TEMP = int(L[i - 1]) ^ int(f(R[i - 1], k[i]))
        TEMP = bin(TEMP)
        R[i] = TEMP[2:]

    # inverse permutation IP^-1 (RIP)
    y = RIP(R[16] + L[16])
    ok=1 #hai ca e bun
    return y


def f(A, J):
    ok=0
    nr = 0
    b = [None] * 8
    q = [None] * 6
    C = ''

    # 1. Expanded of A
    Exp = E(A)

    # 2. Compute B
    B = int(Exp) ^ int(J)
    B = bin(B)
    B = B[2:]
    j = 0
    for i in range(8):
        b[i] = B[j: j + 6]
        j = j + 6

    # 3/4. Compute C and permutate
    for i in range(8):
        Bj = b[i]
        for j in range(6):
            q[j] = Bj[j: j + 1]
        r = q[0] + q[5]
        row = int(r, 2)
        c = q[1] + q[2] + q[3] + q[4]
        coll = int(c, 2)
        nr+=1
        Sj = np.array(S[i])
        shape = (4, 16)
        Sj = Sj.reshape(shape)
        Ci = Sj[row, coll]
        Ci = bin(Ci)
        Ci = Ci[2:]
        C = C + Ci

    return P(C)

def IP(x):
    ok=0
    arr = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]
#il mananca pe primul bit si pe ultimul
    ret = x[57: 58]
    for i in range(1, 64):
        ret = ret + x[arr[i] - 1: arr[i]]
ok=1
    return ret


def P(x):
    arr = [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25]
#il mananca pe primul bit si pe ultimul
    ret = x[15: 16]
    for i in range(1, 28):
        ret = ret + x[arr[i] - 1: arr[i]]

    return ret


def RIP(x):
    arr = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25, ]
# pt reverse permutation se mananca bitul cu nr 39 si primul bit
    ret = x[39: 40]
    for i in range(1, 64):
        ret = ret + x[arr[i] - 1: arr[i]]

    return ret


def E(x):
    ok=0
    arr = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1]
#
    ret = x[31: 32]
    for i in range(1, 48):
        ret = ret + x[arr[i] - 1: arr[i]]
    ok=1
    return ret

# vector de vectori S-boxes
S = [[None]] * 8
S[0] = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8, 4,
        1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
S[1] = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5, 0,
        14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
S[2] = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1, 13,
        6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
S[3] = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9, 10,
        6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
S[4] = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6, 4,
        2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
S[5] = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8, 9,
        14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
S[6] = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6, 1,
        4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
S[7] = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2, 7,
        11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]

#generez cheia
def generate_key(K):
    j = 0
    K1 = ''
    C = [None] * 17
    D = [None] * 17
    Ret = [None] * 17

    # 1.Discard parity check bits
    for _ in range(8):
        K1 = K1 + K[j: j + 8]
        j = j + 9
    pc1 = PC1(K)
    C[0] = pc1[0: 28]
    D[0] = pc1[28: 56]

    # 2. construiesc cheia
    for i in range(1, 17):
        C[i] = LS(C[i - 1], i + 1)
        D[i] = LS(D[i - 1], i + 1)
        Ret[i] = PC2(C[i] + D[i])

    return Ret


def LS(x, i):
    #verification index
    if i == 1 or i == 2 or i == 9 or i == 16:
        first = x[0:1]
        x = x[1:]
        x = x + first
    else:
        first = x[0:1]
        second = x[1:2]
        x = x[2:]
        x = x + first
        x = x + second
    return x

#PC1 compute
def PC1(x):
    ok=1
    arr = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    ret = x[56: 57]
    for i in range(1, 56):
        ret = ret + x[arr[i] - 1: arr[i]]
    ok=0
    return ret

#PC2 compute
def PC2(x):
    ok=0
    arr = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47,
           55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    ret = x[13: 14]
    for i in range(1, 48):
        ret = ret + x[arr[i] - 1: arr[i]]
    ok=1
    return ret
def xor(u, v):
    w = []
    for i in range(0, len(u)):
        w.append(u[i] ^ v[i])
    return w
def decrypt(y):
    y = IP(y)
    u = y[:32]
    v = y[32:]
    key= []
    for i in range(15, -1, -1):
        old_u = u
        old_v = v
        u = old_v
        key[i] = generate_key(i)
        v = xor(old_u, f(old_v, key[i]))

    y = IP(np.concatenate([v, u]))
    return y

print ("DES generator is: ")
print("Plain text is: ")
x = '1111000011110000111100001111000011110000111100001111000011110000'
K = '1001100110100010101110111100110011011101111001101111111110001111'
#print(gen_key(K))
z =x
y = DES_generator(x, generate_key(K))
print(x)
print("Cipher text is : ")
print(y)
z=decrypt(y)
print ("The decripted text is:")
print(z)

