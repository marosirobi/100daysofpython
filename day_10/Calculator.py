def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
def calc():
    calc_with_final = True
    num1 = float(input('Enter first number: '))

    while calc_with_final:

        for operator in operations:
            print(operator)
        operator = input('Enter an operator: ')
        num2 = float(input('Enter second number: '))
        final = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {final}")
        run_or_stop = input(f'Type True if you want to continue with {final} or False if you want to quit. ').title()
        if run_or_stop == "False":
            calc_with_final = False
            print("\n" * 20)
            calc()
        else:
            calc_with_final = True
            num1 = final

calc()
