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
cd /scratch
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

I would like for you to commit to memory the following chain of events to do for these two weeks. **Log in to rivanna --> cd /scratch** ... yep. thats it.
  
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

## Part 8. Coding challenge (part I of the quiz):

As we just explored above, the grep command is a powerful way to mine for data. In our case,  the command `grep ">" Mus.sequence.fasta > justheaders.txt` you could verbally reads this command out loud as: *hey Rivanna, please find (`grep`) all lines with the symbol `">"` in the file `Mus.sequence.fasta` and save it to (`>`) the new file `justheaders.txt`*. The power of commands like grep is that you can use options (sometimes called "flags") to change entire behaviors of the function. For instance, just by adding the flag `-v` the command becomes "find everything that DOES NOT contain a given symbol".  As such:

```
#find all lines containing the ">" symbol
grep ">" Mus.sequence.fasta 

#vs

#find all lines NOT containing the ">" symbol
grep -v ">" Mus.sequence.fasta 
```
#### What is the challenge? -->  (5 points)
Your challenge is to create a file named  "noheaders.<< your name >>.txt". This is a file that contains only the DNA/RNA sequence of `Mus.sequence.fasta`. After creating this file I want you to **copy** this file to your **Homework_Drop_off** (this is a folder located at `/project/biol4585j-yey2sn/Challenge_Drop_off/<< your name >>`). That's it.

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

## Part 9. Introduction to R (a statistical analysis framework).
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
Generally speaking you know you are in **Rivanna** if the console reads:
```
-bash-4.2$
```
Generally speaking you know you are in **R** if the console reads just:
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
## Part 10. The Tidyverse
The tidyverse is the colloquial name given to a broad suite of R libraries and packages designed to drastically improve the user experience in R and ensure that our analysis pipelines can be easily replicated. We don't have time to do a deep dive into this library but you can learn more about it [here](https://www.tidyverse.org/). 

### The Iris flower datasets

For our first biological analysis (and chance to learn R) we are going to use the iris data set. This dataset gives the measurements in centimeters of the variables sepal length and width and petal length and width, respectively, for 50 flowers from each of 3 species of iris. The species are _Iris setosa_,_versicolor_, and _virginica_.

