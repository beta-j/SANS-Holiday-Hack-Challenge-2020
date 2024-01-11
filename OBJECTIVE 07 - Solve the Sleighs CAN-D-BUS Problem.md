# Objective 7 – Solve the Sleigh’s CAN-D-BUS Problem #

## OBJECTIVE: ##
>Jack Frost is somehow inserting malicious messages onto the sleigh's CAN-D bus. We need you to exclude the malicious messages and no others to fix the sleigh. Visit the NetWars room on the roof and talk to Wunorse Openslae for hints.
#  

## Hints ##
<details>
  <summary>Hints provided for Objective 7</summary>
 
>-	**WUNORSE OPENSLAE:** Try filtering out one CAN-ID at a time and create a table of what each might pertain to. What's up with the brakes and doors?

</details>

#  
## PROCEDURE: ##
I filtered out the most commonly occurring IDs – ideally i’d like to see no updates while the sleigh is idle.  We can then start re-enabling these one by one and see what changes when I tweak the sleigh’s inputs.
```
-	018#
-	244#
-	019#
-	080#
-	188#
-	19B#
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/49bc6ab2-e0ab-4543-b3ff-bbce6d2df018)

With some experimentation I figured out the following:
Function|	ID|	Code (Range)|	Status
:---|:---:|:---|:---
Start Signal|	`02A#`|	`00FF00`|	OK
Stop Signal| `02A#`|`0000FF`|	OK
Rev Counter| `244#`|	`00000003E4` to around `000000233E`|	OK
Lock Signal	|`19B#`|	`0000000000000`|	Code keeps popping up randomly with value `0000000F2057`
Unlock Signal| `19B#`|		`00000F000000`| Code keeps popping up randomly with value `0000000F2057`	
Steering|	`019#`|	`FFFFFFCE` to `000032`|	OK
Brakes|	`080#`|	`000000` to `000064`|	Weird values starting with `FFFFF0` pop up between legitimate signals

So it looks like the malicious messages are using the **Un/Lock Signal** and **Brake IDs** (`19B#` and `080#`).

Filtering out the malicious un/lock signals is Pretty straightfoward and I filter out anything that equals `19B#0000000F2057`.

For the brakes, I had to remind myself that these are signed integers and therefore anything starting with a `F` is a negative number.  Therefore we need to filter out anything with `ID` `080` that is below `0000000000` and we effectively filter out all the illegal values for the brakes too.

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/e2f9e85d-be00-48a7-8e07-4f155f610837)


