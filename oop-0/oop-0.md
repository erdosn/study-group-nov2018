
# Objectives
* YWBAT create a class
* YWBAT instantiate some class variables
* YWBAT create class methods
* YWBAT assign/reassign variables using methods


```python
import pet

from importlib import reload 
from pet import Pet
reload(pet)
```




    <module 'pet' from '/Users/rcarrasco/notes/study_groups/study-group-nov2018/oop-0/pet.py'>




```python
my_pet = Pet(name="Hedwig", breed='owl', sex='M')
```


```python
my_pet.name, my_pet.breed, my_pet.sex, my_pet.is_hungry
```




    ('Hedwig', 'owl', 'M', True)




```python
my_pet.feed_pet()
```

    Feeding Hedwig



```python
my_pet.is_hungry
```




    False




```python
my_pet.feed_pet()
my_pet.is_hungry
```

    Pet will die if you feed it, don't feed





    False




```python
my_pet.set_is_hungry(hungry=True)
my_pet.get_is_hungry()
```




    True




```python
print(my_pet.make_noise)
```

    None



```python
my_pet.set_make_noise(noise="Grrr")
```


```python
my_pet.make_noise
```




    'Grrr'




```python
my_pet.speak(sentence="hi")
```




    'hi'



# Wrap Up

* setters/getters 
    * set a specific attribute
    * retreive the attribute
    * use 'set' and 'get' because of common practice
* '__init__'
    * initalizes the attributes of the class
    * constructor method in python
* use reload when doing oop
