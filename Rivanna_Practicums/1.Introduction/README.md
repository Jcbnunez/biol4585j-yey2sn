# A Primer on Bioinformatics and Rivanna

**NOTE:** This step-by-step by guide contains assignments interspersed across the text. Read carefully and ask questions during class to make sure you get all the allocated points.  In total you can expect 25 points per class from these coding assignments of quizzes. 

## Part 1. How to log into Rivanna. 

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

## Part 2.  Interacting with the super computer

### Now that we are connected to Rivanna, lets learn some basics:
In order to "talk to the super computer" you must click on ther MATE terminal icon on the top bar of the screen. Once you click on it a "black box" with the word "**bash**" will open up. YOU ARE READY TO GET CODING!

### Talking to the computer... well... making the computer talk to you
Lets type our first command:

```{sh}
echo "hello world"
```
In this case the command **echo** will tell the computer to, literally, echo whatever is inside the quotes. Give it a try.  --- can you make it echo "hello << your name >>"?

### Understanding your location in the supercomputer
While existing in the ether of information, the supercomputer is pretty much a real place, and as a user you can move to different folders or partitions (given you have the right permissions) to execute code. This is pretty much similar to the way your computer operates: there are root folders which contain sub-folder, etc, etc... you move inside the supercomputer by moving in and out of folders. 

Remember, in Rivanna, you are always inside some folder and whatever command you type may or may not affect all the files inside the folder you are inhabiting. For example, **echo** doesn't do anything to files, but you can imagine there are command that can delete all your work in a milisecond! My point is, be mindful of what you code, and where you code it!

In order to know where you currently are type:

```
pwd
```
the command **pwd** will *print the working directory*  and will reveal where you are in rivanna. In this particular case I bet you are in your **home** directory
```
/home/yourUserName
```

## Moving into a new folder
Lets go somewhere new now. Lets go to the folder of our class. You can move to a new folder using the command
```
cd << new  place >>
```
or more specifically
```
cd /project/biol4585j-yey2sn
```
Notice that in this case **/project/biol4585j-yey2sn** is the address where our class lives. you will have to type this every time you want to go to our class workspace. 

Now that you are in our class folder, lets investigate the contents of the folder. you can do this using the commnad

```
ls
```

Try it out!

Ok, let go to a different place altogether. This time around we want to go to a special folder called **scratch**. 
```
cd /scratch
```
**Yes, you will need the "/" to travel around, just typing cd scratch wont work!**

## Work spaces in Rivanna
Up to this point we have been to three folder, or spaces, in Rivanna:
1. /home
2. /project/biol4585j-yey2sn
3. /scratch

The question is: what exactly are these folders? and when will I work on these? -- lets cover some grounds rules here:

### /home
Home is basically a welcome space that Rivanna creates for you as a landing page when you log into the supercomputer. Generally speaking we wont do any coding here. We wont create folder or files here. We wont run analysis here. If Rivanna were to be a hotel, think of /home as the welcome lobby. Lets be good guests and not disturb the public lobby. You can run code here.. but you should not!

### /project/biol4585j-yey2sn
This is a folder which I manage and contains most, if not all, of the course materials. This is a space that **I** will use to share files with you, so that you don't have do download anything and to ensure we are all using the most updated files at all time. You wont run programs or create folder here.. unless I tell you otherwise. You can run code here.. but you should not!

### /scratch
Exactly as it sounds, this is your code play ground! You may code here, run commands here, create folders and files. Just have fun! -- I bet this is the space where you would be spending most of your time during the class. 

I would like for you to commit to memory the following chain of events to do for these two weeks. **Log in to rivanna --> cd /scratch** ... yep. thats it.
  
## Creating new folders
I want you to be aware that, over the next two weeks, we will be running many many analysis. The inevitable result of this is that you will generate a lot of files. And, trust me, if you plan on a strategy to be tidy, your scratch will get messy real quick... and you wont be able to find your stuff... 

A good strategy to mitigate this is to create folder, with informative names, that help you find your files in a timely and orderly fashion. Lets create our first folder with the command
```
mkdir my_first_folder
```
In this case the command is **mkdir** and you are creating a folder named **my_first_folder**. Also, notice that spaces " " will not be used used as part of our code. Instead we will replace all spaces with "_" symbols. So instead of "my_first_folder" we must write "my_first_folder". This is **KEY** becuase spaces " " can mess up code real bad! and we dont want that.. do we?
 
## Part 3. Exploring and copying files around

### Move into your new folder
We first want to move into our new folder  "my_first_folder":
```
cd my_first_folder 
``` 

### Copy a file to your folder
Now lets copy a file from the class folder to our folder
```
cp /project/biol4585j-yey2sn/Files/Day_1/Mus.sequence.fasta ./
```
In this case the command is "cp". cp takes 2 arguments:
1. --> /project/biol4585j-yey2sn/Files/Day_1/Mus.sequence.fasta ... and 
2. --> ./

