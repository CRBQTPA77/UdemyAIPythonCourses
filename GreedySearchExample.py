# this is an implementation of greedy search.  it starts with a heuristic that, in 
# this case, is the straight line distance from each city to the destination.  
# here we are starting in a city called Arad and for each neighboring (adjacent)
# city it will select the one with the shorted straight line distnace to the 
# destination city called Bucharest.  It then starts at that city and repeats 
# the process to select the next city with the shortest straight line distance to
# the destination Bucharest until we reach the destination.  the path it selects should
# be the shortest path to Bucharest.

'''
# the following classes are defined and they each store their objects in an array
# however Python does not a data element called array so a list is used.

classes are:
1 - Vertex with objects label and distance_objective and an "array" aka list
# called self.adjacent is created that 

2 - Adjacent
'''

class Vertex:
  # this will execute each time we create a new object aka an instance
  # of this class
  # "label" is the name of the city and "distance_objective" is the heuristic
  # which is the number of kilometers from each city to the desitination city
  # of Bucharest if we draw a straight line on the map
  def __init__(self, label, distance_objective):
    # the next line recieves the city name as a parameter
    self.label = label
    # we're setting visited to False so we don't "visit" the same city twice
    self.visited = False
    # the next line recieves the straight line distance to Bucharest as a parameter
    self.distance_objective = distance_objective
    # creating an empty array (same as a list[]) that will eventually store the cities adjacent or 
    # connected to the starting city for each run.  The first ones will be the 
    # adjacent citys to Arad which are Zerind, Sibiu, and Timisoara
    self.adjacent = []

  def add_adjacent(self, adjacent):
    # next line access the list "self.adjacent" and appends all of the connections
    # to the self.adjacent list
    self.adjacent.append(adjacent)

  def print_adjacent(self):
    # this does not print on the run of the program?
    for i in self.adjacent:
      print('City name:', i.vertex.label, 'Heuristics or straight line distance to Bucharest:', i.cost)

class Adjacent:
  # this accepts the vertex and the cost as an attribute
  def __init__(self, vertex, cost):
    self.vertex = vertex
    self.cost = cost

class Graph:
  # these values are the heuristics which are the straight line distnace from
  # each city to the distination city called Buchrest.  This is the "as the crow
  # flies" distance, not necessarily the path that has an actual road on it

  # When the program starts, the Vertex is the city you are which is Arad.  The adjacent cities in the second list 
  # are the cities that are directly connected to the vertex.  once the adjacent wit the shortest
  # straight line distance to Bucharest is found, that adjacent becomes the next
  # vertex and then it's adjacents are evaluated looking for the one with the 
  # shortest SLD (straight line distance) to Bucharest
  arad = Vertex('Arad', 366)
  zerind = Vertex('Zerind', 374)
  oradea = Vertex('Oradea', 380)
  sibiu = Vertex('Sibiu', 253)
  timisoara = Vertex('Timisoara', 329)
  lugoj = Vertex('Lugoj', 244)
  mehadia = Vertex('Mehadia', 241)
  dobreta = Vertex('Dobreta', 242)
  craiova = Vertex('Craiova', 160)
  rimnicu = Vertex('Rimnicu', 193)
  fagaras = Vertex('Fagaras', 176)
  pitesti = Vertex('Pitesti', 98)
  bucharest = Vertex('Bucharest', 0)
  giurgiu = Vertex('Giurgiu', 77)
  urziceni = Vertex('Urziceni', 80)
  hirsova = Vertex('Hirsova', 151)
  eforie = Vertex('Eforie', 161)
  vaslui = Vertex('Vaslui', 199)
  iasi = Vertex('Iasi', 226)
  neamt = Vertex('Neamt', 234)

  arad.add_adjacent(Adjacent(zerind, 75))
  arad.add_adjacent(Adjacent(sibiu, 140))
  arad.add_adjacent(Adjacent(timisoara, 118))
  zerind.add_adjacent(Adjacent(arad, 75))
  zerind.add_adjacent(Adjacent(oradea, 71))
  oradea.add_adjacent(Adjacent(zerind, 71))
  oradea.add_adjacent(Adjacent(sibiu, 151))
  sibiu.add_adjacent(Adjacent(oradea, 151))
  sibiu.add_adjacent(Adjacent(arad, 140))
  sibiu.add_adjacent(Adjacent(fagaras, 99))
  sibiu.add_adjacent(Adjacent(rimnicu, 80))
  timisoara.add_adjacent(Adjacent(arad, 118))
  timisoara.add_adjacent(Adjacent(lugoj, 111))
  lugoj.add_adjacent(Adjacent(timisoara, 111))
  lugoj.add_adjacent(Adjacent(mehadia, 70))
  mehadia.add_adjacent(Adjacent(lugoj, 70))
  mehadia.add_adjacent(Adjacent(dobreta, 75))
  dobreta.add_adjacent(Adjacent(mehadia, 75))
  dobreta.add_adjacent(Adjacent(craiova, 120))
  craiova.add_adjacent(Adjacent(dobreta, 120))
  craiova.add_adjacent(Adjacent(pitesti, 138))
  craiova.add_adjacent(Adjacent(rimnicu, 146))
  rimnicu.add_adjacent(Adjacent(craiova, 146))
  rimnicu.add_adjacent(Adjacent(sibiu, 80))
  rimnicu.add_adjacent(Adjacent(pitesti, 97))
  fagaras.add_adjacent(Adjacent(sibiu, 99))
  fagaras.add_adjacent(Adjacent(bucharest, 211))
  pitesti.add_adjacent(Adjacent(rimnicu, 97))
  pitesti.add_adjacent(Adjacent(craiova, 138))
  pitesti.add_adjacent(Adjacent(bucharest, 101))
  bucharest.add_adjacent(Adjacent(fagaras, 211))
  bucharest.add_adjacent(Adjacent(pitesti, 101))
  bucharest.add_adjacent(Adjacent(giurgiu, 90))
  bucharest.add_adjacent(Adjacent(urziceni, 85))
  giurgiu.add_adjacent(Adjacent(bucharest, 90))
  urziceni.add_adjacent(Adjacent(bucharest, 85))
  urziceni.add_adjacent(Adjacent(hirsova, 98))
  hirsova.add_adjacent(Adjacent(urziceni, 98))
  hirsova.add_adjacent(Adjacent(eforie, 86))
  eforie.add_adjacent(Adjacent(hirsova, 86))
  vaslui.add_adjacent(Adjacent(iasi, 92))
  iasi.add_adjacent(Adjacent(vaslui, 92))
  iasi.add_adjacent(Adjacent(neamt, 87))
  neamt.add_adjacent(Adjacent(iasi, 87))

