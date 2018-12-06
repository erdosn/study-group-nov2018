
# Objectives
* YWBAT explain the permutation formula
* YWBAT derive the combination formula

# Stuff we need first


```python
# factorial(5) = 5*4*3*2*1
# factorial(8) = 8*7*6*..*1
```


```python
x = ['a', 'b', 'c']
```


```python
def factorial(n):
    prod = 1
    for number in range(1, n+1):
        prod *= number
    return prod
```


```python
len(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
```




    6




```python
3 * 2 * 1
```




    6




```python
'abcdef'
```




    'abcdef'




```python
factorial(6)
```




    720




```python
# what is the probability of getting an arrangement with a as the third letter
```


```python
# p(having a as 3rd letter) = number of ways a is 3rd letter / total arrangements
```


```python
# permutations is used to get the size of probability space
```


```python
P_a_third_letter = (720/6)/factorial(6)
P_a_third_letter
```




    0.16666666666666666




```python
# a as the 3rd letter is 1/6 of everything 
# P = event space / probability space
# P = 120 ways a is 3rd / 720 different permutations
# P = 120/720 = 1/6 = 0.1666666666...
```


```python
# P('a is 3rd') = 720/6 
p_a_3 = factorial(5) / factorial(6)
p_a_3
# a 5 4 3 2 1 
```




    0.16666666666666666




```python
# P(a is 1st and b is 4th)
# how big is probability space = 720
# how big is event space = factorial(4)
factorial(4)/factorial(6)
```




    0.03333333333333333




```python
1/12
```




    0.08333333333333333




```python
1/30
```




    0.03333333333333333




```python
# permutations - ways things can be arranged (repetition counts)
```


```python
# combination - groups
```


```python
lst = ['andrew', 'rafael', 'allison', 'eli', 'katie']
```


```python
s = (('andrew', 'rafael', 'allison'), ('andrew', 'rafael', 'eli'), ('andrew', 'rafael', 'katie'), ('andrew', 'allison', 'eli'), ('andrew', 'allison', 'katie'), ('andrew', 'eli', 'katie'), ('rafael','allison', 'eli'), ('rafael', 'allison', 'katie'), ('allison', 'eli', 'katie'))
```


```python
len(set(s)) == len(s)
```




    True




```python
def combinations(total_group_size, desired_group_size):
    numerator = factorial(total_group_size)
    denominator = factorial(desired_group_size) * factorial(total_group_size-desired_group_size)
    return numerator/denominator
```


```python
combinations(5, 2)
```




    10.0




```python
# choose function 
```


```python
from itertools import combinations
```


```python
x=list('abcde')
x
```




    ['a', 'b', 'c', 'd', 'e']




```python
count_as = 0
for combination in combinations(x, 3): # groups of 2 from x
    if 'a' in combination:
        count_as += 1 # print all combinations
```


```python
# total combinations
len(list(combinations(x, 2))) # similar to our combinations functions
```




    10




```python
# what is the probability of making groups of 3 and picking 1 group of 3 that has a in it from abcde
```


```python
denominator = len(list(combinations(x, 3))) # probability space
denominator
```




    10




```python
for combo in combinations(x, 3):
    if 'a' in combo:
        print(combo)
print(len(list(combinations(x, 3))))
```

    ('a', 'b', 'c')
    ('a', 'b', 'd')
    ('a', 'b', 'e')
    ('a', 'c', 'd')
    ('a', 'c', 'e')
    ('a', 'd', 'e')
    10



```python
count_as
```




    6




```python
numerator = len(list(combinations([1, 2, 3, 4], 2)))
numerator
```




    6




```python
4 choose 2 / 5 choose 3
```
