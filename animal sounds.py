#  Create a base class Animal with a method make_sound()

class animal:
      def make_sound(self):
            print('generic animal sound')
            
# Create two subclasses Dog and Cat, each inheriting from the Animal class.            
# override the make_sound() method in the dog and cat classes

class dog(animal):
      def make_sound(self):
            print('bark')
class cat(animal):
      def make_sound(self):
            print('meow')  

# Implement a function called animal_sound_in_zoo() that takes an animal object as a parameter and calls its make_sound() method.

def animal_sound_in_zoo(animal):
      animal.make_sound() 
# Create instances of Dog and Cat classes and call the animal_sound_in_zoo() function with these instances as arguments to observe their unique sounds.

dog_instance=dog()
cat_instance=cat()     

animal_sound_in_zoo(dog_instance)   
animal_sound_in_zoo(cat_instance)                