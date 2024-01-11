# Objective 6 – Splunk Challenge #

## OBJECTIVE: ##
>Access the Splunk terminal in the Great Room. What is the name of the adversary group that Santa feared would attack KringleCon?
#  

## HINTS ##
<details>
  <summary>Hints provided for Objective 6</summary>
 
>-	**MINTY CANDYCANE:** Defenders often need to manipulate data to `decRypt`, `deCode`, and `reform` it into something that is useful. Cyber Chef is extremely useful here!
>-	**MINTY CANDYCANE:** There was a great [Splunk talk](https://www.youtube.com/watch?v=qbIhHhRKQCw) at KringleCon 2 that's still available!
>-	**MINTY CANDYCANE:** Dave Herrald talks about emulating advanced adversaries and [hunting them with Splunk](https://www.youtube.com/watch?v=RxVgEFt08kU).

</details>

#  
## PROCEDURE: ##
This challenge was quite frustrating for me, as I had no idea of what Splunk is and no experience using it at all, and I couldn’t really understand why some of the filters I was using weren’t giving me any results at all.  Nevertheless it was a massive learning experience and the sense of satisfaction having completed it successfully was immense 😄

**Question 1**
>How many distinct MITRE ATT&CK techniques did Alice emulate?
```
¦ tstats count where index=* by index
```
  Count the unique index numbers only
***Ans: `26`***


**Question 2**
>What are the names of the two indexes that contain the results of emulating Enterprise ATT&CK technique 1059.003? (Put them in alphabetical order and separate them with a space)
```
| tstats count where index=* by index 
| search index=T1059.003*
```
***Ans: `t1059.003-main t1059.003-win`***

**Question 3**
>One technique that Santa had us simulate deals with 'system information discovery'. What is the full name of the registry key that is queried to determine the MachineGuid?

-  Go to the MITRE ATT&CK Enterprise Matrix at [https://attack.mitre.org/matrices/enterprise/](https://attack.mitre.org/matrices/enterprise/)
-  Search for `system information discovery`
-  We find that it is `ID: T1082`
-  Go to Atomic Red Team GitHub Repo: [https://github.com/redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team)
-  Find `T1082` under the `atomics` folder
-  Reading through the .md file we find `Atomic Test #8 – Windows MachineGUID Discovery`
 
***Ans: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography`***

**Question 4**
>According to events recorded by the Splunk Attack Range, when was the first OSTAP related atomic test executed? (Please provide the alphanumeric UTC timestamp.)
```
| index = attack
| search OSTAP
```
***Ans: `2020-11-30T17:44:15Z`***

**Question 5**
>One Atomic Red Team test executed by the Attack Range makes use of an open source package authored by frgnca on GitHub. According to Sysmon (Event Code 1) events in Splunk, what was the ProcessId associated with the first use of this component?

-  I looked up `frgnca` on github and found he has 8 repositories of which only two seemed like they may be used for malicious attacks: `AudioDeviceCmdlets` and `fcpi`
-  Running the search query:
```
index=attack | search *audio* EventCode=1
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/87e1d482-6e87-4631-b6ce-87df70a6ef36)
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/c839c513-e792-4386-8f58-7e6df893d2d7)

***Ans: `3648`***

**Question 6**
>Alice ran a simulation of an attacker abusing Windows registry run keys. This technique leveraged a multi-line batch file that was also used by a few other techniques. What is the final command of this multi-line batch file used as part of this simulation?

-  I searched for ``index=* | search bat``
-  This returns a number of batch files and the associated technique number
-  I looked up the individual technique numbers one by one in the `atomic-red-team` github repo until I found one that had multiple lines (`T1074.001`) and copied the last line for the answer.
  
 ![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/0cfed4e8-49e3-4f71-9c77-092b6332ee4f)
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/3d6fa0af-624f-4169-bfd8-566c48eeeaa5)

Ans: ***`quser`***


**Question 7**
>According to x509 certificate events captured by Zeek (formerly Bro), what is the serial number of the TLS certificate assigned to the Windows domain controller in the attack range?

-  Search for ``index=* sourcetype=”bro:x509:json”``
-  Look at the entries for `certificate.serial` – there are 12 in total but the most frequently used certificate serial no. is clear:

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/91aeaf36-df5a-4658-92f9-1daa02efe128)

***Ans: `55FCEEBB21270D9249E86F4B9DC7AA60`***


**Challenge Question**
>Access the Splunk terminal in the Great Room. What is the name of the adversary group that Santa feared would attack KringleCon?

All the hints required for this challenge are in the challenge question itself.  Looking through [the Splunk talk on Youtube](https://www.youtube.com/watch?v=qbIhHhRKQCw), I quickly found Santa’s favourite phrase at the end of it.

Alice also tells me that the ciphertext is base64 encoded and that it is encrypted with an old algorithm that uses a key – a quick Google search tells me that this is probably **RC4**.

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/541e0c56-177b-4dcd-bc26-477ef11f7abb)

**Step 1** – Encode the key phrase to base64 – i.e. `Stay Frosty` becomes ``U3RheSBGcm9zdHk=``

**Step 2** – Create a recipe on [http://icyberchef.com/](http://icyberchef.com/) which;
1.  Takes the ciphertext as a text input
1.  Converts it from Base64
1.  Takes the text created in the previous step and decrypts it using RC4 with the Base64 Passphrase created in Step 1
    
**Step 3** – This recipe gives us a cleartext legible output
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/419d8508-9291-4c30-a126-1cbbe25eb9b2)

***Answer: `The Lollipop Guild`***

