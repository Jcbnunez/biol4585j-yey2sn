# Introduction to R (a statistical analysis framework).

In today's class we will learn how to do statistical analyses using the R programming language. Notice that, because R is an independent program, we have to run it "on top of" the base Rivanna system.

### How to run a program within Rivanna
In order to work in R  we have to first load the program itself and all its dependencies. In Rivanna we call this to "load of module", or `module load`:

```
module load gcc/7.1.0
module load openmpi/3.1.4
module load R/4.1.1
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
#Load the tidyverse package
library(backports, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
library(tzdb, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
library(withr, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
library(rstudioapi, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
library(labeling, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
library(farver, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
library(tidyverse, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")

#We will also load "ggpubr" a supporting library
library(ggpubr, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")

## Notice that the option lib.loc is only required because
## we are using an educational partition. 
## In most super-computers or personal-computers simply
## typing library(tidyverse) will do the trick.
```
## Part 1. The Tidyverse
The tidyverse is the colloquial name given to a broad suite of R libraries and packages designed to drastically improve the user experience in R and ensure that our analysis pipelines can be easily replicated. We don't have time to do a deep dive into this library but you can learn more about it [here](https://www.tidyverse.org/). 

### The Iris flower datasets

For our first biological analysis (and chance to learn R) we are going to use the iris data set. This dataset gives the measurements in centimeters of the variables sepal length and width and petal length and width, respectively, for 50 flowers from each of 3 species of iris. The species are _Iris setosa_,_versicolor_, and _virginica_.

