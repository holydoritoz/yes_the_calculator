from art import logo

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
}

def calculator():
    print(logo)
    num1=float(input('Whats your number?: '))
    for symbol in operations:
        print(symbol)
    continueOp=True   # Exit flag
    while continueOp:
        for symbol in operations:
            print(symbol)
        operation_symbol=input('Pick an operation: ')
        num2=float(input('Whats your next number?: '))

        #Codigo de la calculadora
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)

        #Resultado
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        #Continuing de operations
        user_ex=input('Do you whant to continue calculating with the previos answer? Type "y" or Type "n" to start over: ').lower()
        if user_ex =='y':
            num1=answer
        else:
            continueOp=False
            calculator()

calculator()

