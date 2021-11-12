## Part 1. How to log into Rivanna. 

### Check out [Log into Rivanna - video Tutorial](https://youtu.be/_kpRgRpGMXo)

1. Type [https://_rivanna_-_portal_._hpc_.virginia.edu](https://rivanna-portal.hpc.virginia.edu) into your web browser. This will automatically trigger a UVA authentication step. Input your UVA credentials to enter the super-computer GUI.
2. Once inside you will see a "Message of the day board". Go to the top bar and search for the option "**Interactive Apps**".
3. Once you click **Interactive Apps** a drop down menu will appear. Click on the option names **Desktop**. 
4. Clicking on Desktop will give you the option to create an interactive session with the supercomputer. Before you can do that you need to tell the supercomputer what are the parameters of your interactive session. These are:
	```
	Rivanna partition: --> select "instructional"
	Number of hours: --> 3
	Number of cores:--> 3 
	Memory Request in GB:--> 24
	Allocation (SUs): --> leave empty
	Optional: GPU type for GPU partition**: --> leave empty
	Optional: Slurm Option: --> leave empty
	Optional: Group: --> write biol4585j-yey2sn
	```
5. Once you have these entered these options go ahead and press **LAUNCH**
6. It may take a couple seconds to a minute before your request is approved by the powers that be. Once this is done a button will appear saying **Launch Desktop**
7. WELCOME TO RIVANNA -- Congratulations, you are now interacting with the super computer!.


## Part 2. Using the GUI (graphical user interface) to facilitate my coding.

 You may have noticed after logging in that Rivanna provides you a nice GUI for you to interact. In our case, we blew pass that, straight to the command line. But you can actually use your GUI to navigate your coding experience. 

I did not introduced this right away because there is actually some nuance to using the GUI file navigator.  You can click in the computer or the folder icon and it will open a file navigator showing the contents of you home folder. 

### How do I navigate to my other folders (e.g., /scratch)? 
To do this look at the menu bar of the top of file browser and click on the button that says **GO**. From the drop down menu choose the option **Location... (Crtl + L)**. This will enable a type in bar: in that bar now type:
```
/scratch/<< your user name >>
```
For example
```
/scratch/abc123
```
Then press enter... and voila! you now are at your folder of interest. I hope that of the lessons you are learning here is that all those fancy GUIs in your computer are simply running regular commands like "cd" on the backend. Feel free to try this to move around your folders...

### you probably want to create bookmarks
This will help you get to and from folder faster. There is an option to create bookmarks in the top menu of the file browser.
