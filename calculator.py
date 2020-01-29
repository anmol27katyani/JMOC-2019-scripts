def calculator():
    expression = raw_input("Enter the expression to be calculated or type exit to exit the calculator")
    if expression == 'exit':
        return
    else:
        evaluate = eval(expression)
        print(evaluate)
        calculator()

calculator()
