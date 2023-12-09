def fibonacci(n):
    numbers = [0] * n

    numbers[0] = 1
    numbers[1] = 1

    i = 2
    while i < n:
        numbers[i] = numbers[i - 1] + numbers[i - 2]
        i += 1

    return numbers


def bubleSort(mass, param):
    if param == 1:
        for i in range(len(mass) - 1):
            for j in range(len(mass) - i - 1):
                if mass[j] > mass[j + 1]:
                    temp = mass[j]
                    mass[j] = mass[j + 1]
                    mass[j + 1] = temp
    if param == 0:
        for i in range(len(mass) - 1):
            for j in range(len(mass) - i - 1):
                if mass[j] < mass[j + 1]:
                    temp = mass[j]
                    mass[j] = mass[j + 1]
                    mass[j + 1] = temp
    return mass


def calculate(num1, num2, operator):
    if operator == '*':
        return num1 * num2
    else:
        if operator == '/':
            return num1 / num2
        else:
            if operator == '+':
                return num1 + num2
            else:
                if operator == '-':
                    return num1 - num2
                else:
                    return Exception('not supported')
