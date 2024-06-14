def linear_search(list, target):
    '''return the index position'''
    for i in range(0,len(list)):
        if list[i]==target:
            return i
    return None

# l1=[1,2,3,4,5,6,7,8,9]
# print("the list is",l1,"\n")
# val=input("Enter the value to find its index-")
# result=linear_search(l1,val)
# print(result)

#SUM OF n NUMBERS USING RECURSION 
def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
# SUM OF N NUMBERS WITHOUT RECURSION
def sum2(n):
    result=0
    for i in range(1,n+1):
        result+=i
    return result

# print(sum2(90))
# STRING REVERSAL
# def reverse(s):
    # return print(s[::-1])

s="hello"
# reverse(s)
txt = "Hello World"[::-1]
# print(txt)
list=[1,2,3,4,5]
r_list=reversed(list)
# print(r_list)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self) -> str:
    return f"{self.name}-{self.age}"
  
class Student(Person):
   def __init__(self, name, age, year):
      super().__init__(name, age)
      self.gradyear=year
   def __str__(self) -> str:
      return f"{super().__str__()} , {self.gradyear}"
      
    

p1 = Student("John", 36,2019)
# print(p1)
# mytuple = ("apple", "banana", "cherry")
# for element in mytuple:
#    print(element)
# my=iter(mytuple)
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))

class Playlist:
   def __init__(self,weekend) -> None:
      self.songs=weekend
      self.songindex=0

   def __iter__(self):
      return self
   def __next__(self):
      if self.songindex<len(self.songs):
         weekend=self.songs[self.songindex]
         self.songindex+=1
         return weekend
      else:
         raise StopIteration
      
my_playlist = Playlist(["Song 1", "Song 2", "Song 3", "Song 4"])
# for i in my_playlist:
#    print (f"CURRENT SONG {i}")
class Vechicle:
   def __init__(self,brand,model) -> None:
      self.brand=brand
      self.model=model

 
class Car(Vechicle):
  def move(self):
    print("Drive!")

class Boat(Vechicle):


  def move(self):
     print("Sail!")

class Plane(Vechicle):
   def move(self):
      print("Fly!")



car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()
      
import platform

# print(dir(platform))
import datetime as dt

x = dt.datetime.now()

# print(x.year)
# print(x.strftime("%S"))
import sys
# print(sys.builtin_module_names)
import time
# print(dir(time))
# print("1")
# time.sleep(4)
# print("1")

import difflib
import json
# from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))


def WordSearcher(key):
   # SequenceMatcher(None,data.keys()).ratio()
   
   if key in data:
      print(data[key])

   elif len(get_close_matches(key,data.keys(),cutoff= 0.8))>0:
         c=get_close_matches(key,data.keys(),cutoff= 0.8)[0]
         choice=input(f"did you {c} mean?(Y/N) - ")
         if choice == "Y" or "y":
            print(f"The meaning of {c} is {data[c]}")
         elif choice == "N" or "y":
           print("The word doesn't exist or Please recheck the spelling.") 
         else:
            print("Didn't understand your input.")
   
   else:
         print("The word doesn't exist or Please recheck the spelling.")
      
      
n=""   
while n!="n" or "N":
   key=input("Enter a word: ")
   WordSearcher(key.lower())
   n=input("Do you have an another word to look up for?(Y/N)")