The first argument,  "/project/biol45...etc" is the file that you want to copy, and the second "./" is where you want to copy it. In **Rivanna the term "./" simply means "here"...** read that as "./" means whenever I happen to be (think of pwd...).

### Check if your file is in the folder
Type:
```
ls
```
Do you see your file?

### Explore properties of the file:

* File Size

We can learn about file sizes by using a special option of the command "ls". This is the options `-l` and `--block-size=M` . NOTICE: this is a **global command** that will give you the file size for all files inside the folder you happen to be in.

```{bash}
ls -l --block-size=M
```
*Quiz question: How big is the file?* **X points**

* File Length

We can learn how many lines of text are contained in the file by using
```
wc -l Mus.sequence.fasta
```
NOTICE: `wc -l` is a **specific file command** (i.e., not a global one). specific command expect that you will indicate a *specific file* in which to act. in this case we are asking Rivanna to count the number of lines of the file `Mus.sequence.fasta`

*Quiz question: How many lines are there in the file?* **X points**

* Exploring the head and tail of a file.

Most times that we interact with a file in a computer, files are small (less than 500 Mb) and we can easily explore them by eye. Imagine you have a giant genome file that is >>5 GB or larger... you wont event be able to open the file to inspect by eye. So we need to use tricks to do quick exploration of our files. One trick is to just show the top "n" lines of a file.
For example a command to see just the first 10 lines of a file.
```
head -n 10 Mus.sequence.fasta
```
What is the console showing you?

*Quiz question: The command `tail` is the reciprocal of `head`, i.e., shows the last "n" lines of a file. Can you infer how would the command to show the last 15 lines of our file? (it is not a trick question, it is probably as simple as you think it is...)* **X points**

### Finding patterns in a file and creating a new file:
One staple of bioinformatic files is that they are arcane and jammed packed with all sorts of data of biological interest. One core challenge of any bioinformatician is how to extract data from files of any size.. from 10Mb to 1Tb!. One easy way to do this is by using the command `grep`.

#### Basic grep structure 
```
grep "<<key word>>" file
```
for example, the file that we have been working with `Mus.sequence.fasta` is whats known as a fasta file (we will learn more about these tomorrow). Generally speaking, fasta files are universal files used to store DNA or RNA information. Because they are "universal" they have some regular aspects that we can leverage to do "data mining". For example: fasta files separate diffent sequences by the use of the symbol "**>**"... that means that a file were the character ">" is present 5 times has 5 DNA/RNA sequences.  

Lets use this knowledge. Lets say that you are only interested in the name of DNA sequences, but you don't really care about the sequence itself. How could you simply extract the DNA names. Lets try:

```
grep ">" Mus.sequence.fasta

# Remember we are using ">" as our key word because we know
# that fasta files use > to indicate DNA/RNA names

# Also, notice that I wrote this text using a "#" symbol.
# In the super computer the "#" symbol means "this line is just text"
# The supercomputer will treat this as simple text, not code
# This is used to annotate code
``` 
What do you see?
*Quiz question: How many DNA/RNA sequences are on file?* **X points**
*Quiz question: What is the model organism from which these sequences come from?* **X points**

#### Creating a new file
lets say that you want to create a brand new file that only contains the header names. you can do this by modifying our earlier command.

```
grep ">" Mus.sequence.fasta > justheaders.txt
```
In this case you are using the unix command `>` to save the output of this command to a file named `justheaders.txt`.

**THIS IS CONFUSING!!**: uh oh! we have encounter the first point were most first-time bioinformaticians get confused. How come that we are using `">"` as the key word of grep, but also, at the same time, we are using `>` (notice that there are no quotes!) to save new files! The reason for this comes from the fact that these two symbols are changing meaning as a function of their position in the code. the `">"` is acting as the argument of the grep command and it is related to the properties of the fasta file. On the other hand, the `>` (no quotes) is an internal command of the operating system that means **save to**.  I know this is can be confusing at first, but don't get discouraged by this. Also, don't worry we wont use too many if these confusing cases in the class... but you should know that these exists... and are actually very common...  The reality is that coding can sometimes be confusing like this and it is just a matter of being careful and paying attention when we code. :) You can do this!!

## Coding challenge (part of the quiz):
As we just explored above, the grep command is a powerful way to mine for data. In our case,  the command `grep ">" Mus.sequence.fasta > justheaders.txt` you could verbally reads this command out loud as: *hey Rivanna, please find (`grep`) all lines with the symbol `">"` in the file `Mus.sequence.fasta` and save it to (`>`) the new file `justheaders.txt`*. The power of commands like grep is that you can use options (sometimes called "flags") to change entire behaviors of the function. For instance, just by adding the flag `-v` the command becomes "find everything that DOES NOT contain a given symbol".  As such:

