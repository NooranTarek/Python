# def withinRange():
#     try:
#         number = int(input("enter a number: "))
#         if 20 <= number <= 50:
#             print("in the range.")
#         else:
#             print("not in the range.")
#     except ValueError:
#         print("enter a number please .. this input is not a number")

# withinRange()
#_________________________________________________________________________

# def getArea():
#     try:
#         length = int(input("enter a length: "))
#         width = int(input("enter a width: "))
#         if length <= 0 or width <= 0:
#             print("can't assign negative numbers or zero to width and height")
#         else:
#             print("area is", length * width)
#     except ValueError:
#         print("enter a number please .. this input is not a number")

# getArea()


#_________________________________________________________________________

# def getPrimeter(length, width):
#     try:
#         length = int(input("enter a length: "))
#         width = int(input("enter a width: "))
#         if length <= 0 or width <= 0:
#             print("can't assign negative numbers or zero to width and height")
#         else:
#              print("primeter is",2*(length+width))
#     except ValueError:
#         print("enter a number please .. this input is not a number")


# getPrimeter()

#_________________________________________________________________________

# def compineStrings(str1, str2):
#     print('the concated string is',str1 +" "+ str2 ,f"{str1} {str2}" ) 
# compineStrings("nouran","tarek")
#_________________________________________________________________________
# def square_list(values):
#     valuesSquared = []
#     for value in values:
#         valuesSquared.append(value * value)
#     print('the values squared are',valuesSquared) 

# values = [1, 2, 3, 4, 5]
# valuesSquared = square_list(values)
# print(valuesSquared)
# #_________________________________________________________________________
# def dictionariesCombination(dict1, dict2):
#     dict1.update(dict2)
#     return dict1

# dict1 = {"n": 1, "o": 2 ,"r":3}
# dict2 = {"t": 4, "a": 5 ,"k":6}
# dictionariesAfterCombine = dictionariesCombination(dict1, dict2)
# print(dictionariesAfterCombine)
#_________________________________________________________________________
# def listsMerging(l1, l2):
#     return l1 + l2
# list1 = ["n", "o", "u"]
# list2 = ["r", "a", "n"]
# listsAfterMerging = listsMerging(list1, list2)
# print(listsAfterMerging)
#_________________________________________________________________________

# def keysExistOrNot(dictionaryKeys,dictionary):
#     if dictionaryKeys.issubset(dictionary):
#         print(dictionaryKeys.issubset(dictionary),'keys exist in the dictionary :) ')
#     else :
#         print( dictionaryKeys.issubset(dictionary),'keys not exist in the dictionary :( ')

# dictionaryKeys = {"job", "card_number"}
# dictionary = {"name": "jone", "email": "jane@outlook.com", "age": 25,
# "job": "engineer", "address": "cairo, Egypt"}
# keysExistOrNot(dictionaryKeys,dictionary)
#_________________________________________________________________________
# def sumFrom1To100():
#     sum = 0
#     for number in range(1, 101):
#         sum += number
#     return sum
# print(sumFrom1To100())
#_________________________________________________________________________
# def evenOrOdd():
#     try:
#      number=int(input("enter a number: "))
#      if number % 2 == 0:
#         return "Even"
#      else:
#         return "Odd"
#     except ValueError:
#         return "enter a number please .. this input is not a number"
# print(evenOrOdd())
#_________________________________________________________________________
# def stringReverse():
#     valueOfString = input("enter a string to reverse: ")
#     stack = []
#     for char in valueOfString:
#         stack.append(char)
    
#     reversedString = ""
#     while stack:
#         reversedString += stack.pop()
#     print("string after reverse:", reversedString)

# reversed_string = stringReverse()
#_________________________________________________________________________
# def checkIfPalindrome ():
#     valueOfString = input("enter a string: ")
#     stack = []
#     for char in valueOfString:
#         stack.append(char)
    
#     reversedString = ""
#     while stack:
#         reversedString += stack.pop()
#     if valueOfString == reversedString:
#         print(valueOfString,"is Palindrome")
#     else:
#         print(valueOfString,"is not Palindrome")

# checkIfPalindrome()
#_________________________________________________________________________
# def oddSquaredNumbersInList(listOfNumber):
#     try:
#         oddSquaredNumbers = []
#         for num in listOfNumber:
#             if num % 2 != 0:
#              oddSquaredNumbers.append(num * num)
    
#         print(oddSquaredNumbers)
#     except TypeError:
#         return "sorry you entered a tring in the list cannt do this oparation."

# listOfNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# oddSquaredNumbers= oddSquaredNumbersInList(listOfNumber)
#_________________________________________________________________________
# def isPrimeOrNot():
#     try:
#         number=int(input("enter a number: "))
#         if number <= 1:
#             return False
#         if number % number == 0 & number%1==0:
#             return True
#     except ValueError:
#         return "enter a number please .. this input is not a number"

# print(isPrimeOrNot()) 
#_________________________________________________________________________
# def factrorialOf():
#     try:
#         factorial = 1
#         number = int(input("Enter a number: "))
#         if number < 0:
#             print("no factorial for negative numbers.")
#         else:
#             for i in range(1, number + 1):
#                 factorial *= i
#             print("Factorial of", number, "is", factorial)
#     except ValueError:
#         print("enter a number please. This input is not a number.")

# factrorialOf()
#_________________________________________________________________________
# def operationsOnNumbers(listOfNumbers, operation):
#     try:
#         if operation == 'sum':
#             result = sum(listOfNumbers)
#         elif operation == 'min':
#             result = min(listOfNumbers)
#         elif operation == 'max':
#             result = max(listOfNumbers)
#         elif operation == 'square':
#             squaredList = []
#             for num in listOfNumbers:
#                 squaredList.append(num * num)
#             result = squaredList
#         return result
#     except TypeError:
#         return "sorry you entered a string in the list cannt do this oparation."

# listOfNumbers = [1, 2, 3, 4, 5]
# operations = ['sum', 'min', 'max', 'square']
# for operation in operations:
#     result = operationsOnNumbers(listOfNumbers, operation)
#     print(f"{operation} of the list is {result}")

