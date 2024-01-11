# OBJECTIVE 3 - Point-of-Sale Password Recovery #

## OBJECTIVE : ##
>Help Sugarplum Mary in the Courtyard find the supervisor password for the point-of-sale terminal. What's the password?
#  

## HINTS: ##
<details>
  <summary>Hints provided for Objective 1</summary>
  
>-  **SUGARPLUM MARY:** There are [tools](https://www.npmjs.com/package/asar) and [guides](https://medium.com/how-to-electron/how-to-get-source-code-of-any-electron-application-cbb5c7726c37) explaining how to extract ASAR from Electron apps.
>-	**SUGARPLUM MARY:** It's possible to extract the source code from an Electron app.



</details>

#  

## PROCEDURE : ##

Download the .exe file and open it with `7zip`. The `resources` folder contains a file called `app.asar`.

This can be opened using `7zip` (after installing a plugin).  The .asar file contains a helpful readme file that points us to the first line in `main.js` for the password which truns out to be **`santapass`**

![image](https://github.com/beta-j/SANS-Holiday-Hack-Challenge-2020/assets/60655500/c4053ec2-9259-46e8-b003-abd59761892b)


