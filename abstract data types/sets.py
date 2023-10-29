""" 
Unit: Abstract Data Types
Presentation: 0 - Introduction - Sets

In this task you will explore the Sets abstract data type (ADT).
The tasks are structured such that the each is progressively more diffiult. 

When you are done with these tasks you should be able to answer the following
questions: 
  1. How is the data organized in the ADT?
  2. How can we manipulate that data?
  3. How could this ADT be used, or in what situations could you use it?

"""

from code import interact


def sets_problem1(lst):
    return set(lst)

    """
    Given a list return a set.

  Example: 
    lst = [1, 2, 3, 2, 3, 4, 4, 1]
    Returns {1, 2, 3, 4} or equivalent (order doesn't matter)

  """

print(sets_problem1([1, 2, 3, 2, 3, 4, 4, 1]))


def sets_problem2(set1, set2):
    return set1.intersection(set2)
    """
  Given two sets return the values that common to both as a list in order 
  from least to greatest.

  Example:
    set1 = {1, 2, 3, 4} and set2 = {2, 3, 4, 5, 6}
    Returns [2, 3, 4] 
  
  """ 
set1 = {1, 2, 3, 4} 
set2 = {2, 3, 4, 5, 6}
print(sets_problem2(set1,set2))


def sets_problem3(set1, set2, set3):
  """
  Given three sets return the values that are in set1 and set2 but not in set3. 
  
  Example:
    set1 = {1, 2, 3} and set2 ={2, 3, 4} and set3 = {3, 4, 5}
    Returns{2}
  """
  pass
