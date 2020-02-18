import numpy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas
from sklearn import linear_model

listX = [1,2,3,4,5,6,7,8,9,6,6,5,138,28]

#The mean value is the average value.
#c = numpy.mean(listX)

#The median value is the value in the middle
#c = numpy.median(listX)

#find the number that appears the most
#c = stats.mode(listX)

#Standard Deviation is often represented by the symbol Sigma: σ
#s = numpy.std(listX)

#Variance is often represented by the symbol Sigma Square: σ2
#c = numpy.var(listX)

#=================================
#Percentiles
'''ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
percentile = numpy.percentile(ages, 1)
print(percentile)'''


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
'''x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
#predictModel = myfunc(10)
#print(predictModel)
print(r) #The relationship is measured with a value called the r-squared.
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()'''


#Polynomial Regression
'''x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 22, 50)
print(r2_score(y, mymodel(x)))
print(mymodel(17))# predict the speed of the car
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()'''


#Polynomial Regression (BAD FIT)
'''x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(2, 95, 100)

print(r2_score(y,mymodel(x)))
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()'''


'''df = pandas.read_csv("cars.csv")
X = df[['Dimensions.Length', 'Dimensions.Height']]
y = df['Fuel Information.Highway mpg']
regr = linear_model.LinearRegression()
regr.fit(X, y)
print(regr.coef_)'''



x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

#plt.scatter(x, y)
#plt.show()

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]












