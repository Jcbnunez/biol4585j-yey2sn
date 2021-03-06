# biol4585j-yey2sn
Material for the course UVA biol4585j (Evolutionary Genomics)


## How to log into Rivanna. 

### Check out the [Video Tutorial](https://youtu.be/_kpRgRpGMXo)

**NOTE:** To access Rivanna you must use **on-grounds** wifi (e.g., **_eduroam_**) or ethernet. If you want to access Rivanna off-grounds you will need to use [UVA's VPN](https://virginia.service-now.com/its/?id=itsweb_kb_article&sys_id=f24e5cdfdb3acb804f32fb671d9619d0)

1. Type [https://_rivanna_-_portal_._hpc_.virginia.edu](https://rivanna-portal.hpc.virginia.edu) into your web browser. This will automatically trigger a UVA authentication step. Input your UVA credentials to enter the super-computer GUI.
2. Once inside you will see a "Message of the day board". Go to the top bar and search for the option "**Interactive Apps**".
3. Once you click **Interactive Apps** a drop down menu will appear. Click on the option names **Desktop**. 
4. Clicking on Desktop will give you the option to create an interactive session with the supercomputer. Before you can do that you need to tell the supercomputer what are the parameters of your interactive session. These are:
	```
	Rivanna partition: --> select "instructional"
	Number of hours: --> 6
	Number of cores:--> 3 
	Memory Request in GB:--> 24
	Allocation (SUs): --> leave empty
	Optional: GPU type for GPU partition**: --> leave empty
	Optional: Slurm Option: --> --reservation=biol4585
	Optional: Group: --> write biol4585j-yey2sn
	```
5. Once you have these entered these options go ahead and press **LAUNCH**
6. It may take a couple seconds to a minute before your request is approved by the powers that be. Once this is done a button will appear saying **Launch Desktop**
7. WELCOME TO RIVANNA -- Congratulations, you are now interacting with the super computer!.
