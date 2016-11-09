#!/usr/local/bin/python3

import math, random
from fractions import gcd

def randprime():
  prime_list = create_prime_list()

  # smaller prime numbers take less time
  # uncomment next line for pure implementation
  return prime_list[random.randint(len(prime_list)//50,len(prime_list)//25)]
  # return prime_list[random.randint(0,len(prime_list))]

def create_prime_list():
  prime_list = []
  for i in range(2, 65536):
    if is_prime(i):
      prime_list.append(i)
  return prime_list

def is_prime(n):
    if n % 2 == 0 and n > 2:  return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def pow2(r, n):
  for i in range(r):
    p = 1
    for j in range(n):
      p *= i

def keygen(name):
  Z = {}

  p = randprime()
  q = randprime()

  print("%s's keys:" % name)
  print("p = %s" % p)
  print("q = %s" % q)

  m = (p-1) * (q-1)
  print("m = %s" % m)

  n = p * q
  print("n = %s" % n)

  e = random.randrange(1, m)
  g = gcd(e, m)
  while g != 1:
      e = random.randrange(1, m)
      g = gcd(e, m)

  print("e = %s" % e)

  d = -1
  for k in range(0,9999999999):
    if (k * e) % m == 1:
      d = k
      print("d = %s" % d)
      break

  Z['name'] = name
  Z['p'] = p
  Z['q'] = q
  Z['m'] = m
  Z['n'] = n
  Z['e'] = e
  Z['d'] = d
  Z['public_key'] = (e, n)
  Z['private_key'] = (d, n)

  return Z

def sign(x, private_key):
  d, n = private_key
  print("Signing x")
  s = pow(x, d) % n
  print("s = %s" % s)
  return s

def encrypt(x, public_key):
  e, n = public_key
  print("Encrypting x")
  y = pow(x, e) % n
  print("y = %s" % y)
  return y

def decrypt(y, private_key):
  d, n = private_key
  dy = pow(y, d) % n
  print("Decrypted y (x) = %s" % dy)
  return dy

def sig_verify(s, public_key):
  e, n = public_key
  sv = pow(s, e) % n
  print("Signature verification (x) = %s" % sv)
  return sv

def main():
  try:
    x = int(input('Enter plaintext integer: '))
    if (x < 10000 or x > 60000): raise StandardError
  except:
    print("Invalid input: x must be an integer value and 10000 < x < 60000")
    # print("You may uncomment line 10 to encrypt larger numbers with larger prime numbers")
    exit(0)

  print ("x = %s" % x)

  for i in ['Alice', 'Bob']:
    if i == "Alice":
      A = keygen(i)
    elif i == "Bob":
      B = keygen(i)

  s = sign(x, B['private_key'])

  y = encrypt(x, B['public_key'])

  dy = decrypt(y, B['private_key'])

  sv = sig_verify(s, B['public_key'])

if __name__ == "__main__":
    main()