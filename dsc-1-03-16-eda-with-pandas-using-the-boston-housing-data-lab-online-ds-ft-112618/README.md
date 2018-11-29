
# Project - EDA with Pandas Using the Boston Housing Data

## Introduction

In this section you've learned a lot about importing, cleaning up, analysing (using descriptive statistics) and visualizing data. In this more free form project you'll get a chance to practice all of these skills with the Boston Housing data set,  which contains housing values in suburbs of Boston. The Boston Housing Data is commonly used by aspiring data scientists.  

# What is EDA? 
## Exploratory Data Analysis
* Step to take initial data set and get a high level statistical numbers (centralities/dispersions/etc) - Andrew
* Find possible bugs and logical inconsistencies in the data, have to go back to team that put together database - Tara

## Objectives
You will be able to:
* Show mastery of the content covered in this section
* YWBAT Explore data and find correlations
* YWBAT Create visualizations from the data set
* YWBAT slice data based on specific values 
* YWBAT normalization of the data (mean)

# What did we learn?
* The color dictionary scatter plot - Tara, John, Andrew
* The steps to take a high level eda - Andrew
* Scattermatrix - Andrew

# Goals

Use your data munging and visualization skills to conduct an exploratory analysis of the dataset below. At minimum, this should include:

* Loading the data (which is stored in the file train.csv)
* Use built-in python functions to explore measures of centrality and dispersion for at least 3 variables
* Create *meaningful* subsets of the data using selection operations using `.loc`, `.iloc` or related operations. Explain why you used the chosen subsets and do this for 3 possible 2-way splits. State how you think the 2 measures of centrality and/or dispersion might be different for each subset of the data. Examples of potential splits:
    - Create a 2 new dataframes based on your existing data, where one contains all the properties next to the Charles river, and the other one contains properties that aren't.
    - Create 2 new datagrames based on a certain split for crime rate.
* Next, use histograms and scatterplots to see whether you observe differences for the subsets of the data. Make sure to use subplots so it is easy to compare the relationships.


```python
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
```


```python
# look at nulls
df.info()
# all numbers equal 333 which means there are no nulls
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 333 entries, 0 to 332
    Data columns (total 15 columns):
    ID         333 non-null int64
    crim       333 non-null float64
    zn         333 non-null float64
    indus      333 non-null float64
    chas       333 non-null int64
    nox        333 non-null float64
    rm         333 non-null float64
    age        333 non-null float64
    dis        333 non-null float64
    rad        333 non-null int64
    tax        333 non-null int64
    ptratio    333 non-null float64
    black      333 non-null float64
    lstat      333 non-null float64
    medv       333 non-null float64
    dtypes: float64(11), int64(4)
    memory usage: 39.1 KB



```python
df = pd.read_csv("train.csv") # df is very common name a variable (dataframe)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>crim</th>
      <th>zn</th>
      <th>indus</th>
      <th>chas</th>
      <th>nox</th>
      <th>rm</th>
      <th>age</th>
      <th>dis</th>
      <th>rad</th>
      <th>tax</th>
      <th>ptratio</th>
      <th>black</th>
      <th>lstat</th>
      <th>medv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1</td>
      <td>296</td>
      <td>15.3</td>
      <td>396.90</td>
      <td>4.98</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2</td>
      <td>242</td>
      <td>17.8</td>
      <td>396.90</td>
      <td>9.14</td>
      <td>21.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3</td>
      <td>222</td>
      <td>18.7</td>
      <td>394.63</td>
      <td>2.94</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3</td>
      <td>222</td>
      <td>18.7</td>
      <td>396.90</td>
      <td>5.33</td>
      <td>36.2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>0.08829</td>
      <td>12.5</td>
      <td>7.87</td>
      <td>0</td>
      <td>0.524</td>
      <td>6.012</td>
      <td>66.6</td>
      <td>5.5605</td>
      <td>5</td>
      <td>311</td>
      <td>15.2</td>
      <td>395.60</td>
      <td>12.43</td>
      <td>22.9</td>
    </tr>
  </tbody>
</table>
</div>



# Variable Descriptions

This data frame contains the following columns:

#### crim  
per capita crime rate by town.

#### zn  
proportion of residential land zoned for lots over 25,000 sq.ft.

#### indus  
proportion of non-retail business acres per town.

#### chas  
Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).

