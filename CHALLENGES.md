# CHALLENGE 1 - Linuc Primer #

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
