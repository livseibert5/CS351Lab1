from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import binascii as binascii

def findKey(iv, goal, message):
  words = open('words.txt', 'r')
  for word in words.readlines():
    w = word.strip()
    if (len(w) <= 16):
      topad = w
      while (len(topad) < 16):
        topad = topad + '#'
      data = topad.encode('hex').strip()
      key = data.decode('hex')
      cipher = AES.new(key, AES.MODE_CBC, iv)
      ciphertext = cipher.encrypt(message)
      cipherstring = ciphertext.encode('hex')
      short = cipherstring[0:64]
      print(short)
      if (short == goal):
        return w
  return "no key found"  

if __name__ == '__main__':
  iv = 'aabbccddeeff00998877665544332211'.decode('hex')
  goal = '46beb3b832973495f79b860884245e431d73c2d3f7e3a7632dce894ed14ff62b'
  print(goal)
  f = open('flag', 'r')
  mess = f.read()
  mess = pad(mess, 16)
  messhex = mess.encode('hex').strip()
  print(messhex)
  message = messhex.decode('hex')
  out = findKey(iv, goal, message)
  print(out)