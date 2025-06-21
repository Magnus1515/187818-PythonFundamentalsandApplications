

# class Singleton:
#   _instance = None

#   def __new__(cls):
#     if cls._instance is None:
#       cls._instance = super().__new__(cls)
#     return cls._instance
  

# s1 = Singleton()
# s2 = Singleton()

# print(s1 is s2)


import copy 

class Prototype:
    def clone (self):
      return copy.deepcopy(self)
    

class Car(Prototype):
  def __init__(self, model, color):
    self.model = model
    self.color = color
    
  def __str__(self):
   return f"{self.color} {self.model}"

car1 = Car("Tesla", "Red")
car2 = car1.clone()
car2.color = "Blue"

print(car1)  # Red Tesla
print(car2)  # Blue Tesla

