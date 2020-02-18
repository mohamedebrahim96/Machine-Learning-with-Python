import numpy
from scipy import stats
listX = [1,2,3,4,5,6,7,8,9,6,6,5,138,28]

#The mean value is the average value.
#c = numpy.mean(listX
#)

#The median value is the value in the middle
#c = numpy.median(listX
#)

#find the number that appears the most
#c = stats.mode(listX
#)

#Standard Deviation is often represented by the symbol Sigma: σ
#s = numpy.std(listX
#)

#Variance is often represented by the symbol Sigma Square: σ2
#c = numpy.var(listX
#)

#=================================
#Percentiles
'''ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
percentile = numpy.percentile(ages, 1)
print(percentile)'''

import matplotlib.pyplot as plt

#y = numpy.random.uniform(0.0,0.5,1000)#Data Distribution
#y = numpy.random.normal(5.0,1.0,100000)#Normal Data Distribution
'''plt.hist(y, 100)
plt.show()'''

#Scatter Plot
'''x = numpy.random.normal(5.0,1.0,1000)
y = numpy.random.normal(5.0,1.0,1000)
plt.scatter(x, y)
plt.show()'''


#Linear Regression
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()








