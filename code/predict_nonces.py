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
