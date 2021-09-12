#!/usr/bin/env python3
# coding=utf-8

# Программа получает значения A B X и выводит Y согласно
# y = (6 * x^2 + a * b) / (2*x^2), x > 6
# y = 4 * (x + a^2 + b^2), x <= 6


def main():
    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x > 6:
        print("X больше 6, применяем формулу:")
        print("(6 * x^2 + a * b) / (2*x^2)")
        y = (6 * x**2 + a * b) / (2*x**2)
    else:
        print("X меньше или равно 6, применяем формулу:")
        print("4 * (x + a^2 + b^2)")
        y = 4 * (x + a**2 + b**2)
    print("y = %.3f" % y)


if __name__ == '__main__':
    main()
