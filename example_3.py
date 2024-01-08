#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    s = input("Введите предложение: ")
    n = int(input("Введите длину: "))

    # Проверить требуемую длину
    if len(s) >= n:
        print("Заданная длина должна быть больше длины предложения", file=sys.stderr)
        exit(1)


    # Разделить предложение на слова
    words = s.split(' ')
    # Проверить количество слов в предложении
    if len(words) < 2:
        print("Предложение должно содержать несколько слов", file=sys.stderr)
        exit(1)

