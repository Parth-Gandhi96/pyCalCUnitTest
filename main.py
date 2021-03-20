import math

class cal():
    def __init__(self, calc_name):
        self.name = calc_name

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def subtract(self, a, b):
        return a - b

    def square(self, a):
        return a ** 2

    def square_root(self, a):
        return math.sqrt(a)

def main():
    calc_name = "Calculator 1"
    calculator = cal(calc_name)
    print(str(4) + '+' + str(3) + ' =', calculator.add(4,3))
    print(str(12) + '-' + str(3) + ' =', calculator.subtract(12,3))
    print(str(4) + '*' + str(5) + ' =', calculator.multiply(4,5))
    print(str(16) + '/' + str(2) + ' =', calculator.divide(16,2))
    print(str(5) + '^' + str(2) + ' =', calculator.square(5))
    print('sqrt ('+str(16) + ') =', calculator.square_root(16))


if __name__ == '__main__':
    main()