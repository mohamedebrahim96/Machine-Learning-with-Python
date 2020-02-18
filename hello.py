


#x = ["s","v","m","e","t"]
#print(x[:3])

#x = "We are the so-called \"Vikings\" from the north."
"""print(len(x))"""
#print(x)


#print(3>1)


"""class Test():
    def __len__(self):
        return 0
myobj = Test()
print(myobj.__len__())

def amazing():
    return "Amazingg"
print(amazing())"""

"""def hiMan():
    return true
if hiMan:
    print("yes")
else:
    print("No")"""

"""x = 200
print(isinstance(x,int))"""


"""thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[0] = "apps"
print(thislist[:2])"""


#for loop example
"""thisList = ["man","woman","test"]
for x in thisList:
    print(x)"""


"""listty = ["Apple","banna","eminem"]
print(len(listty))
listty.insert(1,"sss")
listty.append("Dd")
listty.remove("banna")
listty.pop(1)
print(listty)"""

#list can be changed
#Tuples can't be changed
#sets is arraylist without index

"""thisset = {"apple", "banana", "cherry"}
thisset.add("ffff")
print(thisset)"""

"""if 5<7:
    print("TRUE")
    if 5<6:
        print("FALSE")
elif 4>2:
    print("Himohamed")"""

#one line statment
# if 5>3 and 3>2: print("momomo")

"""x = 0
while 55>44:
    print(x)
    if x==10:
        print("Done")
        break
    x += 1"""

"""listy = [66,77,88,99,5,33,22,11]
for x in listy:
    if x == 5:
        continue
    print(x)"""

"""def print_Maname(fName,lName):
    print("Hello, "+fName)
print_Maname(lName = "Test",fName = "Mohamed")
print_Maname(lName = "Test",fName = "Ahmed")"""

"""class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printMyAge(self):
        print("My age is: "+str(self.age))
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade

personn = Student("mohamed",34,33.5)
personn.printMyAge()
print(personn.grade)"""



#Example for global variable
"""x = 300
def changeMynumber():
    global x 
    x = 400
    print(x)

changeMynumber()
print(x)"""

'''import json
x = {"name":"mohamed","age": 23}
y = json.dumps(x)
yy = json.loads(y)
print(yy["name"])'''