![Three species of Iris flowers](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/2.Introduction_to_R/Figures/iris-machinelearning.png?raw=true)
[Figure from data camp](https://www.datacamp.com/community/tutorials/machine-learning-in-r)

#### Learn more about this of the Iris datatset
You can type
```
?iris

#press "q" to quit the readme

# In R, you can learn more details about a package or function by using the ? commmand
```
**what is going on here??** By typing `iris` we are summoning an object with data that is preloaded into R. Basically `iris`  = our data! In future classes we will learn how to make our own objects!

For more details on the data see:

* The data were collected by Anderson, Edgar (1935). The irises of the Gaspe Peninsula,  _Bulletin of the American Iris Society_,  **59**, 2–5.

### Exploring data in R & using pipes (%>%) to execute functions
Similar to Rivanna (Unix) we can use exploratory commands to get a sense of what the data looks like. 

**NOTE**: `library(tidiverse , lib.loc = ...)` must be activated for any of this code to work. 

### See the first N colums of iris
```
iris %>% head(n=10)
```
**what is going on here??** R-tidyverse has a funky way of doing code, but I promise, it is actually very intuitive. In this language you can code by "piping" `%>%` data into commands to get desired outputs. In our case here, the code, `iris %>% head(n=10)`, can be read out loud as" *to the data, `iris`, apply `%>%` the head `head(n = 10)` command*.

**how many pipes can I use?** As many as you like. For example you could get the "tail of the head". E.g., `iris %>% head(n = 20) %>% tail(n = 10)`. This is an example command chain (taking the first 20 lines of iris and the taking the last 10 lines ... of the first 20 lines). But I hope it shows the power of pipes in R. 

**What is the directional of pipes?** While very flexible, pipes do have directionality. That is to say, the data always comes first, then the functions... (not the other way around). `iris %>% head(n=10)` **is correct**. On the other hand `head(n=10) %>% iris` **is incorrect!**

**What is up with head(n = 10)?** Wait a minute! didn't we just learn that the `head` command used "flag arguments" `head -n 10`? Why are we seeing `head(n = 10)`? The answer is simple: `head -n 10` is the **UNIX (Rivanna)** language, whereas `head(n = 10)` is the **R ** language. While in unix functions take arguments using flags separated by spaces "-x -n -k", in R functions take arguments inside parenthesis and are often separated by commas. Example `head(n = 10)`. In this class you will have to wire your brain to being bilingual, but, instead of English, Spanish, or French, our languages are going to be unix and R. 

## Part 2. Moving around Rivanna while inside of R
To move around the supercomputer you can use commands:
```
getwd()  #---> this is the same as pwd in unix
setwd("./<< address >>") #--> this is the same as cd ./<< address >> in unix
```
**A core difference between Rivanna (unix) and R** is that, while in Rivanna you can provide addresses as simnple text `./some/place/here`,  **in R** you have to give addresses in quotes `"./some/place/here"`.

## Part 3. Filtering data in R 
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

## Part 4. How do we filter for multiple conditions?
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

## Part 5. Visualizing the basic properties of datasets.
One of the most important tasks in bioinformatics and genomics is to use tools to describe statistical distributions. These "tools" range from the fundamental summary statistics (mean, variance, median, confidence intervals) to elaborate data visualizations aimed at showcasing the properties of your data in a manner that is intuitive. Lets see some examples.

### Using ggplot to visualize data.
The R library _ggplot_ is perhaps on of the most famous libraries among data scientist. Ggplot provides a unified set of graphical tools to visualize your data. 

#### Ggplot works like a canvas
As a graphical tool, ggplot has rules of its own that we need to understand. Any ggplot figure is built using three sets of components: 1. Data + 2. Aesthetic map + 3. Elements. Here is an example: 

![ggplot basics](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/2.Introduction_to_R/Figures/ggplot_basics.wb2.png?raw=true)
**Data**: This is the data object would would like to base your figure on. Pass your data into ggplot by pipping it into `ggplot`

**Aesthetic map**: This is. the first function of any ggplot. This part generally always looks the same `ggplot(aes(..))`. it is a nested function of `ggplot()` and the `aes()` function. While technically different functions, for the purposes of this class, you can think for  `ggplot(aes(..))` as a single function. Now inside that function we get to put in what we want the actual data to be. For example `x=` , `y=` will define what data will go into the x and y axis.

**Elements**: This is the bread and butter of ggplot. You can add different types of figures to your plot. **Given that they are compatible with your data, of course!** Some examples are: `geom_point()`, `geom_errorbar()`. We will learn different elements as we progress in the class. A key thing to know is that you add elements to your plot using the `+` symbol (you can press enter after every `+`). 

#### Lets view a example using a "points plot"
```
iris %>%
ggplot(aes(x=Species, y=Sepal.Length)) +
geom_point(size = 3) -> just_points

#this will generate a "plot" point showing our data. geom_point only requires x and y data.

#save your plot
ggsave(just_points, file = "just_points.pdf", width = 6, height = 4)

#check your plot using your browser GUI
```

#### Lets add some color
Lets add some color. ggplot is a pretty smart function. As such you can simply ask ggplot to color your plot by a given variable.
```
iris %>%
ggplot(aes(x=Species, y=Sepal.Length, color=Species )) +
geom_point(size = 3) -> just_points_color

ggsave(just_points_color, file = "just_points_color.pdf", width = 6, height = 4)
```
![points with color](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/2.Introduction_to_R/Figures/species_plot_color.png?raw=true)
#### Using boxplots to summarize the core properties of distributions
Commonly called "box plots", interquartile range plots are a simple, yet elegant, way to visualize the the fundamental properties of your data. 

![IQR plots](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/2.Introduction_to_R/Figures/boxplot.png?raw=true)
```
iris %>%
ggplot(aes(x=Species, y=Sepal.Length, color=Species )) +
geom_boxplot() -> boxplot_iris

ggsave(boxplot_iris, file = "boxplot_iris.pdf", width = 6, height = 4)
```
![IQR plots](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/2.Introduction_to_R/Figures/boxplot_iris.png?raw=true)

## Part 6. Summarizing data
Now that we are masters of data exploration and manipulation. We can start asking questions about the data. We will start by asking trivial questions about  the data, but we will eventually move into more interesting biological questions. 
The first thing we need in order to summarize data is **grouping variable**. A grouping variable is basically some aspect of the data that we can use to partition the data. For example, lets partition the data based on whether or not a given species is my favorite or not. We will accomplish this by using the command `group_by()` 
```
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",)) %>%
group_by(isFavorite) 
```

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

## Part 6. Visualizing summaries using _ggplot_
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

This plot shows the point estimates of our `summarize(MEAN = ...)` analysis. But always remember that in statisitcs, point estimates are always associated with variance (i.e., a measure of data dispersion ). In our case we can some measure of dispersion by including our estimates of standard deviation  `summarize(SD = ...)`. We can do this using the element known as `geom_errorbar()`. This element requires, on top of `x` and `y`, two additional arguments `ymin` and `ymax`. We need to add these to the **aesthetic map**.

```
MyFavoriteIrisFlowers %>%
ggplot(aes(x=isFavorite, y=MEAN)) +
geom_point(size = 3)  -> point_estimates

ggsave(point_estimates, file = "point_estimates.pdf", width = 6, height = 4)

#check your plot using your browser GUI
```

**what is going on here??** So far, not much has happened in the front-end. In the back-end, however, as long as you continue to pipe the `group_by` function, R will group the data according to the contents of the  `isFavorite ` column. It is important to know that the grouping variable has to exists in the data, for example, if you use `select()` to pick a couple columns and by doing this you end up removing your grouping column, `group_by()` wont work!. So be careful when you code. 

![geom_point only](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/2.Introduction_to_R/Figures/point_only.png?raw=true)
```
MyFavoriteIrisFlowers %>%
ggplot(aes(x=isFavorite, y=MEAN, ymin = MEAN-SD, ymax = MEAN+SD)) +
geom_point(size = 3) +
geom_errorbar(width = 0.5) -> error_plus_point

ggsave(error_plus_point, file = "error_plus_point.pdf", width = 6, height = 4)

#check your plot using your browser GUI
```

![geom_point only](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/2.Introduction_to_R/Figures/point_plusError_only.png?raw=true)

wow! look at that! our point estimates are not very different after all!

## Part 7. Testing  explicit hypothesis these distributions
Now that we have graphically described our data, based on "my favorite category", we should apply statistical principles to test whether there distributions are. **significantly** different. One of the simplest options available to us is to use of the T statistic test. This is known formally as Student's T or Gosset's T, and colloquially as the "_t-test_". 

Like most statistical tests, the T-test makes some assumptions about the data. Applying any statistical test haphazardly will results in uninformative results! So always check your assumptions.  In the case of T, the primary assumption of the test is _normality_.

Want to learn more about hypothesis testing? [Check this summary video](https://www.youtube.com/watch?v=0oc49DyA3hU)

### Spot checking for normality in our data
To do this, lets go back to the "dis-aggregated" data.
```
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",)) %>%
ggplot(aes(x=Sepal.Length, color=isFavorite )) +
geom_histogram() -> favo_histogram

ggsave(favo_histogram, file = "favo_histogram.pdf", width = 6, height = 4)
``` 
#### Does that look "normal" to you?
![ggplot hist](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/2.Introduction_to_R/Figures/favorite_distribution_hist.png?raw=true)
We can check for signatures of normality using a graphical device call a QQplot, or a quantile-quantile plot. This is method allows you to compare how different percentiles in the real data, compare to "theoretical" percentiles from a simulated normal distribution. 

Want to learn more about QQplots? [check out this video](https://www.youtube.com/watch?v=okjYjClSjOg)

Lets divide the data into "yeas" and "nays":

```
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",)) %>%
ggqqplot(data = ., x = "Sepal.Length", color = "isFavorite") -> myqqplot

ggsave(myqqplot, file = "myqqplot.pdf", width = 6, height = 4)

```
**Learning an R trick**: Notice that we have passed data into `wilcox.test` using the symbol `.` this is neat trick that you can use all the time. The symbol `.` or, `(data = .)`, basically means pass onto the function whatever data comes "down the pipe"

![ggplot qqplot](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/2.Introduction_to_R/Figures/qqplot_iris.png?raw=true)

### Would you go ahead with a test assume normality with this data?
The answer is no. This is because our "No" distribution does not follow the QQ normality plot, so you probably should not assume normality with this dataset.  **Advanced tip** We can do a _formal_ hypothesis testing of these assumtion using the R function `shapiro.test()`. 

### How can we test if these distributions are different?
Since we cannot use Student'T, our next best option is to use `wilcox.test` (a.k.a. _Mann-Whitney's U_). A test which does not assumes normality. 
```
#let's make a data object w
iris %>%    
mutate(isFavorite = case_when(Species == "versicolor" ~ "Yes", Species != "versicolor" ~ "No",)) %>%
wilcox.test(Sepal.Length~isFavorite, data = .)
```

Want to learn more about the wilcox test? [check out this video](https://www.youtube.com/watch?v=TqCg2tb4wJ0) in which a statisitcian does the wilcox testing **by hand**! 

Now let's look at the results:
```
Wilcoxon rank sum test with continuity correction

data:  Sepal.Length by isFavorite
W = 2142.5, p-value = 0.1543
alternative hypothesis: true location shift is not equal to 0
```

## Part 8. Code Challenge 

Using you knowledge of R for data manipulation generate the following graph --> A graph showing on the **x-axis** all the species contained in `iris`, on the **y-axis** showing the mean value for `Petal.Length` also include error bars showing the standard deviation. Hint: you will use `group_by()`, `summarize()`, `ggplot(aes())`, `geom_point()`, `geom_errorbar()`, among others. Submit your graph to the homework folder once you are done.
