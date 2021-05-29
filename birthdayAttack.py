import hashlib
import random
import matplotlib.pyplot as plt
import numpy as np

sha256 = hashlib.sha256()
input_size = 10
number_of_trys = 40

def getDbitHAsh(string,d):
    global sha256
    sha256.update(bytes(string, encoding='utf8'))
    hexHash=sha256.hexdigest()
    return bin(int(hexHash,16))[2:][:d]

def generateRandomString(d):
    charString = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([random.choice(charString) for i in range(d)])

def fun(d):
    global input_size
    totalBits = 0
    data = {}
    first = generateRandomString(input_size)
    hashCode = getDbitHAsh(first,d)
    data[hashCode] = first
    totalBits += d
    counter = 1
    while True:
        totalBits += d
        counter += 1
        first = generateRandomString(input_size)
        hashCode = getDbitHAsh(first,d)
        if hashCode in data.keys() and data[hashCode] != first:
            return data[hashCode], first, hashCode,totalBits, counter*(counter-1)
        data[hashCode] = first

print("Hash Bits, string1, string2, hashCode, Largest Memory in Bits, comparission")    
for d in range(1, 25):
    print(d, "     ", fun(d))

# uncomment to generate plots

'''
m_avg = []
n_avg = []
for d in range(1,25):
    mavg = navg = 0
    for tt in range(number_of_trys):
        s1,s2,h,m,t = fun(d)
        mavg += m
        navg += t
    m_avg.append(mavg/number_of_trys)
    n_avg.append(navg/number_of_trys)

bits = np.array(np.arange(1,25))
m_avg = np.array(m_avg)
n_avg = np.array(n_avg)


plt.plot(bits,n_avg, marker = '.')
plt.title("Plot-1 d vs n_avg")
plt.xlabel("bits in hash code")
plt.ylabel("avg comparission")
plt.show()


plt.plot(bits,m_avg, marker = 'o')
plt.title("Plot-2 d vs m_avg")
plt.xlabel("bits in hash code")
plt.ylabel("avg memory in bits")
plt.show()
'''