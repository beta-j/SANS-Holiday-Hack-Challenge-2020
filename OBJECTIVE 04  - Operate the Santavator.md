# OBJECTIVE 4 - Operate the Santavator #

## OBJECTIVE : ##
>Talk to Pepper Minstix in the entryway to get some hints about the Santavator.
#  

## HINTS: ##
<details>
  <summary>Hints provided for Objective 4</summary>
  
>-	**RIBB BONBOWFORD:** There may be a way to bypass the Santavator S4 game with the browser console...



</details>

#  

## PROCEDURE : ##

Once I found all the bulbs and bolts it was quite easy to get the stream of electrons flowing to each of the three conduits. However there is no clickable button to take me to the workshop (Floor 1.5).

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/39af5eaa-1a9b-4809-8ab5-d44bb85b4539)

To get to floor 1.5, I right-clicked on the button panel and selected **inspect**.

Under the **elements** tab I found the line ``<button class=”btn btn15active” data-floor=”1.5”>...</button> == $0`` and clicked it.

On the right-hand pane under `style.css:31` I unticked the entry for `pointer events: none`

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/1540dc6b-beec-4d7b-a3e3-9521f59378f5)

Although the button to Floor1.5 is still missing, this technique makes the button gap clickable and sure enough the Santavator takes you to the Workshop level.

To make the button visible untick ``display: none`` for ``<img class=”f15btn” src=”images/floor1-5button.png”>``
