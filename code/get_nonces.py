#!/usr/bin/python3
from naughty_nice import *

with open('official_public.pm', ‘rb’)as fh:
  official_public_key = RSA.importKey(fh.read())
  c2 = Chain(load=True, filename='blockchain.dat')  

for x in range (0,1548):
  nonce= c2.blocks[x].nonce
  print (nonce)

predict_nonces.py

#!/usr/bin/env python3
import random
from mt19937predictor import MT19937Predictor

predictor = MT19937Predictor()		# load the Mersenne Twister Predictor
file = open("outfile.txt", "r")		# load the file with the nonces we got with get_nonces.py
content =  file.readlines()		

for line in range (0,1548):		# cycle through the file line by line
    
    x = int(content[line])		# read the value of each line and convert it to integer
    print (line, ": ",x)
    predictor.setrandbits(x, 64)		# teach the value to the predictor

for i in range (129997, 130001):
  print (i,": ",predictor.getrandbits(64))  # predict the values for indexes 129997 to 130000
