#LAB11 Simple Calculator

while True:
    op_select = input("What operation (+, -, *, /) would you like to select? ")
    if op_select.capitalize() == "Done":
        print("Good bye!")
        break

    number_1 = int(input("What is the first number?"))
    number_2 = int(input("What is the second number?"))

    if op_select == "+":
        add_numbers = number_1 + number_2
        print(f'{number_1} {op_select} {number_2} = {add_numbers}')
    elif op_select == "-":
        sub_numbers = number_1 - number_2
        print(f'{number_1} {op_select} {number_2} = {sub_numbers}')
    elif op_select == "*":
        multiply_numbers = number_1 * number_2
        print(f'{number_1} {op_select} {number_2} = {multiply_numbers}')
    elif op_select == "/":
        divide_numbers = number_1 / number_2
        print(f'{number_1} {op_select} {number_2} = {divide_numbers}')

    else:
        print("Not valid operation")
        run_again = input("Would you like to try again? ").strip().lower()

        print('-'*60)