![Three species of Iris flowers](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Rivanna_Practicums/1.Introduction/Figures/iris-machinelearning.png)
[Figure from data camp](https://www.datacamp.com/community/tutorials/machine-learning-in-r)

### Learn more about this of the Iris datatset
You can type
```
?iris

# In R, you can learn more details about a package or function by using the ? commmand
```
**what is going on here??** By typing `iris` we are summoning an object with data that is preloaded into R. Basically `iris`  = our data! In future classes we will learn how to make our own objects!

For more details on the data see:

* The data were collected by Anderson, Edgar (1935). The irises of the Gaspe Peninsula,  _Bulletin of the American Iris Society_,  **59**, 2–5.

## Exploring data in R & using pipes (%>%) to execute functions
Similar to Rivanna (Unix) we can use exploratory commands to get a sense of what the data looks like. 

**NOTE**: `library(tidiverse , lib.loc = "/project/biol4585j-yey2sn/R/4.0/"` must be activated for any of this code to work. 

### See the first N colums of iris
```
iris %>% head(n=10)
```
**what is going on here??** R-tidyverse has a funky way of doing code, but I promise, it is actually very intuitive. In this language you can code by "piping" `%>%` data into commands to get desired outputs. In our case here, the code, `iris %>% head(n=10)`, can be read out loud as" *to the data, `iris`, apply `%>%` the head `head(n = 10)` command*.

**how many pipes can I use?** As many as you like. For example you could get the "tail of the head". E.g., `iris %>% head(n = 20) %>% tail(n = 10)`. This is an example command chain (taking the first 20 lines of iris and the taking the last 10 lines ... of the first 20 lines). But I hope it shows the power of pipes in R. 

**What is the directional of pipes?** While very flexible, pipes do have directionality. That is to say, the data always comes first, then the functions... (not the other way around). `iris %>% head(n=10)` **is correct**. On the other hand `head(n=10) %>% iris` **is incorrect!**

**What is up with head(n = 10)?** Wait a minute! didn't we just learn that the `head` command used "flag arguments" `head -n 10`? Why are we seeing `head(n = 10)`? The answer is simple: `head -n 10` is the **UNIX (Rivanna)** language, whereas `head(n = 10)` is the **R ** language. While in unix functions take arguments using flags separated by spaces "-x -n -k", in R functions take arguments inside parenthesis and are often separated by commas. Example `head(n = 10)`. In this class you will have to wire your brain to being bilingual, but, instead of English, Spanish, or French, our languages are going to be unix and R. 

## Part 12. Moving around Rivanna while inside of R
To move around the supercomputer you can use commands:
```
getwd()  #---> this is the same as pwd in unix
setwd("./<< address >>") #--> this is the same as cd ./<< address >> in unix
```
**A core difference between Rivanna (unix) and R** is that, while in Rivanna you can provide addresses as simnple text `./some/place/here`,  **in R** you have to give addresses in quotes `"./some/place/here"`.

## Part 13. Filtering data in R 
Ok, now we are going to start to data mine our iris dataset. Lets explore some filtering options

### How many colums and rows do we have?
```
iris %>% dim

# dim outputs 2 values: the number of rows and the number of columns
```
### What are the names of the columns?
```
iris %>% names

# names will provide you with the names of all the columns in the dataset
```
### How to select columns of interest? (Pipes in action)
Lets say that you are interested in just seeing the "Sepal.Length" column. You can do this by:
```
iris %>% select(Sepal.Length)
```
This outputs a the entirety of the column. Lets say that you want to select "Sepal.Length" but only see the first 10 lines.
```
iris %>% select(Sepal.Length) %>% head(n = 10)

# Now we are seeing pipes in action!
```  
### How to select columns of interest *and* save it to a new data object?
for our next task we will do a double take! we will select TWO columns and then we will save these to a brand new object.
```
iris %>% select(Sepal.Length, Species) -> newIris
```
**what is going on here??** Here, we are taking the data set `iris`, from it we are selecting two columns `select(Sepal.Length, Species)` and then we are saving the output of the pipe ` -> ` to the object `newIris`.  (**WARNING:** never save a *modified* object into the *original* object. example: `iris %>% head -> iris` **This is a terrible idea!!** ) Can you guess why? Again, this is something that you *can* do... but you definitely *should not* do.
Lets look at our new object:
```
newIris %>% head
```
### PROTIP: you can make your code look pretty and tidy :)
You make your code look pretty by using the "enter" key (formally called the carriage return) in between your pipes and your pipe save. Returns always go after the pipe or pipe termination symbol.
Example:
```
iris %>%    
select(Sepal.Length, Species) -> 
newIris

#Notice how you can press enter after the pipe "%>%" and the pipe save "->"
#isn't coding just wonderful![?] .... I think so anyway :)
```

### How do we filter data by observations?
Lets say you are interested in just some subset of observations. For example, you only want to retain only observations  in which `Sepal.Width ` is larger than 3.1. We can do this easily with `filter`
```
iris %>%    
filter(Sepal.Width > 3.1) 

# Notice that in this case > is being use in it orginal form as the logical operator greater than!
# Note: How many times have we encountered > having differnt meanings? 
# A lot..
# why computer programmers are obsessed with the > symbol is a mistery!
```
*how many observation have Sepal.Width > 3.1*  (hint you can pipe the code to dim `%>% dim`)
*how many observation have Sepal.Width > 3.4*  
*how many observation have Sepal.Width < 2.7*  

**Math and logical operators in R** *your most powerful tools for data mining!* 

| Arithmetic Operator    Description                 	|
|-----------------------------------------	|
| +        addition                       	|
| -        subtraction                    	|
| *        multiplication                 	|
| /        division                       	|
| ^or**    exponentiation                 	|
| x%%y    modulus    (x mod y) 5%%2 is 1  	|
| x%/%y    integer    division 5%/%2 is 2 	|

###
|Logic Operator     Description        	|
|---------------------------------	|
| <     less than                 	|
| <=     less than or equal to    	|
| >     greater than              	|
| >=     greater than or equal to 	|
| ==     exactly equal to         	|
| !=     not equal to             	|
| !x     Not x                    	|
| x \| y     x OR y               	|
| x & y     x AND y               	|
| isTRUE(x)     test if X is TRUE 	|

## Part 14. How do we filter for multiple conditions?
```
iris %>%    
filter(Sepal.Width > 3.1 & Petal.Width < 1.5 & Species != "setosa") 

# In English we would say:
#filter Sepal.Width > 3.1 AND Petal.Width < 1.5 AND Species IS NOT "setosa"
```
*how many observation have Sepal.Width > 3.3 and Petal.Width < 0.5*  

## Adding new columns to a data object 
Ok, you can filter exisitng data! But can you create new data in your data object? Yes you can, and here is how:
```
iris %>%    
mutate(NewCol = "this_is_new")


# You have used the function mutate add a new column!
# Generally this works by:
# mutate(NewColName = << data for new column >>)
```
Ok, but that is kinda lame because we just "spammed" the phrase `this_is_new` in our data object. This is not very useful.. right?

Well, lets say that I want to add a new column called `isFavorite`. Basically if the species is my favorite, I will say `Yes`, otherwise `No`. We can do this by **nesting** the `mutate` and `case_when` commands! Like so:
```
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",) )

# In this case. I am asking R to write Y for my favorite species, versicolor.  
```
**what is going on here??** Ok, a lot of things are happening here! Lets walk through them. First thing you are doing is piping the data `iris` to a `mutate` command to create a new column. However, **inside** the `mutate()` function you are **nesting** the `case_when()` function.

**case_when()** is a very powerful function that aks R to evaluate whether or not a condition is true and then react accordingly (`Species == "versicolor"`). In this case the reaction (`~`) is to print the word "Yes" or "No". When combined with the function `mutate` it creates a column of "Yes" or "No" as the new column.

## Part 15. Summarizing data
Now that we are masters of data exploration and manipulation. We can start asking questions about the data. We will start by asking trivial questions about  the data, but we will eventually move into more interesting biological questions. 
The first thing we need in order to summarize data is **grouping variable**. A grouping variable is basically some aspect of the data that we can use to partition the data. For example, lets partition the data based on whether or not a given species is my favorite or not. We will accomplish this by using the command `group_by()` 
```
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",)) %>%
group_by(isFavorite) 
```
**what is going on here??** So far, not much has happened in the front-end. In the back-end, however, as long as you continue to pipe the `group_by` function, R will group the data according to the contents of the  `isFavorite ` column. It is important to know that the grouping variable has to exists in the data, for example, if you use `select()` to pick a couple columns and by doing this you end up removing your grouping column, `group_by()` wont work!. So be careful when you code. 

### Count the number of species which are, and are not, my favorites:
We can count the number of observations which have Yes or No in the `isFavorite` by nesting two functions `summarize()` and `n()`.  **summarize** is a powerful function that will apply any function to your data. However, by this is not done globally, instead this is done within the groups of the grouping variable (for example, all the Yes, and all the No). On the other hand `n()`, the function inside, will count the number of observation in each group.  
```
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",)) %>%
group_by(isFavorite) %>%
summarize( n() )
```
### Estimate the mean and standard deviation of the Sepal.Length, as a function of my favorites

**Need a reminder about what _means_ and _standard deviations_ are? [check this video tutorial (by Josh Starmer)](https://youtu.be/SzZ6GpcfoQY)**

Lets expand on our code above to do more stuff! For example, lets estimate both the mean and standard deviation of `Sepal.Length` for both my favorite and non-favorite samples. As I mentioned, instead of changing the code, we are going to build on it by adding more arguments to the `summarize()` function. We can do this by using commas `,`.
**Stats Functions:** in R you can estimate means using `mean()` and standard deviations using `sd()`.
```
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",)) %>%
group_by(isFavorite) %>%
summarize(n(), mean(Sepal.Length), sd(Sepal.Length) )

#You should see a table with all this data!
#  isFavorite `n()` `mean(Sepal.Length)` `sd(Sepal.Length)`
# <chr>      <int>                <dbl>              <dbl>
# No           100                 5.80              0.945
# Yes           50                 5.94              0.516
```
### Can we make this code prettier and neater? 
As we continue to code our analysis, you will soon notice how our code starts growing and growing. And it may turn into a chunk of text that is difficult to keep track of. Earlier on we learned a trick  where you can use "enter" after pipes to stream-line the code. In addition to pipes (`%>%` and `->`), you can use this trick also for commas `,` and other elements within functions.  Applying this trick to our code makes now look more organized:

**ITS YOUR CHOICE:** if this process of tidying up your code is too confusing or if it has the tendency to break your code, you can chose not to use it. Use as much or as little tidiness as you like. **Our priority is simply to make our code work!!**

### Tip 1: use your spaces strategically
```
iris %>%    
mutate(isFavorite = case_when(	

Species == "versicolor" ~ "Yes", 
Species != "versicolor" ~ "No",)  ) %>%

group_by(isFavorite) %>%
summarize(  
n(), 
mean(Sepal.Length), 
sd(Sepal.Length) )
```
Notice that **this code is exactly the same as the one above** it simply uses spacing as a way to make the code more legible and easy to follow. 

### Tip 2: provide output names to the summarize() function
Another way to make both the code and the output easier to add your own names to the summarize function. Right now, we are simply using the default behavior in that outputs the names of the functions as the column names. This looks like   `'n()'` `'mean(Sepal.Length)'` `'sd(Sepal.Length)'` . This can get clunky really quickly, so we can provide R our own output names. See the code below
```
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",)) %>%
group_by(isFavorite) %>%
summarize(  
N = n(),                       # Notice we have added the name N =
MEAN = mean(Sepal.Length),     # Notice we have added the name MEAN =
SD = sd(Sepal.Length) )        # Notice we have added the name SD =

# This outputs a much neater output:
#  isFavorite   N  MEAN    SD
# <chr>      <int> <dbl> <dbl>
# No           100  5.80 0.945
# Yes           50  5.94 0.516
```

## Part 16. Visualizing the data using _ggplot_
The last exercise we hope to accomplish is to make a graph showcasing our analysis. Data visualization is a fundamental part of genomics and data science. 
First thing we need to do is to save our summarize pipe into a new object. Lets call it `MyFavoriteIrisFlowers` 
```
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",)) %>%
group_by(isFavorite) %>%
summarize( N = n(), MEAN = mean(Sepal.Length), SD = sd(Sepal.Length) ) ->
MyFavoriteIrisFlowers   
```
All the data that we need is now consolidated in `MyFavoriteIrisFlowers`. 
### Using ggplot to visualize data.
The R library _ggplot_ is perhaps on of the most famous libraries among data scientist. Ggplot provides a unified set of graphical tools to visualize your data. 

#### Ggplot works like a canvas
As a graphical tool, ggplot has rules of its own that we need to understand. Any ggplot figure is built using three sets of components: 1. Data + 2. Aesthetic map + 3. Elements. Here is an example: 

![ggplot basics](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Rivanna_Practicums/1.Introduction/Figures/ggplot_basics.wb2.png)
**Data**: This is the data object would would like to base your figure on. Pass your data into ggplot by pipping it into `ggplot`

**Aesthetic map**: This is. the first function of any ggplot. This part generally always looks the same `ggplot(aes(..))`. it is a nested function of `ggplot()` and the `aes()` function. While technically different functions, for the purposes of this class, you can think for  `ggplot(aes(..))` as a single function. Now inside that function we get to put in what we want the actual data to be. For example `x=` , `y=` will define what data will go into the x and y axis.

**Elements**: This is the bread and butter of ggplot. You can add different types of figures to your plot. **Given that they are compatible with your data, of course!** Some examples are: `geom_point()`, `geom_errorbar()`. We will learn different elements as we progress in the class. A key thing to know is that you add elements to your plot using the `+` symbol (you can press enter after every `+`). 

Lets see an example:
```
MyFavoriteIrisFlowers %>%
ggplot(aes(x=isFavorite, y=MEAN)) +
geom_point(size = 3) -> just_point

#this will generate a "plot" point showing our data. geom_point only requires x and y data.

#save your plot
ggsave(just_point, file = "just_point.pdf", width = 6, height = 4)

#check your plot using your browser GUI
```

![geom_point only](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Rivanna_Practicums/1.Introduction/Figures/point_only.png)

This plot shows the point estimates of our `summarize(MEAN = ...)` analysis. But always remember that in statisitcs, point estimates are always associated with variance (i.e., a measure of data dispersion ). In our case we can some measure of dispersion by including our estimates of standard deviation  `summarize(SD = ...)`. We can do this using the element known as `geom_errorbar()`. This element requires, on top of `x` and `y`, two additional arguments `ymin` and `ymax`. We need to add these to the **aesthetic map**.

```
MyFavoriteIrisFlowers %>%
ggplot(aes(x=isFavorite, y=MEAN, ymin = MEAN-SD, ymax = MEAN+SD)) +
geom_point(size = 3) +
geom_errorbar(width = 0.5) -> error_plus_point

ggsave(error_plus_point, file = "error_plus_point.pdf", width = 6, height = 4)

#check your plot using your browser GUI
```

![geom_point only](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Rivanna_Practicums/1.Introduction/Figures/point_plusError_only.png)

wow! look at that! our point estimates are not very different after all!

## Part 16. Recap
In today's lecture and practicum you have learned 4 core skills for bioinformatics work:

1. How to log in an interact with a supercomputer (aka **HPC**; High Performance Computer)
2. You have learned how to navigate a **Unix** system (Rivanna) and some basic file manipulations
3. You have learned how to use **R-tidyverse** to filter, manipulate, and summarize data.
4. You have learned how to visualize data using **R-ggplot**

## Part 17. Code Challenge (20 pts)

Using you knowledge of R for data manipulation generate the following graph --> A graph showing on the **x-axis** all the species contained in `iris`, on the **y-axis** showing the mean value for `Petal.Length` also include error bars showing the standard deviation. Hint: you will use `group_by()`, `summarize()`, `ggplot(aes())`, `geom_point()`, `geom_errorbar()`, among others. Submit your graph to the homework folder once you are done.


