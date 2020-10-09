##### Table of Contents  
[Encoding Systems](#Encodings)
* [ASCII](#ascii--usually-base10---decimal-)
* [Binary](#binary-base2)
* [Hexadecimal](#hexadecimal-base16)
* [Base64](#base64)
* [Links](#links)

[Modern Cryptography](#modern-cryptography)
* [RSA](#rsa)
  + [Requirements](#requirements)
  + [RSA 0](#rsa-0)
  + [RSA 1](#rsa-1)

# Encodings

##### ASCII ( Usually Base10 - Decimal )
Every byte (8-bits) has an id (number) to allow the operating system(windows,linux,android,macOS) or browser or every other application to recognize it.
Ascii codes are regrouped in ascii table where only printable characters have code from 32 (SPACE) up to 126 (~).

Composed by an alphabet of
`0123456789`

![](http://www.asciitable.com/index/asciifull.gif)

In python  
~~~python
import string #this is a builtin module you don't have to install it

pr = string.printable #printable characters (32-126)
print(pr)
#output: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"

char = 'm'
print(ord(char)) 
#output: 109 --> ascii('m') = 109

ascii = 97
print(chr(ascii))
#output: 'a' --> ascii('a') = 97
~~~~

##### Binary (Base2)
The unit of information. before to get recognized by the OS or the browser. Ascii code is represented as a binary of 8-bits (byte/octet).

Composed by an alphabet of
`01`

Every 8 bits get converted to ascii and get recognized.
`1100001 --> 97 --> 'a'`

in python  
~~~python
print(bin(97))
#output: '0b1100001' --> the output is a string containing only 0 and beginning with 0b proving that's a binary representation

#example
msg = "sc2"
msg_bin = [bin(ord(char))[2:].zfill(8) for char in msg] #i added zfill(8) because python by default removes trailing "0" so the length won't be 8 but less (because all characters have ascii less than 127 = 2^8-1 that means a bit length less than 8
msg_bin = "".join(msg_bin)
print(msg_bin)
#output: 011100110110001100110010

#now doing the inverse
msg = [msg_bin[i:i+8] for i in range(0,len(msg_bin),8)] #taking bits 8 by 8
msg = [int(s,2) for s in msg] # converting binary to ascii (base10)
#int(string,base) convert that string to a base, available bases from 2 to 36
msg = [chr(s) for s in msg]
msg = "".join(msg)
print(msg)
#output: "sc2"

#this can be done in one line but i showed steps for more comprehension
#in one line
msg = "sc2"
msg_bin = "".join(bin(ord(char))[2:].zfill(8) for char in msg)
msg = "".join(chr(int(msg_bin[i:i+8],2)) for i in range(0,len(msg_bin),8))
~~~~

##### Hexadecimal (Base16)
Used generally for [hashes](https://blog.emsisoft.com/fr/6799/qu-est-ce-qu-un-hash/).

Composed by an alphabet of
`0123456789abcdef`

Like in binary, every byte (character) is represented by it's ascii code but in hexadecimal base
`61 (hex) --> 97 (decimal) --> 'a'`
in python
```python
print(chr(int(61,16)))
#ouyput: 'a'
#to do so manech chno93dou kol marra na3mlou fhal korfi .. just n'importiw module esmou binascii
#(string to hex)
import binascii
msg_hex = binascii.hexlify(b'sc2') #we put b before the string to be considered as a byte object that means every character will be equivalent to it's ascii code
print(msg)
#outpuy: b'736332'

#73(hex) --> 115(decimal-ascii) --> 's'
#63(hex) --> 99(decimaal - ascii) --> 'c'
#32(hex) --> 50(decimal - ascii) --> '2'
#736332 --> sc2
#in the inverse (hex to string)
msg = binascii.unhexlify(msg_hex)
#output: b'sc2'
```

##### Base64
Used generally in web to transfer data (binary files or images that are not representable by borwsers).

Well the algorithm is not that important :p !

Composed by an alphabet of `0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=`

In python
```python
import base64
msg = b"sc2"

print(base64.b64encode(msg))
#output: b'c2My'

print(base64.b64decode(b'c2My'))
#output: b'sc2'

```

And other more and more bases like base32,base58,base62,base85 etc...

##### Links
Useful links:
- [CyberChef](https://gchq.github.io/CyberChef/)
- [dcode.fr](https://www.dcode.fr/)




# Modern Cryptography
## RSA

Brievely, RSA is a public-key cryptosystem that is widely used for secure data transmission.

The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, the "factoring problem". Because of this, it is not commonly used to directly encrypt user data.

More often, RSA is used to transmit shared keys for symmetric key cryptography, which are then used for bulk encryption-decryption. 
For more details about the encryption and decryption, you can check [this](https://en.wikipedia.org/wiki/RSA_(cryptosystem)). (It's quite enough to know all about RSA encryption)


Now let's go through the challenges of the last CTF.


#### Requirements!
We need some python packages to help us.
Go to your command line, check you are connected to internet and type
> pip install pycryptodome


#### RSA 0
The challenge provided 
* *p,q* (prime numbers,must be private) 
* *n = p \* q* ( modulus - public) 
* *e* (Public Exponent)
* *c* (ciphertext)

To decrypt an RSA encrypted cipher we need to get the private exponent *d = modular_inverse(e,phi(n))*

So nothing is left but implementing it in python
```python
from Crypto.Util.number import inverse,long_to_bytes
#inverse = inverse modular that means ( a * inverse(a,n) ) = 1 mod n
#long_to_bytes is a shortcut for unhexlify(hex(enc)) with enc a decimal number! (A way to convert data like we saw in System encodings

p = ...
q = ...
n = ...
e = ...
c = ...
assert n == p * q # just to make sure that n == p * q

phi = (p - 1) * (q - 1) # this is Euler totient (betbi3a 9rineha fel prepa :p , malezmch tet7fadh 3la ases dima (p-1)*(q-1) lezem ta3ref relation lkemla 5atr we need it ;)
d = inverse(e,phi)
m = pow(c,d,n)

print(long_to_bytes(m))
#output: b'SC2Flag{W3lc0m3_t0_RSA_w0rld}'

```


#### RSA 1
The challenge provided 
* *n* ( modulus - public) 
* *e* (Public Exponent)
* *c* (ciphertext)

So to know what is behind this encrypted message we need to calculate d, which is calculated from p and q (which we do not have here). What we do ?? we factorize n (online from [here](http://factordb.com/) or [here](https://www.alpertron.com.ar/ECM.HTM))

After getting the factors, the rest is to do similarly like the previous task but with the new values of p,q,n,e and c.
