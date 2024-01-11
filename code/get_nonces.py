#!/usr/bin/python3
from naughty_nice import *

with open('official_public.pm', ‘rb’)as fh:
  official_public_key = RSA.importKey(fh.read())
  c2 = Chain(load=True, filename='blockchain.dat')  

for x in range (0,1548):
  nonce= c2.blocks[x].nonce
  print (nonce)
