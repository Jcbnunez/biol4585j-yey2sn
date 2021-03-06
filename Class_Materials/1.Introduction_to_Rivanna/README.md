# A Primer on Bioinformatics and Rivanna

## Part 1.  Interacting with the super computer

In order to "talk to the super computer" you must click on ther MATE terminal icon on the top bar of the screen. Once you click on it a "black box" with the word "**bash**" will open up. YOU ARE READY TO GET CODING!

### Talking to the computer... well... making the computer talk to you
Lets type our first command:

```{sh}
echo "hello world"
```

#### Supercomputers are **CASE SENSITIVE**. echo =/= Echo =/= ECHO.

In this case the command **echo** will tell the computer to, literally, echo whatever is inside the quotes. Give it a try.  --- can you make it echo "hello << your name >>"?

## Part 2. Understanding your location in the supercomputer
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
cd /scratch/"username"
```
**Yes, you will need the "/" to travel around, just typing cd scratch wont work!**

## Part 3. Know our core work spaces in Rivanna

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

I would like for you to commit to memory the following chain of events to do for these two weeks. **Log in to rivanna --> cd /scratch/username** ... yep. thats it.
  
## Part 4. Creating new folders in Rivanna

I want you to be aware that, over the next two weeks, we will be running many many analysis. The inevitable result of this is that you will generate a lot of files. And, trust me, if you plan on a strategy to be tidy, your scratch will get messy real quick... and you wont be able to find your stuff... 

A good strategy to mitigate this is to create folder, with informative names, that help you find your files in a timely and orderly fashion. Lets create our first folder with the command
```
mkdir my_first_folder
```
In this case the command is **mkdir** and you are creating a folder named **my_first_folder**. Also, notice that spaces " " will not be used used as part of our code. Instead we will replace all spaces with "_" symbols. So instead of "my_first_folder" we must write "my_first_folder". This is **KEY** becuase spaces " " can mess up code real bad! and we dont want that.. do we?
 
## Part 5. Exploring and copying files around

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

## Part 6. Explore properties of the file:

* File Size

We can learn about file sizes by using a special option of the command "ls". This is the options `-l` and `--block-size=M` . NOTICE: this is a **global command** that will give you the file size for all files inside the folder you happen to be in.

```{bash}
ls -l --block-size=M
```
*How big is the file?* 

* File Length

We can learn how many lines of text are contained in the file by using
```
wc -l Mus.sequence.fasta
```
NOTICE: `wc -l` is a **specific file command** (i.e., not a global one). specific command expect that you will indicate a *specific file* in which to act. in this case we are asking Rivanna to count the number of lines of the file `Mus.sequence.fasta`

*How many lines are there in the file?* 

* Exploring the head and tail of a file.

Most times that we interact with a file in a computer, files are small (less than 500 Mb) and we can easily explore them by eye. Imagine you have a giant genome file that is >>5 GB or larger... you wont event be able to open the file to inspect by eye. So we need to use tricks to do quick exploration of our files. One trick is to just show the top "n" lines of a file.
For example a command to see just the first 10 lines of a file.
```
head -n 10 Mus.sequence.fasta
```
What is the console showing you?

*The command `tail` is the reciprocal of `head`, i.e., shows the last "n" lines of a file. Can you infer how would the command to show the last 15 lines of our file? (it is not a trick question, it is probably as simple as you think it is...)* 

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
*How many DNA/RNA sequences are on file?* 
*What is the model organism from which these sequences come from?* 

## Part 7. Creating a new file
lets say that you want to create a brand new file that only contains the header names. you can do this by modifying our earlier command.

```
grep ">" Mus.sequence.fasta > justheaders.txt
```
In this case you are using the unix command `>` to save the output of this command to a file named `justheaders.txt`.

**CONFUSING!!**: uh oh! we have encounter the first point were most first-time bioinformaticians get confused. How come that we are using `">"` as the key word of grep, but also, at the same time, we are using `>` (notice that there are no quotes!) to save new files! The reason for this comes from the fact that these two symbols are changing meaning as a function of their position in the code. the `">"` is acting as the argument of the grep command and it is related to the properties of the fasta file. On the other hand, the `>` (no quotes) is an internal command of the operating system that means **save to**.  I know this is can be confusing at first, but don't get discouraged by this. Also, don't worry we wont use too many if these confusing cases in the class... but you should know that these exists... and are actually very common...  The reality is that coding can sometimes be confusing like this and it is just a matter of being careful and paying attention when we code. :) You can do this!!

## Part 8. Coding challenge (10 points):

As we just explored above, the grep command is a powerful way to mine for data. In our case,  the command `grep ">" Mus.sequence.fasta > justheaders.txt` you could verbally reads this command out loud as: *hey Rivanna, please find (`grep`) all lines with the symbol `">"` in the file `Mus.sequence.fasta` and save it to (`>`) the new file `justheaders.txt`*. The power of commands like grep is that you can use options (sometimes called "flags") to change entire behaviors of the function. For instance, just by adding the flag `-v` the command becomes "find everything that DOES NOT contain a given symbol".  As such:

```
#find all lines containing the ">" symbol
grep ">" Mus.sequence.fasta 

#vs

#find all lines NOT containing the ">" symbol
grep -v ">" Mus.sequence.fasta 
```
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

#### What is the challenge?
Your challenge is to create a file named  "noheaders.<< your name >>.txt". This is a file that contains only the DNA/RNA sequence of `Mus.sequence.fasta`. After creating this file I want you to **copy** this file to your **Homework_Drop_off** (this is a folder located at `/project/biol4585j-yey2sn/Challenge_Drop_off/<< your name >>`). That's it.

To recap, to complete this you have to:

1. run reversed grep (`grep -v`) on Mus.sequence.fasta 
2. save the reversed grep output to a file named `noheaders.yourName.txt`
3. copy (`cp`) this file to the homework drop off folder.
4. Deadline: I will grade this assignment before the end of the day. 

## Part 9. Where are all the DNA data?
DNA sequences are kept in a a centralized repository maintauined by the NIH called "The National Center for Biotechnology Information" (NCBI), a part of the United States National Library of Medicine (NLM). Lets spend the last portion of the class exploring this repository: [https://www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/).
