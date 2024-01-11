Objective 5 – Open HID Lock
Open the HID lock in the Workshop. Talk to Bushy Evergreen near the talk tracks for hints on this challenge. You may also visit Fitzy Shortstack in the kitchen for tips.
Hints
-	BUSHY EVERGREEN: The Proxmark is a multi-function RFID device, capable of capturing and replaying RFID events.
-	BUSHY EVERGREEN: Larry Pesce knows a thing or two about HID attacks. He's the author of a course on wireless hacking!
-	BUSHY EVERGREEN: There's a short list of essential Proxmark commands also available.
-	BUSHY EVERGREEN: You can also use a Proxmark to impersonate a badge to unlock a door, if the badge you impersonate has access. lf hid sim -r 2006......
-	BUSHY EVERGREEN: You can use a Proxmark to capture the facility code and ID value of HID ProxCard badge by running lf hid read when you are close enough to someone with a badge.
Procedure
Now that I have the Proxmark3, I took some time reading through the help files and experimenting to understand what it does and how it works.  It’s a pretty-cool RF hacking tool which allows you to read different kinds of RF cards and also to simulate them. The Proxmark3 has an ‘auto’ mode which automaticlaly looks for readable cards in teh vicinity and gives some info about them.  It can also be set m,anually to look for specific kinds of RF signals.
I spent some time walking around Kringlecon swiping elves’ cards – but I had a pretty good idea who’s card I actually needed to swipe thanks to a hint I got from Fitzy Shortstack who let me know that “Santa really seems to trust Shinny Upatree”
So while standing next to Shinny Upatree:
pm3 --> auto
 
Or else; pm3 --> lf hid read
 
Now I know that I need to simulate a Low Frequency 26-Bit HID Card with a Facility Code of 113 and Card Number 6025.
