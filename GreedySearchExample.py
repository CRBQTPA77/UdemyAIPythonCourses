class Vertex:

  def __init__(self, label, distance_objective):
    self.label = label
    self.visited = False
    self.distance_objective = distance_objective
    self.adjacent = []

  def add_adjacent(self, adjacent):
    self.adjacent.append(adjacent)

  def print_adjacent(self):
    for i in self.adjacent:
      print(i.vertex.label, i.cost)

class Adjacent:
  def __init__(self, vertex, cost):
    self.vertex = vertex
    self.cost = cost

class Graph:
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
    # negative one -1 is used because it is outside the range of valid index positions
    # which start at ZERO
    self.last_position = -1

    # Creates an empty array with a size equal to 'capacity',
    # and specifies that the array will store integers (dtype='int').
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
        print(i, ' - ', self.values[i].label, ' - ', self.values[i].distance_objective)

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
  def __init__(self,objective):
    self.objective = objective
    self.found = False
  
  def search(self, current):
    print('----------- ')
    print('Current: {}'.format(current.label))
    current.visited = True

    if current == self.objective:
      self.found = True
    else:
      ordcered_array = OrderedArray(len(current.adjacent))
      for adjacent in current.adjacent:
        if adjacent.vertex.visited == False:
          adjacent.vertex.visited = True
          ordcered_array.insert(adjacent.vertex)
      ordcered_array.print()

      if ordcered_array.values[0] != None:
        self.search(ordcered_array.values[0])

greedy_search = Greedy(graph.bucharest)
greedy_search.search(graph.arad)
