# pip install pycryptodome
from Crypto.Hash import SHA3_512  
#create an object
obj = SHA3_512.new()  
#Continue hashing of a message by consuming the next chunk of data.
obj.update(b'I love cryptography.') 
#Return the printable digest of the message that has been hashed so far.Hexadecimal encoded. 
print(obj.hexdigest()) 