# this creates and object with all of the vertexes and all of the adjacents
graph = Graph()

# Ordered Array

import numpy as np

class OrderedArray:
  # Constructor: Initializes the OrderedArray object with a given capacity
  def __init__(self, capacity):
    # 'capacity' is the maximum number of elements the array can hold
    self.capacity = capacity

    # The 'last_position' keeps track of the last filled index in the array.
    # It's initialized to -1 to signify that the array is empty.
    # The first valid index in the array is 0, so -1 acts as a placeholder for an empty array.
    # -1 is used because it is outside the range of valid index positions
    # which start at ZERO
    self.last_position = -1

    # Creates an empty array with a size equal to 'capacity',
    # and specifies that the array will store objects (an instance of a class)
    # CHANGED =INT TO =OBJECT FOR MAP USE CASE
    self.values = np.empty(self.capacity, dtype=object)

  def print(self):
    # This method prints the content of the array.

    # If 'last_position' is -1, it means the array is empty, so print a message.
    if self.last_position == -1:
      print('The array is empty')
    else:
      # If the array is not empty, iterate through each position in the array
      # from index 0 to 'last_position' and print the index and the value at that index.
      # we are adding 1 below because when you use range, the values stop 1 position short
      # of the upper end of the range you define. For example "...range(0,3)"
      # will have 3 positions, 0, 1, and 2. 3 is not part of the range so for
      # example if the range of this array was 10, you could replace the next
      # line with "...range(0,11)"
      for i in range(self.last_position + 1):
        # ADDED .LABEL AND .DISTANCE_OBJECTIVE FOR MAP USE CASE
        print('Current row in the array is', i, ' - current city is', self.values[i].label, ' - SLD to Bucharest is', self.values[i].distance_objective, 'km')
        # print('printing i', self.values[i])

  # CHANGED VALUE TO VERTEX FOR MAP USE CASE
  def insert(self, vertex):
    # This method inserts a value into the array while maintaining order.

    # Check if the array is full by comparing 'last_position' to the 'capacity' - 1.
    # If the array is full, print a message and return.
    # "-1" is used because if the capacity is 10, the last index position would
    # be 9 and the index numbers would be 0,1,2,3,4,5,6,7,8,9 for 10 positions
    if self.last_position == self.capacity - 1:
      print('The array is full')
      return

    # If the array is not full, we need to find the correct position to insert the new value.
    position = 0
    # we are adding 1 below because when you use range, the values stop 1 position short
    # of the upper end of the range you define. For example "...range(0,3)"
    # will have 3 positions, 0, 1, and 2. 3 is not part of the range so for
    # example if the range of this array was 10, you could replace the next
    # line with "...range(0,11)"
    for i in range(self.last_position + 1):
      position = i
      #print('this is the position in the for loop of the insert function!', position)
      # the array is ordered so if we start from the lower index number, we
      # know that all values to the right of it, at a higher index number,
      # will be larger.  So, if we come across a value that is greater than
      # the new value, it must be in the position that we must place the
      # new value.  In other words, if we find a value in the array that is
      # greater than the new value, it means we've found the correct
      # insertion position.
      # ADDED .DISTANCE_OBJECTIVE AND CHANGED VALUE TO VERTEX FOR MAP USE CASE
      if self.values[i].distance_objective > vertex.distance_objective:
        #print(' we have found the index position to place the new value!', i)
        break
      # If we reach the last position, then the new value should be inserted
      # right after the last element.
      if i == self.last_position:
        #print('i represents the value to be moved:', i)
        #print('first we\' print the postion of it before it\'s moved:', position)
        position = i + 1
        #print('second we\' print the postion of it after it\'s moved:', position)
    # Now, we need to shift larger values to the right to make room for the new value.
    # We start by storing the current last position in 'x'.
    x = self.last_position

    # Shift elements to the right starting from the 'last_position' and moving backwards
    # until we reach the 'position' where the new value will be inserted.
    while x >= position:
      # Move the current value in 'x' to the next position (x + 1).
      self.values[x + 1] = self.values[x]
      # Decrement 'x' to move to the previous index.
      x -= 1

    # Insert the new value at the correct position (position found earlier).
    # CHANGED = VALUE TO = VERTEX FOR MAP USE CASE
    self.values[x + 1] = vertex

    # After inserting the value, we update 'last_position' to reflect the new last filled index.
    # This is done by incrementing 'last_position' by 1.
    self.last_position += 1