#### nox  
nitrogen oxides concentration (parts per 10 million).

#### rm  
average number of rooms per dwelling.

#### age  
proportion of owner-occupied units built prior to 1940.

#### dis  
weighted mean of distances to five Boston employment centres.

#### rad  
index of accessibility to radial highways.

#### tax  
full-value property-tax rate per $10,000.

#### ptratio  
pupil-teacher ratio by town.

#### black  
1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town.

#### lstat  
lower status of the population (percent).

#### medv  
median value of owner-occupied homes in $10000s.
  
  
  
Source
Harrison, D. and Rubinfeld, D.L. (1978) Hedonic prices and the demand for clean air. J. Environ. Economics and Management 5, 81–102.

Belsley D.A., Kuh, E. and Welsch, R.E. (1980) Regression Diagnostics. Identifying Influential Data and Sources of Collinearity. New York: Wiley.


```python
pd.scatter_matrix(df, figsize=(20, 20), density_kwds='kde')
plt.show()
```

    /anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:1: FutureWarning: pandas.scatter_matrix is deprecated, use pandas.plotting.scatter_matrix instead
      """Entry point for launching an IPython kernel.



![png](index_files/index_10_1.png)



```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>crim</th>
      <th>zn</th>
      <th>indus</th>
      <th>chas</th>
      <th>nox</th>
      <th>rm</th>
      <th>age</th>
      <th>dis</th>
      <th>rad</th>
      <th>tax</th>
      <th>ptratio</th>
      <th>black</th>
      <th>lstat</th>
      <th>medv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
      <td>333.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>250.951952</td>
      <td>3.360341</td>
      <td>10.689189</td>
      <td>11.293483</td>
      <td>0.060060</td>
      <td>0.557144</td>
      <td>6.265619</td>
      <td>68.226426</td>
      <td>3.709934</td>
      <td>9.633634</td>
      <td>409.279279</td>
      <td>18.448048</td>
      <td>359.466096</td>
      <td>12.515435</td>
      <td>22.768769</td>
    </tr>
    <tr>
      <th>std</th>
      <td>147.859438</td>
      <td>7.352272</td>
      <td>22.674762</td>
      <td>6.998123</td>
      <td>0.237956</td>
      <td>0.114955</td>
      <td>0.703952</td>
      <td>28.133344</td>
      <td>1.981123</td>
      <td>8.742174</td>
      <td>170.841988</td>
      <td>2.151821</td>
      <td>86.584567</td>
      <td>7.067781</td>
      <td>9.173468</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.006320</td>
      <td>0.000000</td>
      <td>0.740000</td>
      <td>0.000000</td>
      <td>0.385000</td>
      <td>3.561000</td>
      <td>6.000000</td>
      <td>1.129600</td>
      <td>1.000000</td>
      <td>188.000000</td>
      <td>12.600000</td>
      <td>3.500000</td>
      <td>1.730000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>123.000000</td>
      <td>0.078960</td>
      <td>0.000000</td>
      <td>5.130000</td>
      <td>0.000000</td>
      <td>0.453000</td>
      <td>5.884000</td>
      <td>45.400000</td>
      <td>2.122400</td>
      <td>4.000000</td>
      <td>279.000000</td>
      <td>17.400000</td>
      <td>376.730000</td>
      <td>7.180000</td>
      <td>17.400000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>244.000000</td>
      <td>0.261690</td>
      <td>0.000000</td>
      <td>9.900000</td>
      <td>0.000000</td>
      <td>0.538000</td>
      <td>6.202000</td>
      <td>76.700000</td>
      <td>3.092300</td>
      <td>5.000000</td>
      <td>330.000000</td>
      <td>19.000000</td>
      <td>392.050000</td>
      <td>10.970000</td>
      <td>21.600000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>377.000000</td>
      <td>3.678220</td>
      <td>12.500000</td>
      <td>18.100000</td>
      <td>0.000000</td>
      <td>0.631000</td>
      <td>6.595000</td>
      <td>93.800000</td>
      <td>5.116700</td>
      <td>24.000000</td>
      <td>666.000000</td>
      <td>20.200000</td>
      <td>396.240000</td>
      <td>16.420000</td>
      <td>25.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>506.000000</td>
      <td>73.534100</td>
      <td>100.000000</td>
      <td>27.740000</td>
      <td>1.000000</td>
      <td>0.871000</td>
      <td>8.725000</td>
      <td>100.000000</td>
      <td>10.710300</td>
      <td>24.000000</td>
      <td>711.000000</td>
      <td>21.200000</td>
      <td>396.900000</td>
      <td>37.970000</td>
      <td>50.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.crim.plot(kind='hist', bins=20, figsize=(5, 5), alpha=0.5, grid=True)
# alpha affects the transparency of the graph
plt.xlabel("crime per capita")
plt.ylabel("counts")
plt.title("Crime per Capita Histogram")
plt.show()
```


![png](index_files/index_12_0.png)



```python
medv = df.medv
crim = df.crim
plt.figure(figsize=(8, 8))
plt.scatter(crim, medv, alpha=0.5, c='r')
plt.grid()
plt.xlabel("Crime Per Capita")
plt.ylabel("Median Occupied Home Owners")
plt.title("Crime Per Capita vs\nMedian Occupied Home Owners")
plt.show()
```


![png](index_files/index_13_0.png)



```python
crime_greater_than_one = df[(df["crim"] > 1.0) & (df["medv"] < 30)]
```


```python
crime_greater_than_one.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>crim</th>
      <th>zn</th>
      <th>indus</th>
      <th>chas</th>
      <th>nox</th>
      <th>rm</th>
      <th>age</th>
      <th>dis</th>
      <th>rad</th>
      <th>tax</th>
      <th>ptratio</th>
      <th>black</th>
      <th>lstat</th>
      <th>medv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>17</td>
      <td>1.05393</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>5.935</td>
      <td>29.3</td>
      <td>4.4986</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>386.85</td>
      <td>6.58</td>
      <td>23.1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>21</td>
      <td>1.25179</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>5.570</td>
      <td>98.1</td>
      <td>3.7979</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>376.57</td>
      <td>21.02</td>
      <td>13.6</td>
    </tr>
    <tr>
      <th>15</th>
      <td>23</td>
      <td>1.23247</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>6.142</td>
      <td>91.7</td>
      <td>3.9769</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>18.72</td>
      <td>15.2</td>
    </tr>
    <tr>
      <th>18</th>
      <td>31</td>
      <td>1.13081</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>5.713</td>
      <td>94.1</td>
      <td>4.2330</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>360.17</td>
      <td>22.60</td>
      <td>12.7</td>
    </tr>
    <tr>
      <th>19</th>
      <td>32</td>
      <td>1.35472</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>6.072</td>
      <td>100.0</td>
      <td>4.1750</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>376.73</td>
      <td>13.04</td>
      <td>14.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
medv = crime_greater_than_one.medv
crim = crime_greater_than_one.crim
plt.figure(figsize=(8, 8))
plt.scatter(crim, medv, alpha=0.5, c='r')
plt.grid()
plt.xlabel("Crime Per Capita")
plt.ylabel("Median Occupied Home Owners")
plt.title("Crime Per Capita vs\nMedian Occupied Home Owners")
plt.show()
```


![png](index_files/index_16_0.png)



```python
plt.figure(figsize=(8, 8))
plt.hist(df.nox, color='b', alpha=0.5)
plt.grid()
plt.show()
```


![png](index_files/index_17_0.png)



```python
plt.figure(figsize=(8, 8))
plt.hist(df.indus, color='b', alpha=0.5)
plt.grid()
plt.show()
```


![png](index_files/index_18_0.png)



```python
df_nox_indus_slice = df[(df.indus < 25) & (df.nox < 0.8)]
```


```python
nox = df_nox_indus_slice.nox.values
indus = df_nox_indus_slice.indus.values

plt.figure(figsize=(8, 8))
plt.scatter(nox, indus, alpha=0.5, c='g')
plt.grid()
plt.xlabel("nox")
plt.ylabel("indus")
plt.title("nox vs indus")
plt.show()
```


![png](index_files/index_20_0.png)



```python

```




    (array([27., 57., 30., 49., 35., 51., 27., 32., 15., 10.]),
     array([-0.95451194, -0.87287208, -0.79123222, -0.70959235, -0.62795249,
            -0.54631262, -0.46467276, -0.38303289, -0.30139303, -0.21975317,
            -0.1381133 ]),
     <a list of 10 Patch objects>)




![png](index_files/index_21_1.png)



```python
plt.figure(figsize=(8, 8))
plt.hist(df.crim, color='b', alpha=0.5, bins = 20)
plt.grid()
plt.show()
```


![png](index_files/index_22_0.png)



```python
df.crim.describe()
```




    count    333.000000
    mean       3.360341
    std        7.352272
    min        0.006320
    25%        0.078960
    50%        0.261690
    75%        3.678220
    max       73.534100
    Name: crim, dtype: float64




```python
inner_quarters = np.percentile(df.crim.values, q=[25, 50, 75])
```


```python
inner_quarters_crim_df = df[(df.crim >= 0.7896) & (df.crim <= 3.36822)]
inner_quarters_crim_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>crim</th>
      <th>zn</th>
      <th>indus</th>
      <th>chas</th>
      <th>nox</th>
      <th>rm</th>
      <th>age</th>
      <th>dis</th>
      <th>rad</th>
      <th>tax</th>
      <th>ptratio</th>
      <th>black</th>
      <th>lstat</th>
      <th>medv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>17</td>
      <td>1.05393</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>5.935</td>
      <td>29.3</td>
      <td>4.4986</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>386.85</td>
      <td>6.58</td>
      <td>23.1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>19</td>
      <td>0.80271</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>5.456</td>
      <td>36.6</td>
      <td>3.7965</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>288.99</td>
      <td>11.69</td>
      <td>20.2</td>
    </tr>
    <tr>
      <th>13</th>
      <td>21</td>
      <td>1.25179</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>5.570</td>
      <td>98.1</td>
      <td>3.7979</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>376.57</td>
      <td>21.02</td>
      <td>13.6</td>
    </tr>
    <tr>
      <th>14</th>
      <td>22</td>
      <td>0.85204</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>5.965</td>
      <td>89.2</td>
      <td>4.0123</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>392.53</td>
      <td>13.83</td>
      <td>19.6</td>
    </tr>
    <tr>
      <th>15</th>
      <td>23</td>
      <td>1.23247</td>
      <td>0.0</td>
      <td>8.14</td>
      <td>0</td>
      <td>0.538</td>
      <td>6.142</td>
      <td>91.7</td>
      <td>3.9769</td>
      <td>4</td>
      <td>307</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>18.72</td>
      <td>15.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(8, 8))
plt.hist(inner_quarters_crim_df.crim, color='b', alpha=0.5, bins = 20)
plt.grid()
plt.show()
```


![png](index_files/index_26_0.png)



```python
plt.figure(figsize=(8, 8))
plt.hist(inner_quarters_crim_df.ptratio, color='b', alpha=0.5, bins = 20)
plt.grid()
plt.show()
```


![png](index_files/index_27_0.png)



```python
inner_quarters_crim_df.ptratio.value_counts()
```




    14.7    21
    21.0    10
    20.2     3
    21.2     3
    18.4     2
    13.0     1
    Name: ptratio, dtype: int64




```python
color_dict = {14.7: 'g', 21.0: 'b', 20.2: "r", 21.2: "k", 18.4: "purple", 13.0: "cyan"}
```


```python
plt.figure(figsize=(10, 10))
for cr, pt in zip(inner_quarters_crim_df.crim, inner_quarters_crim_df.ptratio):
    plt.scatter(cr, pt, alpha=0.5, c = color_dict[pt])
plt.xlabel("crime")
plt.legend()
plt.grid()
plt.ylabel("ptratio")
plt.title("crime vs ptratio")
plt.show()
```

    No handles with labels found to put in legend.



![png](index_files/index_30_1.png)



## Summary

Congratulations, you've completed your first "freeform" exploratory data analysis of a popular data set!


```python
ptratio_14 = df[df.ptratio == 14.7]
```


```python
pd.scatter_matrix(ptratio_14, figsize=(20, 20))
plt.show()
```

    /anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:1: FutureWarning: pandas.scatter_matrix is deprecated, use pandas.plotting.scatter_matrix instead
      """Entry point for launching an IPython kernel.
    /anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py:3124: UserWarning: Attempting to set identical left==right results
    in singular transformations; automatically expanding.
    left=14.7, right=14.7
      'left=%s, right=%s') % (left, right))
    /anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py:3443: UserWarning: Attempting to set identical bottom==top results
    in singular transformations; automatically expanding.
    bottom=14.7, top=14.7
      'bottom=%s, top=%s') % (bottom, top))



![png](index_files/index_33_1.png)

