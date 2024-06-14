import difflib                        # this is used for comparing words in the Dictionary
import json                           # this is for the json file which is used as the database for the Dictionary
# from difflib import SequenceMatcher # This is just another module for better understanding.
from difflib import get_close_matches # Another module for guessing the typo mistake.
data = json.load(open("data.json"))   # load the json file content in 'data' 


def WordSearcher(key):                                           
   # SequenceMatcher(None,data.keys()).ratio()                   # for learning purpuse only.
   
   if key in data:
      print(data[key])

   elif len(get_close_matches(key,data.keys(),cutoff= 0.8))>0:   # this returns a list type result 
         c=get_close_matches(key,data.keys(),cutoff= 0.8)[0]     # only the first i.e. Zero index element is choosen as a match.
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
   WordSearcher(key.lower())                                    # The data in the json file is in lowercase so to match that the lower() is used.
   n=input("Do you have an another word to look up for?(Y/N)")


