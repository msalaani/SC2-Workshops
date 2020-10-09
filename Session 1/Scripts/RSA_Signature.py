from Crypto.PublicKey import RSA #This is used to generate RSA staff

keyPair = RSA.generate(bits=1024)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

#output
#Public key:  (n=0x8d28a5825fdd36f83266df8d6ad25b2d9dce522458e7ddb02e13cef51c9b159c9e526396763da8931b23d7f09dcc04cd06ad243c3c176662673098073772f5b06fa89af9824c25f09ca8d04ad8a162874e040ff750e6e46004860a61cec556178be4912715864e06f5b8e26640695c7311177b60e7a1d538debe9597adda9635, e=0x10001)
#Private key: (n=0x8d28a5825fdd36f83266df8d6ad25b2d9dce522458e7ddb02e13cef51c9b159c9e526396763da8931b23d7f09dcc04cd06ad243c3c176662673098073772f5b06fa89af9824c25f09ca8d04ad8a162874e040ff750e6e46004860a61cec556178be4912715864e06f5b8e26640695c7311177b60e7a1d538debe9597adda9635, d=0xd0269fe92073941b6a37486fc09570de53556acb2e4ebb1890d9a4d4ccd9e3848ff1ede871737aa171e3e90967a6f16d63eaed03e5989be17f48a8e5fb5e09eb71b88333fa3f820bc4aed9cf8276a3dba153d90af8807927d90452936c6b5cda73763d7c001733d370fc827c9175475df5961f8381f93a441d4c57ac4bae01)

# RSA sign the message
msg = b'A message for signing'
from hashlib import sha512
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

#output Signature: 0x1bf3c98fc61b9fcb4013d057cdbf145e490f28b5a0a4b9845fe15b9ae5208f822ac77b5401e97cb5f6d9612d6643c06bbf3989d7429c13ddf1887c9b5ef33e215990c298401185c55c1b60bc5299a4869e599ef907907d3509b2928f7d4bbb978e66da0a57090efa02d9934910f44fc6b61508326a441b78e92ba649d0627166

# RSA verify signature
msg = b'A message for signing'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)

#output: Signature valid: True

# RSA verify signature (tampered msg: that means we add something to our original message)
msg = b'A message for signing (tampered)'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid (tampered):", hash == hashFromSignature)

#output Signature valid (tampered): False
