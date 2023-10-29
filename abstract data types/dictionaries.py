""" 
Unit: Abstract Data Types
Presentation: 0 - Introduction - Dictionaries

In this task you will explore the dictionaries abstract data type (ADT).
The tasks are structured such that the each is progressively more diffiult. 

When you are done with these tasks you should be able to answer the following
questions: 
  1. How is the data organized in the ADT?
  2. How can we manipulate that data?
  3. How could this ADT be used, or in what situations could you use it?

"""


def dictionaries_problem1(dict_to_check):
    try:
        if dict_to_check['Go']%2 == 0:
            return True
    except:
        pass
    return False

    """
  Given a parameter which is a dictionary, check if the dictionary contains
  the key "Go" and an even number as its value. 

  If the key-value pair is in the dictionary and event return True, else
  return False. 

  """
print(dictionaries_problem1({'HI':2,"nope":13}))


def dictionaries_problem2(dict_to_use):
    dict_to_use.pop("Here")
    dict_to_use["There"] = 10
    if "Where" in dict_to_use:
        dict_to_use.update({"Where":5})
    
    return dict_to_use
    """
  Given a dictionary perform the following operations on it.
    1. Remove the key "Here".
    2. Add a key "There" and give it the value 10.
    3. If the key "Where" exists, update it to 5. 

  """ 
print(dictionaries_problem2({'HI':2,"nope":13, "Here":12,"Where":3}))



def dictionaries_problem3():
    my_dict = {}
    for i in range(26):
        my_dict[chr(65+i)] = i
    
    print(my_dict)
    """
  Create and return a dictionary that contains all the letters of the alphabet
  with their values being their location in the alphabet. As a programmer you 
  should obviously start with 0. 

  Example: 
    d = {'A': 0, 'B': 2 ... 'Z': 25}

  Hint: Use the chr() and ord() functions to help you. 

  """
dictionaries_problem3()

def dictionaries_problem4(d1, d2):
    if d1 == d2:
        return 2
    elif d1.keys() == d2.keys():
        return 1
    else:
        return 0
    """
  Given two dictionaries determine if they have all the same keys,
  the same keys and values, or nothing which is all the same. 
  Return the following based on the criteria:

    1. Nothing is the same, return 0
    2. Just the keys are the same, return 1
    3. The keys and the values are all the same, return 2
  
  Example: 
    d1 = {'b': 1, 'c': 2}
    d2 = ['b': 2, 'c': 9}

    This will return 1

  """
d1 = {'HI':2,"nope":13, "Here":12,"Where":3}
d2 = {'HI':2, "Here":12,"Where":3,"nope":11,}
print(dictionaries_problem4(d1,d2))
  