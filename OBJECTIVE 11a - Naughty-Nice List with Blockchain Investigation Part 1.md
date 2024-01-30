# Objective 11a – Naughty/Nice List with Blockchain Investigation Part 1 #
## OBJECTIVE: ##
>Even though the chunk of the blockchain that you have ends with `block 129996`, can you predict the nonce for `block 130000`? Talk to Tangle Coalbox in the Speaker UNpreparedness Room for tips on prediction and Tinsel Upatree for more tips and tools. (Enter just the 16-character hex value of the nonce)

#  

## HINTS : ##
<details>
  <summary>Hints provided for Objective 11a</summary>
 
>-	**TANGLE COALBOX:** If you have control over two bytes in a file, it's easy to create MD5 [hash collisions](https://github.com/corkami/collisions). Problem is: there's that nonce that we would have to know ahead of time.

</details>

## TOOLS: ##
[Download the required toolkit for Objective 11 here](assets/Objective%2011.zip)

#  
## PROCEDURE: ##
So I start by downloading the toolkit and it looks like it’s something I need to install using **Docker** …. 
Great I have little to no experience with Docker!

Eventually I figure it out
```console
# sudo apt-get install docker-ce
# docker build --tag=”sanshh:Dockerfile” /root/objective11a/dockerbuild/
```
Running `# docker images` confirms that we now have a repository called `sanshh`.
Running `./docker.sh now` takes me into the newly built Docker environment (I think)

I wrote a [python script that cycles through all the blocks and retrieves their nonce](code/get_nonces.py). 

The result of this script was stored in a text file (`outfile.txt`) and this was then fed to [a second python script](code/predict_nonces.py) which ran the [Mersenne twister predictor](https://github.com/kmyk/mersenne-twister-predictor) on the collected nonces.  I set it to take the first 1540 entries as its learning data and to then predict the last 8 entries so that I could compare the output to the last 8 known nonces on the list.  Once I could confirm that the output was matching correctly, I edited the script to give me the expected nonces up to block index `130000`.

The predicted value for block 130000 was `6270808489970332317` which in hex is **`57066318F32F729D`**

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/25abda53-b9ec-492b-9712-f349f983f6f2)


