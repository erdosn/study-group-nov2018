import random
random.seed(42)

# Classes are capital case in python and one word EveryWordIsCapitalCase
class Pet(object):
    
    # constructor method
    def __init__(self, name=None, breed=None, sex=None):
        # assign the name to Pet class
        self.name = name
        self.breed = breed
        self.sex = sex
        self.is_hungry = True
        self.make_noise = None
        pass
    
    
    def feed_pet(self):
        if self.is_hungry == False:
            print("Pet will die if you feed it, don't feed")
            return None
        else:
            print("Feeding {}".format(self.name))
            self.is_hungry = False
    
    
    # setter method setter/getter
    def set_is_hungry(self, hungry=None):
        self.is_hungry = hungry
        pass
    
    
    def get_is_hungry(self):
        return self.is_hungry
    
    
    def set_make_noise(self, noise=None):
        self.make_noise = noise
        pass
    
    
    @staticmethod # decorator -> really advanced
    def speak(sentence):
        return sentence
    