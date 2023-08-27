
add = '+'
subtract = '-'
divide = '/'
multiply = '*'



def calculator(operator,input1,input2):
    if operator == add:
        result = input1 + input2
        print(result)
    elif operator == subtract:
        result = input1 - input2
        print(result)
    elif operator == multiply:
        result = input1 * input2
        print(result)
    elif operator == divide:
        result = input1 / input2
        print(result)
    else:
        print("Error, No solution")


print(calculator(add,5,8))