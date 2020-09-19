# CorrelationMatrix

I was looking through some Kaggle projects to find out how some other
data scientists go about analyzing new data sets. One powerful tool
I found to get a rough sense of the data was the correlation matrix.

The correlation matrix displays how closely every attribute correlates
with one another in the data set. Using matplotlib and seaborn, these
correlations can be easily analyzed. Stronger correlations can pop with
brighter or darker colors!

-----------------------------------------------------------------------
Step 1: Build My First Correlation Matrix

This step ended up being easier than I expected! Pandas has a built-in
function to generate a correlation matrix of values for a given dataframe.

I used the df.corr() function to generate all the data necessary. Then,
I was able to use seaborn to plot this data on a heatmap where the 
lighter colors showed a strong positive correlation.

The first chart constructed, 

"CorrelationMatrix_Start.png"

is just a display of random values compared with one another. 
Unsurprisingly, there is virtually no correlation between any of the 
variables.

----------------------------------------------------------------------
Step 2: Find Some Data to Test Out the Correlation Matrix!

I looked around on Kaggle for some data that could display interesting
variables to compare. I eventually came across data that compared a 
country's happiness score to a number of variables and figured this
would make an interesting showcase for a correlation matrix.

"Happiness_2015_FullMatrix.png" shows the first correlation matrix I made
with the Happiness Data CSV files. 

Since the information above the diagonal line of "1"s is redundant, I
referenced the seaborn documentation to apply a mask to filter the top
half of the data. This allowed the colors to normalize between the 
minimum and maximum correlations between two variables (and cleaned up
the figure quite a bit). The result can be seen with the 

"Happiness_Half_Matrix.png"

figure.

---------------------------------------------------------------------
Step 3: Interpreting the Data

I created figures for each of the 5 CSV files. These figures can be 
seen in the 

"HappinessCorrelationMatrices" 

folder. One correlation clearly stands out to me as the strongest: 
Health to GDP. 
This is made more interesting by the fact that the correlation 
between the happiness score and GDP is not much less than the correlation 
between health and GDP. 

Perhaps it is not GDP that directly causes happiness, but the health
benefits that come with a higher GDP.