array = OrderedArray(5)
array.insert(graph.arad)
array.insert(graph.craiova)
array.insert(graph.bucharest)
array.insert(graph.dobreta)

array.print()

print(array), array.values[0].label, array.values[1].label

# this is an implementation of greedy search.  it starts with a heuristic that, in 
# this case is the straight line distance from each city to the destination.  
# here we are starting in a city called Arad and for each neighboring (adjacent)
# city it will select the one with the shorted straight line distnace to the 
# destination city called Bucharest.  It then starts at that city and repeats 
# the process to select the next city the the shortest straight line distance to
# the destination Bucharest
class Greedy:
  # this creates and object and accepts the objective (aka destination city) as
  # a parameter
  def __init__(self,objective):
    # this line sets self.objective to the parameter that was passed in
    # self.objective is a variable in the new instance of Greedy
    self.objective = objective
    # next line sets found to false since we just passed the destination city
    # and created the object.  If we were already at the destination, we would not
    # need to use Greedy to find the shorted path.
    self.found = False
  
  def search(self, current):
    # label, visited, distance_objective, and 
    # adjacent were all created in the Vertex class
    # these are all attributes of the object called current.  This is how we
    # can have multiple values within the array at the same index position.
    print('----------- ')
    print('Current: {}'.format(current.label))
    current.visited = True

    # if our current city is the objective do this
    if current == self.objective:
      self.found = True
      print('This is the destination city!', current)
    # if the current city is not the objective, do this
    else:
      # set ordered_array to be an object of the "OrderedArray" class
      # and pass in the length of current.adjacent which will be set to
      # capacity in that class which is the number of objects that the 
      # array can hold aka the size of the lis of adjacents
      # it passes in all adjacents for the current city which we entered
      # above here.  For Arad, there are 3 adjacents so that will be the 
      # capacity for this run of the class
      ordered_array = OrderedArray(len(current.adjacent))
      # this for loop will go through the list lf adjacents for the current
      # city which, when we start will be Arad and adjacents will be Zerind,
      # Sibiu, and Timisoara

      #
      for adjacent in current.adjacent:
        # only do this if we have not already visted the city
        if adjacent.vertex.visited == False:
          # first set it to visited since we are here now
          adjacent.vertex.visited = True
          # now insert all adjacents for the current city to the ordered_array
          # and we know doing that will put them in order from smallest heuristic
          # aka straight line distance to our destination to largest
          # this insures the first element of the array, in postion [0], will 
          # be the one we want
          ordered_array.insert(adjacent.vertex)
      # once the list has been created that contains all of the stops we 
      # must make, print it - think of it as printing directions!
      ordered_array.print()

      if ordered_array.values[0] != None:
        # this will call search (WHICH IS FUNCTION WE ARE CURRENTLY IN = THAT IS 
        # KNOWW AS RECURSION!) and pass to it the current adjacent with the 
        # shorted distnace to Bucharest
        # this is how we trigger search to run after the first time it is called
        # in main program at the bottom
        # this passes the adjacent of the previous visted city so it's adjacents
        # can be found and passed to the array so the shortest path city can be
        # printed making up our "directions" to Bucharest!
        self.search(ordered_array.values[0])

# this is basically the main program that kicks off the execution of greedy search
greedy_search = Greedy(graph.bucharest)
greedy_search.search(graph.arad)
