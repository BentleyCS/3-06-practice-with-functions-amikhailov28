#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(a, b, c):
    perimeter = (a + b + c) / 2
    return perimeter

#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(a, b, c, d):
    x = a * (a - b) * (a - c) * (a - d)
    return x

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a, b, c):
    x = semiPerimeter(a, b, c)
    y = multiplyDifferences(x, a, b, c)
    z = math.sqrt(y)
    return z

#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(a):
    return a * 2

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(b, d):
    x = -b + d
    y = -b - d
    return x, y

#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a, b, c):
    x = b * b - (4 * (a * c))
    return x

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a, b, c):
    x = mainCalc(a, b, c)
    d = math.sqrt(x)
    top1, top2 = plusMinus(b, d)
    root1 = top1 / denominator(a)
    root2 = top2 / denominator(a)
    return root1, root2
