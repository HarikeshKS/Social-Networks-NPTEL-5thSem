import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])      # the list provided in the function acts as the points on the Y-axis, thus the X-axis is by default taken as the indices of the respective elements in the list.
plt.show()

plt.plot([1,2,3,4,5],[1,4,9,16,25], 'g')  # this changes the colour of the line.
plt.show()
plt.plot([1,2,3,4,5],[1,4,9,16,25], 'go')  # this changes the colour as well as, shows the points.
plt.show()
plt.plot([1,2,3,4,5],[1,4,9,16,25], 'go-')  # this shows line inclusive of the above features.
plt.show()
# the things in the single qoutes here are known as MARKER.

# Check the documentation here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#
plt.plot([1,2,3,4,5],[1,4,9,16,25], 'yo-', linewidth = 3.0)  # this shows line inclusive of the above features, linewidth adds weight to the line, otherwise by default it's value is 1.0
plt.title("Brother")
plt.xlabel("Harikesh", fontsize=18, color='blue')
plt.ylabel("Hakusha")
# For changing the start of the axis values, the following function can be used.
plt.axis([0,6,0,30])
plt.grid() # Displays the grid also
plt.show()

# creating list using for loop:
x = [i for i in range(20)]
# we use the numpy package to apply the arithematic operations on a structure of data that is similar to a list, that's why numpy is used
import numpy
x = numpy.array(x)
plt.plot(x,x**2,'r-',x,x**3,'b-',x,x**4,'g-')
plt.show()

# There are different types of plots: 
# Scatter
import random
a = [random.randint(1,100) for i in range(100)]
b = [random.randint(1,100) for i in range(100)]
plt.scatter(a,b)
plt.axis([0,100,0,100])
plt.show()

# Bar Chart
plt.bar(a,b)
plt.axis([0,100,0,100])
plt.show()