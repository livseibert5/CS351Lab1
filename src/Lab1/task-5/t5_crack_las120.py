from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import binascii as binascii

def findKey(iv, goal, message):
  words = open('words.txt', 'r')
  for word in words.readlines():
    w = word.strip()
    print(w)
    data = binascii.hexlify(w.encode('hex')).strip()
    bin = bytearray.fromhex(data).strip()
    key = pad(bin, 16).strip()
    print(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message,16))
    if (goal == message.decode().encode('hex')):
      return word
  return "no key found"

  

if __name__ == '__main__':
  iv = bytearray.fromhex('aa bb cc dd ee ff 00 99 88 77 66 55 44 33 22 11')
  goal = '46 be b3 b8 32 97 34 95 f7 9b 86 08 84 24 5e 43 1d 73 c2 d3 f7 e3 a7 63 2d ce 89 4e d1 4f f6 2b'
  f = open('flag', 'r')
  message = f.read()
  out = findKey(iv, goal, message)
  print(out)