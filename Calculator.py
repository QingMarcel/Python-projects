"""
This is my first python project.
A simple calculator, that adds, subtracts, multiply and divide.
"""
#declartion of variable operation, this wil define the 
#operation to carry out

def addition_operation(a,b):
    return a + b
def subtraction_operation(a,b):
    return a - b
def multiplication_operation(a,b):
    return a * b
def division_operation(a,b):
    return a / b

"""
operations include
1. add
2. subtract
3. multiply
4. divide
"""
# Definition of functions
def decide_operation():
    print("What Operation do you want to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    decision = int(input("Enter the corresponding number: "))
    return decision
    
def carryOut_operation(decision):
    if decision == 1:
        num1 = float(input("Enter number: "))
        print( num1,"+")
        num2 = float(input(""))
        result = addition_operation(num1,num2)
    elif decision == 2:
        num1 = float(input("Enter number: "))
        print( num1,"-")
        num2 = float(input(""))
        result = subtraction_operation(num1,num2)
    elif decision == 3:
        num1 = float(input("Enter number: "))
        print( num1,"*")
        num2 = float(input(""))
        result = multiplication_operation(num1,num2)
    elif decision == 1:
        num1 = float(input("Enter number: "))
        print( num1,"/")
        num2 = float(input(""))
        result = division_operation(num1,num2)
    else:
        print(decision, "is not part of the required number")
    return result

    
def dislay_result(a):
    print("The answer =", a)

# Main Function/Program
decision = decide_operation()
result = carryOut_operation(decision)
dislay_result(result)