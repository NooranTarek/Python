# #import the decorator for abstact method
# from abc import ABC, abstractmethod
# import math
# #__________________________________________________________________________________
# #define class
# class Shape(ABC):
#     #define constructor self-->like this
#     def __init__ (self,name,color):
#         self.name=name
#         self.__color=color
#     #define seetters and getters
#     def getColor(self):
#         return self.__color
#     def setColor(self,color):
#         self.__color=color
#     @abstractmethod
#     def calculateArea(self):
#         pass
# #______________________________
# #define subclassess
# class Circle(Shape):
#     def __init__(self,color,radius):
#         super().__init__("circle",color)
#         self.radius=radius
#     def calculateArea(self):
#         if not isinstance(self.radius, (int, float)):
#             return("please provide radius as number")
#         if(self.radius<=0):
#             return "sorry area cannot be negative or zero"
#         else:
#             return math.pi*self.radius*self.radius
# #______________________________       
# class Square(Shape):
#     def __init__(self,color,length):
#         super().__init__("sqaure",color)
#         self.length=length

#     def calculateArea(self):
#         if not isinstance(self.length, (int, float)):
#             return("please provide length and width as numbers")
#         if(self.length<=0):
#             return "sorry area cannot be negative or zero"
#         else:
#             return self.length*self.length
# #______________________________
# class Rectangle(Shape): 
#     def __init__(self,color,length,width):
#          super().__init__("rectangle",color)
#          self.length=length
#          self.width=width

#     def calculateArea(self):
#          if not isinstance(self.length, (int, float)) or not isinstance(self.width, (int, float)):
#             return("please provide length as number")
#          if(self.width<=0 or self.length<=0):
#             return "sorry area cannot be negative or zero"
#          else:
#             return self.width*self.length

# #______________________________
# circle = Circle( "yellow", 5)
# square = Square("orange", 5)
# rectangle = Rectangle( "blue", 5, 5)

# print("AREA OF :")
# print("_________________")
# print("Circle:", circle.calculateArea())
# print("Square:", square.calculateArea())
# print("Rectangle:", rectangle.calculateArea())
#_____________________________________________________________________________________
# def studentsInfo(studentsFile):
#     studentsNames = []
#     studentsGrades = []
#     with open(studentsFile, 'r') as file:
#         #output = file.readlines()
#         #print(output)
#         for student in file:
#             splittedFile = student.split(' ')
#             studentsNames.append(splittedFile[0])
#             studentsGrades.append(int(splittedFile[1]))
#     #avarage        
#     total = sum(studentsGrades)
#     count = len(studentsGrades)
#     averageGradeOfStudents = total / count
#     print("avarage grade", averageGradeOfStudents)
#     #failed
#     for i,studentGrade in enumerate (studentsGrades):
#         if studentGrade < 60:
#              print("student with name : "+studentsNames[i]+" failed :(")

# studentsInfo('students.txt')
#_____________________________________________________________________________________
# import json

# numbers = [4, 9, 16, 25, 36]
# squaredNumbers = map(lambda num: num ** 2, numbers)

# numbersSquaredDict = {num: squaredNum for num, squaredNum in zip(numbers, squaredNumbers)}
# print("_______________________________________________________")
# print(numbersSquaredDict)
# print("_______________________________________________________")
# #toJson = json.dumps(numbersSquaredDict)
# #print(toJson)
# print("_______________________________________________________")
# with open('numbersAndSquare.json', 'w') as file:
#     #file.write(toJson)
#     json.dump(numbersSquaredDict,file)

#_____________________________________________________________________________________
# def make_negative(number):
#     if number >= 0:
#         return -number
#     else:
#         return number

# print(make_negative(1))
# print(make_negative(-5))
# print(make_negative(0))


# def basic_op(operator, value1, value2):
#     if operator == "+":
#         return value1 + value2
#     if operator == "-":
#         return value1 - value2
#     if operator == "*":
#         return value1 * value2
#     if operator == "/":
#         if value2 == 0:
#             return "invalid"
#         else:
#             return value1 / value2
#     return "invalid operator"  

# print(basic_op("+", 8, 2))
# print(basic_op("-", 8, 2))
# print(basic_op("*", 8, 2))
# print(basic_op("/", 8, 0))
# print(basic_op("/", 8, 2))
# print(basic_op("$", 8, 2))



def contains_value(arrayOfNumbers, value):
    return value in arrayOfNumbers

array = [1, 2, 3, 4, 5]
value = 22
print(contains_value(array, value))  
