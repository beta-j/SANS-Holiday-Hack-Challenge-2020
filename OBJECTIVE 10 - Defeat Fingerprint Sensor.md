# Objective 10 – Defeat Fingerprint Sensor #

## OBJECTIVE: ##
>Bypass the Santavator fingerprint sensor. Enter Santa's office without Santa's fingerprint.
#  

## PROCEDURE: ##
Let’s begin by looking at the source code in the elevator.

Inside `app.js` we see that the script is checking whether a token `besanta` is passed to it – presumably this will make the fingerprint scanner clickable

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/55a435c2-889a-40bf-b1a7-e972ac3bd97d)

Searching around in the **elements** pane I come across this entry:
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/ef112fd5-aaf7-4253-876a-8dc523c2f733)

I tried adding `,besanta` to the end of the URI and it worked! The elevator took me to Santa’s work shop!  Well that was easier than I expected!
