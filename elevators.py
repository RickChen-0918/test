import random
import plotly.express as px
import pandas as pd 
class Building:
  def __init__(self,floors,floor_height,traffic):
    self.floors=floors
    self.floor_height=floor_height #meters
    self.traffic=traffic #seconds between every new arrival

class Person:
  def __init__(self,start,end,arrival):
    self.arrival = arrival #time they arrive at
    self.start = start #the floor the start on
    self.end = end #the floor they want to go to
    self.waittime = 0 #seconds
    self.inelevator = False
    if self.start > self.end:
      self.direction = -1
    elif self.start < self.end:
      self.direction = 1
    else:
      self.direction = 0
      
class Elevator:
  def __init__(self, speed, capacity):
    self.direction=1
    self.elapsedtime=0 #seconds
    self.location=1 #floor
    self.speed=speed #meters per second
    self.capacity=capacity #people
    self.stoptime=5 #seconds
    self.passengers=0
    

def simulate_elevator(b,e,starting_p):
  #creating the list of people in the building
  people = []
  for i in range(starting_p):
    people.append(Person((random.randint(1, b.floors)),random.randint(1, b.floors),0))
  
  new_arrived = 0
  
  while e.elapsedtime < 300:
    stopped = False
    
    #if the elevator has reached the top or bottom floor, it must change direction
    if e.location == 1:
      e.direction = 1
    elif e.location == b.floors:
      e.direction = -1
    
    
    for p in range(len(people)):
      #letting people into the elevator
      if (people[p].start == e.location) and (people[p].direction == e.direction):
        if e.passengers<e.capacity:
          people[p].inelevator = True
          stopped = True
          e.passengers += 1
          people[p].waittime = e.elapsedtime - people[p].arrival
        
      #letting people out of the elevator
      if (people[p].inelevator == True) and (people[p].end == e.location):
        people[p].direction=0
        people[p].inelevator = False
        stopped = True
        e.passengers -= 1

    #move elevator to the next floor
    e.location += e.direction

    #incrementing the elapsed time based on whether the elevator stopped or not
    e.elapsedtime += b.floor_height/e.speed
    if stopped:
      e.elapsedtime += e.stoptime

    #generating new people that are arriving at the building
    while (e.elapsedtime)//(b.traffic) > new_arrived:
        if random.randint(0,b.floors+1) > 3:
          people.append(Person(1,random.randint(1, b.floors),e.elapsedtime))
        else:
          people.append(Person(random.randint(2, b.floors),random.randint(1, b.floors),e.elapsedtime))
        new_arrived += 1
  
  total = 0
  counter = 0
  people = sorted(people, key=lambda p: p.start)
  for p in people:
    if p.waittime > 0:
        total += p.waittime
        counter += 1
        print(p.start,p.end,p.waittime)
  print(e.elapsedtime)
  
  return(total/counter)

def get_average(k):
    total = 0
    for _ in range(100):
        total += simulate_elevator(Building(9,4.5,k), Elevator(4.5,10), 1000)
    
    return(total/100)


data = []
for i in range(1,100):
    data.append([i/2,get_average(i/2)])

frame = pd.DataFrame(data,columns =['Time between each new arrival','Average wait time'])
fig = px.bar(frame, x='Time between each new arrival', y='Average wait time', title='Average wait time at various levels of traffic')
fig.show()

