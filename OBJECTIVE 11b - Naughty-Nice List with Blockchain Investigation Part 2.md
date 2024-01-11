# Objective 11a – Naughty/Nice List with Blockchain Investigation Part 2 #
## OBJECTIVE: ##
>The SHA256 of Jack's altered block is:`58a3b9335a6ceb0234c12d35a0564c4ef0e90152d0eb2ce2082383b38028a90f`.
>If you're clever, you can recreate the original version of that block by changing the values of only 4 bytes. Once you've recreated the original block, what is the SHA256 of that block?


#  

## HINTS : ##
<details>
  <summary>Hints provided for Objective 11b</summary>
 
>-	**TANGLE COALBOX:** A blockchain works by "chaining" blocks together - each new block includes a hash of the previous block. That previous hash value is included in the data that is hashed - and that hash value will be in the next block. So there's no way that Jack could change an existing block without it messing up the chain...
>-	**TANGLE COALBOX:** Qwerty Petabyte is giving [a talk](https://www.youtube.com/watch?v=7rLMl88p-ec) about blockchain tomfoolery!
>-	**TANGLE COALBOX:** The idea that Jack could somehow change the data in a block without invalidating the whole chain just collides with the concept of hashes and blockchains. While there's no way it could happen, maybe if you look at the block that seems like it got changed, it might help.
>-  **TANGLE COALBOX:** If Jack was somehow able to change the contents of the block AND the document without changing the hash... that would require a very [UNIque hash COLLision](https://github.com/cr-marcstevens/hashclash).
>-	**TANGLE COALBOX:** Shinny Upatree swears that he doesn't remember writing the contents of the document found in that block. Maybe looking closely at the documents, you might find something interesting.
>-	**TANGLE COALBOX:** Apparently Jack was able to change just 4 bytes in the block to completely change everything about it. It's like some sort of [evil game](https://speakerdeck.com/ange/colltris) to him.


</details>

## TOOLS: ##
[Download the required toolkit for Objective 11 here](assets/Objective%2011.zip)

#  
## PROCEDURE: ##
I used the commented part in `naughty_nice.py` to create a [python script](code/get_block.py) that cycles through the blocks one by one and prints the blocks' index and the score.  I immediately notice that the block at index `1010` has a massive score of `4294967295` (`0xffffffff`)– this must be the block that Jack tampered with.  I also created a [second script](code/get_sha256.py) to check the SHA256 hash of the blocks against the one given in the hints to confirm that I have the right block.

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/59426d0b-d7a4-499f-ae78-19723f0ae23e)

I modified the same script slightly to dump the corresponding files and I got `129459.bin` and `129459.pdf`.

[Opening the pdf](assets/KringleKon3_2020_PosTShelL.pdf) with a hex editor we see a plaintext saying `/Type/Catalog/_Go_Away/Santa/Pages 2`
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/e23c61c6-2b08-4802-bb1d-45d3c25c6175)

This reminded me of one particular [slide](https://speakerdeck.com/ange/colltris?slide=112) in the [Colltris deck](https://speakerdeck.com/ange/colltris).  So following its advice, I changed the value following `pages` from `2` to `3`.

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/9f082926-013e-48fa-bda4-ef924522049e)


I could now re-open the pdf and see a completely new message from Shinny Upatree inside it – so I must be on the right track.
Thanks to **@elakmarcus#5519** on Discord who then nudged me towards this [slide](https://speakerdeck.com/ange/colltris?slide=112):
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/61d64cb4-7ebd-437d-9bd7-41ceb7e50f90)

I followed the suggested instructions: since I incremented the value for pages by 1, I decreased the corresponding value 128 bytes later by 1. 

This substitutes the pdf with the correct one while keeping the same MD5 hash value.  Now I just need to change one more pair of bytes, so I figure this must be the one determining whether the block is naughty or nice.

I modified the previous [python scripts to output the whole block to a binary file](code/output_block.py) (so that I’d avoid any potential errors when re-assembling the block later).  I then loaded this new binary in the hex editor and changed the two bytes mentioned above again.  Next, I looked for the entry for `0xffffffff` (i.e. Jack’s score) and judging by the block structure I knew that the next byte determines whether the entry is for **Naughty** or **Nice**.  So, just like I did before, I changed this from a `1` to a `0` and incremented the corresponding byte 128 bytes later by 1 and saved the binary.
```
root@kali:~/objective11# sha256sum /root/pcshare/outfile.txt
fff054f33c2134e0230efb29dad515064ac97aa8c68d33c58c01213a0d408afb  /root/pcshare/outfile.txt
```

Now I just run `sha256sum` to get the sha256 hash of the original block 😊

***Never in a million years would I have thought that I’d make it this far!!!!***


