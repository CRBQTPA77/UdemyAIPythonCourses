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
    self.values = np.empty(self.capacity, dtype='int')

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
        print(i, ' - ', self.values[i])
  
  def insert(self, value):
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
      print('this is the position in the for loop of the insert function!', position)
      # the array is ordered so if we start from the lower index number, we
      # know that all values to the right of it, at a higher index number, 
      # will be larger.  So, if we come across a value that is greater than
      # the new value, it must be in the position that we must place the
      # new value.  In other words, if we find a value in the array that is 
      # greater than the new value, it means we've found the correct 
      # insertion position.
      if self.values[i] > value:
        print(' we have found the index position to place the new value!', i)
        break
      # If we reach the last position, then the new value should be inserted 
      # right after the last element.
      if i == self.last_position:
        print('i represents the value to be moved:', i)
        print('first we\' print the postion of it before it\'s moved:', position)
        position = i + 1
        print('second we\' print the postion of it after it\'s moved:', position)
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
    self.values[x + 1] = value
    
    # After inserting the value, we update 'last_position' to reflect the new last filled index.
    # This is done by incrementing 'last_position' by 1.
    self.last_position += 1

# Example usage:
array = OrderedArray(10)   # Create an OrderedArray with capacity of 10 elements.
array.insert(6)            # Insert value 6 into the array.
array.insert(2)            # Insert value 6 into the array.
array.insert(7)            # Insert value 6 into the array.
array.insert(1)            # Insert value 6 into the array.
array.insert(0)            # Insert value 6 into the array.
array.insert(16)            # Insert value 6 into the array.
array.insert(88)            # Insert value 6 into the array.
array.insert(12)            # Insert value 6 into the array.
array.insert(5)            # Insert value 6 into the array.
array.insert(2)            # Insert value 6 into the array.
array.insert(121)            # Insert value 6 into the array.
array.print()              # Print the current values in the array.