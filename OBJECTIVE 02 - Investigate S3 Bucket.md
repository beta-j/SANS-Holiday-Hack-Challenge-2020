# OBJECTIVE 2 - Investigate S3 Bucket #

## OBJECTIVE : ##
>When you unwrap the over-wrapped file, what text string is inside the package? Talk to Shinny Upatree in front of the castle for hints on this challenge.

#  

## PROCEDURE : ##

-  Add `Wrapper3000` to the wordlist using `nano`
  
-  Run ``./bucket_finder wordlist``
    -  This returns a public link: `http://s3.amazonaws.com/wrapper3000/package`

-	Download with ``curl http://s3.amazonaws.com/wrapper3000/package -o package``

-	Using the `file` command on `package` returns ASCII text, with very long lines

-	Using `apropos wrapper` returns `p7zip`
  
-	Running `base64 -d package` shows a piece of clear text reading `package.txt.Z.xz.xxd.tar.bz2UT`
  
-	I saved the base64 output to a new file; `package2`
  
-	Then run `file package2` which returns `Zip archive data, at least v1.0 to extract`

-	Renaming the file to `package.zip` and running `unzip package.zip` now gives me a file: `package.txt.Z.xz.xxd.tar.bz2` – time to start unwrapping I guess...
    -  `tar –xf package.txt.Z.xz.xxd.tar.bz2` produces `package.txt.Z.xz.xxd`
    -  .xxd file is a hexdump of a file.  Running ``xxd –r package.txt.Z.xz.xxd > package.txt.Z.xz`` outputs the original file to a new XZ Compressed data file
    -  Running ``xz -d package.txt.Z.xz`` gives me `package.txt.Z`
    -  Running ``uncompress package.txt.Z`` finally gives me `package.txt` which is a plain-text readable file with the phrase; **`North Pole: The Frostiest Place on Earth`**

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/46b8ab36-a76d-444c-9b63-969d1df4846e)
