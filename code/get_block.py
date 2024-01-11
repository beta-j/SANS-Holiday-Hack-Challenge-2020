#!/usr/bin/env python3

from naughty_nice import *

with open('official_public.pem', 'rb') as fh:
    official_public_key = RSA.importKey(fh.read())
c2 = Chain(load=True, filename='blockchain.dat')
for ww in range(len(c2.blocks)):
   print("block no. ",ww," score: ",c2.blocks[ww].score)	# Print the block array indec and score
