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

# CHALLENGE 2 - Grepping for Gold #

## OBJECTIVE : ##
>Howdy howdy!  Mind helping me with this homew- er, challenge?
>Someone ran `nmap –oG` on a big network and produced this `bigscan.gnmap` file.  The `quizme` program has the questions and hints, and incidentally, has NOTHING to do with an Elf University assignment. Thanks!

#  

## HINTS: ##
<details>
  <summary>Hints provided for Objective 13</summary>
  
>-	Check [this](https://ryanstutorials.net/linuxtutorial/cheatsheetgrep.php) out if you need a grep refresher.

</details>

  
## PROCEDURE : ##

>-	**Q:** What port does 34.76.1.22 have open?
```
elf@e49df7806f10:~$ cat bigscan.gnmap | grep 34.76.1.22
Host: 34.76.1.22 ()     Status: Up
Host: 34.76.1.22 ()     Ports: 62078/open/tcp//iphone-syn
