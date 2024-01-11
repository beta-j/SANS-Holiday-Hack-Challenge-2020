# Objective 5 – Open HID Lock #

## OBJECTIVE:##
>Open the HID lock in the Workshop. Talk to Bushy Evergreen near the talk tracks for hints on this challenge. You may also visit Fitzy Shortstack in the kitchen for tips.
#  

## Hints##
<details>
  <summary>Hints provided for Objective 5</summary>
 
>-  **BUSHY EVERGREEN:** The Proxmark is a multi-function RFID device, capable of capturing and replaying RFID events.
>-  **BUSHY EVERGREEN:** Larry Pesce knows a thing or two about [HID attacks](https://www.youtube.com/watch?v=647U85Phxgo). He's the author of a course on wireless hacking!
>-	 **BUSHY EVERGREEN:** There's a [short list of essential Proxmark commands](https://gist.github.com/joswr1ght/efdb669d2f3feb018a22650ddc01f5f2) also available.
>-	 **BUSHY EVERGREEN:** You can also use a Proxmark to impersonate a badge to unlock a door, if the badge you impersonate has access. ``lf hid sim -r 2006......``
>-	 **BUSHY EVERGREEN:** You can use a Proxmark to capture the facility code and ID value of HID ProxCard badge by running `lf hid read` when you are close enough to someone with a badge.
</details>

#  
## PROCEDURE: ##
Now that I have the Proxmark3, I took some time reading through the help files and experimenting to understand what it does and how it works.  
It’s a pretty-cool RF hacking tool which allows you to read different kinds of RF cards and also to simulate them. The Proxmark3 has an **auto** mode which automaticlaly looks for readable cards in the vicinity and gives some info about them.  It can also be set manually to look for specific kinds of RF signals.

I spent some time walking around Kringlecon swiping elves’ cards – but I had a pretty good idea who’s card I actually needed to swipe thanks to a hint I got from Fitzy Shortstack who let me know that ***“Santa really seems to trust Shinny Upatree”***.

So while standing next to Shinny Upatree:
```
pm3 --> auto
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/7b835e90-176b-4396-93c0-daf8c50cb120)

Or else; 
```
pm3 --> lf hid read
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/9f4e772c-69d2-479e-bc08-67aba5f02b47)

Now I know that I need to simulate a **Low Frequency 26-Bit HID** Card with a **Facility Code** of **113** and **Card Number 6025**.

From the output of ``pm3--> wiegand list`` I can see that the corresponding code for a HID 26-bit is **H10301**.

So I headed back up to the locked door in the workshop and while standing next to it I ran:
```
pm3--> lf hid sim –w H10301 --fc 113 --cn 6025
```
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/32c2f7fb-8a90-498d-990c-b55960b65c72)

That’s it!  The door is unlocked and objective is complete.  Now to continue exploring the place as Santa...