```
#find all lines containing the ">" symbol
grep ">" Mus.sequence.fasta 

#vs

#find all lines NOT containing the ">" symbol
grep -v ">" Mus.sequence.fasta 
```
#### What is the challenge? -->  (X points)
Your challenge is to create a file named  "noheaders.<< your name >>.txt". This is a file that contains only the DNA/RNA sequence of `Mus.sequence.fasta`. After creating this file I want you to **copy** this file to your **Homework_Drop_off** (this is a folder located at `/project/biol4585j-yey2sn/Homework_Drop_off/<< your name >>`). That's it.

To recap, to complete this you have to:

1. run reversed grep (`grep -v`) on Mus.sequence.fasta 
2. save the reversed grep output to a file named `noheaders.yourName.txt`
3. copy (`cp`) this file to the homework drop off folder.
4. Deadline: I will grade this assignment before the end of the day. 

#### How can I learn more about the "flags" of grep (and other functions)
Great question! you can learn a lot about various fucntions by running:
```
man grep
```
more generally
```
man << function >>
```
Give it a try...

## Part 4. Using the GUI (graphical user interface) to facilitate my coding.

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


## Part 5. Introduction to R (a statistical analysis framework).
This is the last thing we will do today. Before we dive into some code lets cover some basics. Up to this point we have been coding in Rivanna itself. In other words we have been talking directly to the supercomputer. A big part of bioinformatics and genomics is to do statistical analysis of DNA sequences. The programming language "R" is famous for having a lot of statistical tools at our disposal. Because of this we will choose to do our statistics in R as opposed to on Rivanna directly. To accomplish this we have to run R on top of Rivanna. I know this can be confusing, we are running Rivanna on top of our computers and then R on top of Rivanna. 

### How to run a program within Rivanna
In order to do this we have to first load the program itself and all its dependencies. In Rivanna we call this to "load of module", or `module load`:

```
module load intel/18.0 intelmpi/18.0
module load goolf/7.1.0_3.1.4
module load gdal proj R/4.0.0
# ^ These are all the modules needed to run R in Rivanna
```   
Now that we have loaded the modules lets activate `R`. This is done by simply typing:

```
R
```
### Am I inside R or... am I still in Rivanna
You can differentiate these by the prompt you get in your console.
Generally speaking you know you are in Rivanna if the console reads:
```
-bash-4.2$
```
Generally speaking you know you are in R if the console reads just:
```
>
```
**IT IS CONFUSING, AGAIN:** *I know, I know,* yet again.... we find the `>` symbol meaning something completely different. In this case `>` has a different meaning because we are no longer in Rivanna, per se, but rather inside R.

### What is different in R vs Rivanna (unix)?
The short answer is pretty much everything. To be clear the commands we just practiced `echo, cd, pwd, grep` work in Rivanna, but they wont work inside R. In actuality, you will find yourself jumping between coding in R and coding in Rivanna (generally speaking Rivanna is a Unix system)... so you will jump between R and Unix. 

### Why R ?
The power of R lies in in libraries. Basically there is a large community of scientists who actively develop libraries in R to do a variety of fancy statistical analysis. As of ~2020 there are an estimated 10,000 libraries in circulation (see [https://cran.r-project.org/](https://cran.r-project.org/) and [https://www.bioconductor.org/](https://www.bioconductor.org/)). As you may imagine you dont need all the packages all the time, so R allows you to only load the packages that you need, or want. Lets load some packages:
```
library(tidyverse, lib.loc = "/project/biol4585j-yey2sn/R/4.0/")

## Notice that the option lib.loc is only required because
## we are using an educational partition. 
## In most super-computers or personal-computers simply
## typing library(tidyverse) will do the trick.
```
### The Tidyverse
The tidyverse is the colloquial name given to a broad suite of R libraries and packages designed to drastically improve the user experience in R and ensure that our analysis pipelines can be easily replicated. We don't have time to do a deep dive into this library but you can learn more about it [here](https://www.tidyverse.org/). 

## The Iris flower datasets

For our first biological analysis (and chance to learn R) we are going to use the  famous (Fisher and Anderson) iris data set. This dataset gives the measurements in centimeters of the variables sepal length and width and petal length and width, respectively, for 50 flowers from each of 3 species of iris. The species are _Iris setosa_,_versicolor_, and _virginica_.

![Three species of Iris flowers](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Rivanna_Practicums/1.Introduction/Figures/iris-machinelearning.png)
[Figure from data camp](https://www.datacamp.com/community/tutorials/machine-learning-in-r)

### Source of the Iris datatset
You can type
```
?iris
```
for more details

* Fisher, R. A. (1936) The use of multiple measurements in taxonomic problems.  _Annals of Eugenics_,  **7**, Part II, 179–188.

* The data were collected by Anderson, Edgar (1935). The irises of the Gaspe Peninsula,  _Bulletin of the American Iris Society_,  **59**, 2–5.

