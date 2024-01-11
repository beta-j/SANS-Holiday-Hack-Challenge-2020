#!/usr/bin/env python3

from naughty_nice import *

with open('official_public.pem', 'rb') as fh:
    official_public_key = RSA.importKey(fh.read())
c2 = Chain(load=True, filename='blockchain.dat')
jackshash = "58a3b9335a6ceb0234c12d35a0564c4ef0e90152d0eb2ce2082383b38028a90f"

for ww in range(len(c2.blocks)):			# cycle through all the blocks
  h = SHA256.new()
  h.update(c2.blocks[ww].block_data_signed())	# calculate the sha256 hash of the data 
  if(h.hexdigest() == jackshash):		# compare the hash to jack’s hash
    outfile = open("outfile.txt", "wb")    		# create a new binary file with write-only access
    outfile.write(c2.blocks[ww].data)		# dump the data to the binary file
